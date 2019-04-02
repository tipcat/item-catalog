import random
import string
import httplib2
import json
import requests
from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from catalog_setup import Base, Genre, Album
from datetime import timedelta

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())[
    'web']['client_id']
APPLICATION_NAME = "Music Catalog"

# Connect to Database and create database session
engine = create_engine('sqlite:///musiccatalog.db')
Base.metadata.bind = engine


def newSession():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


# Make session finite; new login required after 15 minutes of inactivity
@app.before_request
def enforce_timeout():
    login_session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)


# Create anti-forgery state token immediately
@app.route('/')
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(
            string.ascii_uppercase +
            string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Login via google
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' %
        access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    google_id = credentials.id_token['sub']
    if result['user_id'] != google_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_google_id = login_session.get('google_id')
    if stored_access_token is not None and google_id == stored_google_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['google_id'] = google_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' style = "width: 150px; height: 150px '
    output += 'border-radius: 150px;-webkit-border-radius: 150px; '
    output += '-moz-border-radius: 150px;">'
    print 'username: ' + login_session['username']
    print 'email: ' + login_session['email']
    enforce_timeout()
    return output


# Disconnect from google
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % credentials
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['google_id']
        del login_session['username']
        del login_session['picture']
        del login_session['email']
        del login_session['provider']
        return render_template('disconnect.html')
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# Define JSON endpoints to view Genre and Album Information
@app.route('/genre/<int:genre_id>/album/JSON')
def genreAlbumsJSON(genre_id):
    session = newSession()
    genre = session.query(Genre).filter_by(id=genre_id).one()
    albums = session.query(Album).filter_by(genre_id=genre_id).all()
    return jsonify(Albums=[album.serialize for album in albums])


@app.route('/genre/<int:genre_id>/album/<int:album_id>/JSON')
def oneAlbumJSON(genre_id, album_id):
    session = newSession()
    album = session.query(Album).filter_by(id=album_id).one()
    return jsonify(album=album.serialize)


@app.route('/genre/JSON')
def genresJSON():
    session = newSession()
    genres = session.query(Genre).all()
    return jsonify(genres=[genre.serialize for genre in genres])


# Show all available genres of music
@app.route('/genre/')
def showGenres():
    session = newSession()
    if 'username' not in login_session:
        return redirect('/login')
    genres = session.query(Genre).order_by(asc(Genre.name))
    return render_template('genre.html', genres=genres)


# Create a new genre
@app.route('/genre/new/', methods=['GET', 'POST'])
def newGenre():
    session = newSession()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newGenre = Genre(
            name=request.form['name'],
            creator=login_session['email'])
        session.add(newGenre)
        session.commit()
        return redirect(url_for('showGenres'))
    else:
        return render_template('newgenre.html')


# Delete a genre
@app.route('/genre/<int:genre_id>/delete/', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    session = newSession()
    if 'username' not in login_session:
        return redirect('/login')
    genreToDelete = session.query(Genre).filter_by(id=genre_id).one()
    if genreToDelete.creator != login_session['email']:
        return "<script> function myFunction() {alert('You may only delete a genre if you created it. Returning to catalog.'); window.location.href='/genre/'}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(genreToDelete)
        session.commit()
        return redirect(url_for('showGenres', genre_id=genre_id))
    else:
        return render_template('deletegenre.html', genre=genreToDelete)


# Show albums in a given genre (user selects)
@app.route('/genre/<int:genre_id>/')
@app.route('/genre/<int:genre_id>/genrelist/')
def showAlbums(genre_id):
    session = newSession()
    if 'username' not in login_session:
        return redirect('/login')
    genre = session.query(Genre).filter_by(id=genre_id).one()
    albums = session.query(Album).filter_by(genre_id=genre_id).all()
    return render_template('albums.html', albums=albums, genre=genre)


# Create a new album
@app.route('/genre/<int:genre_id>/album/new/', methods=['GET', 'POST'])
def newAlbum(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    session = newSession()
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        newAlbum = Album(
            artist=request.form['artist'],
            title=request.form['title'],
            creator=login_session['email'],
            description=request.form['description'],
            price='$' + request.form['price'],
            genre_id=genre_id)
        session.add(newAlbum)
        session.commit()
        return redirect(url_for('showAlbums', genre_id=genre_id))
    else:
        return render_template('newalbum.html', genre_id=genre_id)


# Edit an album
@app.route(
    '/genre/<int:genre_id>/album/<int:album_id>/edit', methods=['GET', 'POST'])
def editAlbum(genre_id, album_id):
    if 'username' not in login_session:
        return redirect('/login')
    session = newSession()
    editedAlbum = session.query(Album).filter_by(id=album_id).one()
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if editedAlbum.creator != login_session['email']:
        return "<script> function myFunction() {alert('You may only edit an album if you created it. Returning to catalog.'); window.location.href='/genre/'}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['artist']:
            editedAlbum.artist = request.form['artist']
        if request.form['title']:
            editedAlbum.title = request.form['title']
        if request.form['description']:
            editedAlbum.description = request.form['description']
        if request.form['price']:
            editedAlbum.price = request.form['price']
        session.add(editedAlbum)
        session.commit()
        return redirect(url_for('showAlbums', genre_id=genre_id))
    else:
        return render_template(
            'editalbum.html',
            genre_id=genre_id,
            album_id=album_id,
            album=editedAlbum)


# Delete an album
@app.route(
    '/genre/<int:genre_id>/album/<int:album_id>/delete',
    methods=[
        'GET',
        'POST'])
def deleteAlbum(genre_id, album_id):
    if 'username' not in login_session:
        return redirect('/login')
    session = newSession()
    genre = session.query(Genre).filter_by(id=genre_id).one()
    albumToDelete = session.query(Album).filter_by(id=album_id).one()
    if albumToDelete.creator != login_session['email']:
        return "<script> function myFunction() {alert ('You may only delete an album if you created it. Returning to catalog.'); window.location.href='/genre/'} </script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(albumToDelete)
        session.commit()
        return redirect(url_for('showGenres', genre_id=genre_id))
    else:
        return render_template('deletealbum.html', album=albumToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
