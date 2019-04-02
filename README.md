## Item Catalog

## Use
_Item Catalog_ is a RESTful web application written in Python that displays information about musical recordings in various genres. Users must be logged in to browse or alter the database. Once logged in, albums and even entire musical genres can be added or deleted. In this way the application demonstrates proficiency with OAuth 2.0 and also with CRUD operations on a database. Additionally, JSON endpoints are provided for data serialization--please see below for links.

SQLAlchemy was used to construct the database, and the Flask web development framework was employed to write template pages that the allow the user to interact with the database.

## Running the application

_Item Catalog_ runs on a virtual Ubuntu box. To get started please proceed as follows:

* You will need a shell window. If you're on a Mac this is the command line utility. If on Windows 7 or later you will need to download [Git BASH](https://gitforwindows.org/).
* In the shell you will run the Ubuntu box using [Vagrant](https://www.vagrantup.com/) in conjunction with [Virtual Box 5.2](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2). **NOTE**: You cannot yet use VirtualBox 6 with Vagrant.
* Assuming you have installed those two components, download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) or fork and clone the Github [repository](https://github.com/udacity/fullstack-nanodegree-vm).

## Prepping the environment
Once you `vagrant up` and then `vagrant ssh` into your virtual machine, type `cd /vagrant` to access your shared files. Clone this repo from that location, then run shell configuration file by typing `sudo ./pg_config.sh`, which will ensure that all necessary dependencies are loaded on to your virtual machine.

Assuming you have cloned this repo you may simply type `python catalog.py` to initiate the server, then open your browser and go to `http://localhost:5000`. You will then be asked to log in with google. You cannot use the application without logging in, and users are automatically signed out after 15 minutes of inactivity. Please be patient as sometimes the various pages will take a short while to load.

If you want to start fresh with a new database, delete the `musiccatalog.db` and `catalog_setup.pyc` files. Then type `python catalog_setup.py` to re-create the database. If you want to load the starter data, type `python catalog.py`.

Enjoy the application and rock on!

## JSON endpoints
* http://localhost:5000/genre/JSON - lists genre names and ID numbers
* http://localhost:5000/genre/1/album/JSON - shows all albums in genre "1" Indie Rock (substitute "1 with one of 2 - 6 to see the albums in other genres per the above link)
* http://localhost:5000/genre/1/album/1/JSON - shows data for individual album "1" (the second "1" can be substituted with an album number from 2 to 48, or more if more are added to the default database listing)
