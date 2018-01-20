import os.path

import cherrypy

#this file serves as the hub for all other pages; the home page,
#search page, upload page, etc

# "pages" refers to the folder containing all the different files with
# code for the various pages

#from pages.home import HomePage
#from pages.search import SearchPage
#etc

if __name__ == '__main__':
    cherrypy.quickstart(HomePage())
