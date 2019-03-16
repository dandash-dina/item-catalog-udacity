# Item Catalog

## Table of Contents

* [Project Description](#describe what this project about)
* [Project Content](#contents)
* [Requirements](#needed to run the project)
* [Setup](#run the project)

## Project Description
This project develops an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items
This application is for Car Free Marketing, which each category is an agency of car and can add their cars to sell as items in the category.

## Project Content
Within the download you'll find the following files:

item_catalog.zip
|
 +-- project.py
 |    
 +-- lotsofmenus.py
 |    
 +-- database_setup.py
 |    
 +-- fb_client_secrets.json
 |    
 +-- client_secrets.json
 |    
 +-- README.md
 |    
 +-- templates
 |    
 +-- static

│   
└──


## Requirements:
VirtualBox

Vagrant

Python3

Bash terminal(for windows machine)


### Installation:
Install [Python3](https://www.python.org/downloads/)
,[VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
and [Vagrant](https://www.vagrantup.com/downloads.html)


*Clone or download the Vagrant VM configuration file from [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)



*Clone or download this repository into the vagrant/ catalog




### Setup
To run this project:

1- Open terminal and go to the folder where you saved the fullstack repository then : cd vagrant.

2- Launch Vagrant to set up the virtual machine and then log into the virtual machine.: vagrant up vagrant ssh
move to root of repository in vagrant : cd /vagrant
move to sub-directory : cd /catalog


3- Set up the database : python database_setup.py

4- Set data for database : python lotsofmenus.py

5- Finally run python project.py .

6- Access and test your application by visiting http://localhost:5000 locally



### APIs
| URI                                               | JSON Information                 |
|---------------------------------------------------|----------------------------------|
| /catalog/JSON'                                    | Listing of Catalog  |
| /catalog/<int:catalog_id>/menu/JSON               | Listing  all items in Catalog|
| /catalog/<int:catalog_id>/menu/<int:menu_id>/JSON | To view Menu Information |
