import os.path

import cherrypy

#this file serves as the hub for all other pages; the home page,
#search page, upload page, etc

# "pages" refers to the folder containing all the different files with
# code for the various pages

#from pages.search import SearchPage
#from pages.list import ListingsPage
#etc

class HomePage:

    @cherrypy.expose
    def index(self):
        return """ <h1> Welcome to Wecycle </h1>"""
    

if __name__ == '__main__':
    cherrypy.quickstart(HomePage())
