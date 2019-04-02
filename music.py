from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog_setup import Genre, Base, Album

engine = create_engine('sqlite:///musiccatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

email="tipcatdp@gmail.com"
# Starter items to be added to databsse -- 8 albums in 6 genres

# Indie Rock Albums
indie = Genre(name="Indie Rock", creator=email)
session.add(indie)
session.commit()


album1 = Album(
    artist="Guided By Voices",
    title="Bee Thousand (1994)",
    description="Seminal genre-defining album from Ohio lo-fi stalwarts",
    creator=email,
    price="$17.99",
    genre=indie)
session.add(album1)
session.commit()


album2 = Album(
    artist="Pavement",
    title="Slanted and Enchanted (1991)",
    description="Arguably THE indie rock album",
    creator=email,
    price="$17.99",
    genre=indie)
session.add(album2)
session.commit()

album3 = Album(
    artist="Sebadoh",
    title="Bubble and Scrape (1993)",
    description="Slacker lo-fi anthems for the socially challenged",
    creator=email,
    price="$15.99",
    genre=indie)
session.add(album3)
session.commit()

album4 = Album(
    artist="Sonic Youth",
    title="Daydream Nation (1988 - double album)",
    description="Innovative classic from NYC noise pioneers",
    creator=email,
    price="$31.99",
    genre=indie)
session.add(album4)
session.commit()

album5 = Album(
    artist="My Bloody Valentine",
    title="Loveless (1991)",
    description="Trailblazing 'shoegaze' album, still massively influential",
    creator=email,
    price="$27.99",
    genre=indie)
session.add(album5)
session.commit()

album6 = Album(
    artist="Arcade Fire",
    title="Funeral (2004)",
    description="Released to universal acclaim, vital indie rock for the 00s",
    creator=email,
    price="$19.99",
    genre=indie)
session.add(album6)
session.commit()

album7 = Album(
    artist="Beach House",
    title="Teen Dream (2010)",
    description="Hazy lo-fi dream pop beauty",
    creator=email,
    price="$18.99",
    genre=indie)
session.add(album7)
session.commit()

album8 = Album(
    artist="Snail Mail",
    title="Lush (2018)",
    description="The new indie rock standard bearer",
    creator=email,
    price="$21.99",
    genre=indie)
session.add(album8)
session.commit()


# Classic Rock Albums
classic_rock = Genre(name="Classic Rock", creator=email)
session.add(classic_rock)
session.commit()


album1 = Album(
    artist="The Beatles",
    title="The Beatles [White Album] (1968)",
    description="The White Album. What more can one say?",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album1)
session.commit()

album2 = Album(
    artist="The Rolling Stones",
    title="Exile on Main Street (1972 - double album)",
    description="The finest record from the Stones",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album2)
session.commit()

album3 = Album(
    artist="Led Zeppelin",
    title="IV (1971)",
    description="\"Stairway to Heaven\" and the sound of 70s hard rock",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album3)
session.commit()

album4 = Album(
    artist="The Kinks",
    title="Lola Versus Powerman and the Moneygoround, Part One (1970)",
    description="\"Lola\" and other gems from these British Invasion veterans",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album4)
session.commit()

album5 = Album(
    artist="The Who",
    title="Quadrophenia (1973)",
    description="The last of The Who's rock \'operas\'",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album5)
session.commit()

album6 = Album(
    artist="The Doors",
    title="The Doors (1967)",
    description="A defining statement of its time",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album6)
session.commit()

album7 = Album(
    artist="Jimi Hendrix",
    title="Are You Experienced? (1967)",
    description="He reinvented the guitar and then some",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album7)
session.commit()

album8 = Album(
    artist="Fleetwood Mac",
    title="Rumours (1977)",
    description="20 million copies sold, a soft rock classic of the 70s",
    creator=email,
    price="$21.99",
    genre=classic_rock)
session.add(album8)
session.commit()

# Punk
punk = Genre(name="Punk", creator=email)
session.add(punk)
session.commit()

album1 = Album(
    artist="Ramones",
    title="Ramones(1976)",
    description="The first true punk album that changed rock forever",
    creator=email,
    price="$18.99",
    genre=punk)
session.add(album1)
session.commit()

album2 = Album(
    artist="Sex Pistols",
    title="Never Mind The Bollocks, Here's The Sex Pistols",
    description="The band that made people fear punk rock",
    creator=email,
    price="$18.99",
    genre=punk)
session.add(album2)
session.commit()

album3 = Album(
    artist="The Clash",
    title="London Calling (1979)",
    description="The punk band that performed radio friendly anthems",
    creator=email,
    price="$22.99",
    genre=punk)
session.add(album3)
session.commit()

album4 = Album(
    artist="Buzzcocks",
    title="Another Music in a Different Kitchen (1978)",
    description="The poppiest of the punks",
    creator=email,
    price="$17.99",
    genre=punk)
session.add(album4)
session.commit()

album5 = Album(
    artist="X",
    title="Los Angeles (1980)",
    description="Los Angeles punk rockers depict decadent glory",
    creator=email,
    price="$15.99",
    genre=punk)
session.add(album5)
session.commit()

album6 = Album(
    artist="The Slits",
    title="Cut (1979)",
    description="A feminist punk classic",
    creator=email,
    price="$13.99",
    genre=punk)
session.add(album6)
session.commit()

album7 = Album(
    artist="Wire",
    title="Pink Flag (1977)",
    description="Art-punk at its finest, pointed the way toward post-punk",
    creator=email,
    price="$21.99",
    genre=punk)
session.add(album7)
session.commit()

album8 = Album(
    artist="Crass",
    title="Penis Envy (1981)",
    description="Dangerous and uncompromising as punk should be",
    creator=email,
    price="$31.99",
    genre=punk)
session.add(album8)
session.commit()

# Jazz
jazz = Genre(name="Jazz", creator=email)
session.add(jazz)
session.commit()

album1 = Album(
    artist="Louis Armstrong",
    title="The Complete Hot Five and Hot Seven Recordings, vol. 1 (1925)",
    description="Early classics from the original jazz master",
    creator=email,
    price="$27.99",
    genre=jazz)
session.add(album1)
session.commit()

album2 = Album(
    artist="Duke Ellington",
    title="Ellington at Newport (1956)",
    description="Legendary live performance that sparked the Duke's comeback",
    creator=email,
    price="$24.99",
    genre=jazz)
session.add(album2)
session.commit()

album3 = Album(
    artist="Miles Davis",
    title="Kind of Blue (1959)",
    description="Arguably the greatest jazz album of all time",
    creator=email,
    price="$21.99",
    genre=jazz)
session.add(album3)
session.commit()

album4 = Album(
    artist="John Coltrane",
    title="Blue Train (1958)",
    description="The first masterpiece by Coltrane",
    creator=email,
    price="$25.99",
    genre=jazz)
session.add(album4)
session.commit()

album5 = Album(
    artist="Ornette Coleman",
    title="The Shape of Jazz to Come (1959)",
    description="The defining document of avant-garde jazz",
    creator=email,
    price="$19.99",
    genre=jazz)
session.add(album5)
session.commit()

album6 = Album(
    artist="Charles Mingus",
    title="Mingus Ah Um (1959)",
    description="Legendary bassist throws down",
    creator=email,
    price="$24.99",
    genre=jazz)
session.add(album6)
session.commit()

album7 = Album(
    artist="John Coltrane",
    title="A Love Supreme (1965)",
    description="Among the most important records ever made in any genre",
    creator=email,
    price="$29.99",
    genre=jazz)
session.add(album7)
session.commit()

album8 = Album(
    artist="Miles Davis",
    title="Bitches Brew (1970)",
    description="The defining word on jazz fusion",
    creator=email,
    price="$41.99",
    genre=jazz)
session.add(album8)
session.commit()


# Hip Hop
hip_hop = Genre(name="Hip Hop", creator=email)
session.add(hip_hop)
session.commit()

album1 = Album(
    artist="Public Enemy",
    title="It Takes a Nation of Millions to Hold Us Back (1988)",
    description="Incendiary classic from NYC crew",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album1)
session.commit()

album2 = Album(
    artist="Beastie Boys",
    title="Paul's Boutique",
    description="A new sound that changed the game",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album2)
session.commit()

album3 = Album(
    artist="N.W.A.",
    title="Straight Outta Compton (1988)",
    description="\'Gangsta\' rap's defining statement",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album3)
session.commit()

album3 = Album(
    artist="Wu-Tang Clan",
    title="Enter the Wu-Tang (36 Chambers) (1993)",
    description="To many, the greatest rap album of all time",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album3)
session.commit()

album4 = Album(
    artist="The Notorious BIG",
    title="Ready to Die (1994)",
    description="East coast classic of hardcore rap from Big-E",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album4)
session.commit()

album5 = Album(
    artist="2Pac",
    title="All Eyez on Me (1996)",
    description="To the west coast what Big-E is to the east",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album5)
session.commit()

album6 = Album(
    artist="Dr Dre",
    title="The Chronic (1992)",
    description="G-Funk defined",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album7)
session.commit()

album7 = Album(
    artist="Outkast",
    title="Stankonia",
    description="A classic of southern hip-hop",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album7)
session.commit()

album8 = Album(
    artist="Kendrick Lamar",
    title="DAMN.",
    description="A contemporary hip-hop masterpiece",
    creator=email,
    price="$21.99",
    genre=hip_hop)
session.add(album8)
session.commit()


# R&B
randb = Genre(name="R&B", creator=email)
session.add(randb)
session.commit()

album1 = Album(
    artist="TLC",
    title="CrazySexyCool (1994)",
    description="The name says it all",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album1)
session.commit()

album2 = Album(
    artist="Boyz II Men",
    title="II (1994)",
    description="90s classic of vocal R&B",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album2)
session.commit()

album3 = Album(
    artist="Mariah Carey",
    title="Music Box (1993)",
    description="Her defining statement",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album3)
session.commit()

album4 = Album(
    artist="Usher",
    title="My Way (1997)",
    description="The R&B loverman par excellence",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album4)
session.commit()

album5 = Album(
    artist="Mary J. Blige",
    title="What's the 411? (1992)",
    description="The queen of hip-hop soul",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album5)
session.commit()

album6 = Album(
    artist="Destiny's Child",
    title="The Writing's on the Wall (1999)",
    description="The Supremes of the 90s",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album6)
session.commit()

album7 = Album(
    artist="Bell Biv Devoe",
    title="Poison (1990)",
    description="Not the hair metal band",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album7)
session.commit()

album8 = Album(
    artist="Blackstreet",
    title="Another Level (1996)",
    description="I like the way you work it...",
    creator=email,
    price="$21.99",
    genre=randb)
session.add(album8)
session.commit()

print("Added genres and albums!")
