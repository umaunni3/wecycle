import random
import string
import cherrypy
import sys

from storage import *

class LocationForm:
    def __init__(self, id_num):
        self.name, self.imgUrl, self.address, self.wk_hrs, self.sat_hrs, self.sun_hrs, self.tag1, self.tag2, self.tag3, self.info, self.website = readEntry(int(id_num))
   
    @cherrypy.expose
    def index(self):
        return ''' 
        <html>
        <head>
        <title>%s</title>
        </head>
        <body>
        <h1>%s</h1>
        '''%(self.name, self.name) + '''
        <img src="%s">'''%(self.imgUrl) + '''
        <h2>Location</h2>
        <p>%s</p>
        '''%(self.address) + '''
        <h2>Weekday Hours</h2>
        <p>%s</p>
        <h2>Saturday Hours</h2>
        <p>%s</p>
        <h2>Sunday Hours</h2>
        <p>%s</p>
        '''%(self.wk_hrs, self.sat_hrs, self.sun_hrs) + '''
        <h2>Items they accept</h2>
        <ul>
            <li>%s</li>
            <li>%s</li>
            <li>%s</li>
        </ul>
        '''%(self.tag1, self.tag2, self.tag3) + '''
        <h2>Additional information</h2>
        <p>%s</p>
        '''%(self.info) + '''
        <a href="%s">Website</a>
        '''%(self.website)

newEntry(["memes r us","https://www.maketecheasier.com/assets/uploads/2013/12/vim-shortcut-cheatsheet-featured.jpg", "1200 Pennsylvania Avenue, Washington D.C., USA", "6 AM - 9 PM", "4 AM - 2:00 PM", "6 AM - 6 PM", "glass", "polyurethrene", "iPod nanos", "meme all day erry day", "https://www.cs61a.org"])

if __name__ == "__main__":
    cherrypy.quickstart(LocationForm(1))
