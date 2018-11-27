# Project 4: Item Catalogue Project
# geraldgsh
## Udacity Full Stack Nanodegree

#### Objective

Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

The homepage displays all current categories along with the latest added items. 

1. Selecting a specific category shows all the items available for that category.

2. Selecting a specific item shows specific information of that item.

3. After logging in, a user has the ability to add, update, or delete item info.

4. The application provides a JSON endpoint, at the very least.


#### Programs used to execute written code;

  1. [Python Version 2.7.13](https://www.python.org/)
  2. [Vagrant Version 1.9.1](https://www.vagrantup.com/)
  3. [VirtualBox Version 5.1.28 ](https://www.virtualbox.org/)
  4. [Git Version 2.14.1](https://git-scm.com/)


#### To run the code;

1. Open a Unix-like command line terminal (e.g. Git Bash on Windows), and navigate to the folder containing this project's files.

2. Start VM using the following command;

        $ vagrant up

3. Login VM using the following command;

        $ vagrant ssh

4. Change directory using the following command;

        $ cd /vagrant


#### Initializing database 

1. Setup Database schema with the following command;

        python database_setup.py

2. Populate database with data using the following command;

        python loaddatabase.py

2. Start web application using the following command;

        python project.py


HMTL was validated using https://validator.w3.org

Python was validated using http://pep8online.com/checkresult# item-catalog
