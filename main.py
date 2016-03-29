#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# self.request.path attribute and string concatenation

import webapp2
import cgi
from google.appengine.api import users
import os
import logging
import jinja2
from os import listdir
from os.path import isfile, join
from google.appengine.api import mail



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HomeHandler(webapp2.RequestHandler):
    def get(self): 
        try:
            path = self.request.path
            template = JINJA_ENVIRONMENT.get_template('templates/%s' %path)
            namelist = path.split('/')
            for item in namelist:
                name = item.split('.')
                nametitle = name[0].title()
                nameinnav = name[0].upper()
            if nametitle =="Guestbook":   
                self.response.write(template.render({'title': nametitle,'header': nametitle, 'caption1':'Home', 'caption2': nameinnav, 'caption3': 'Projects', 'caption': 'Photos'}))
            elif nametitle == "Projects":
                self.response.write(template.render({'title': nametitle,'header': nametitle, 'caption1':'Home', 'caption2': 'Guestbook', 'caption3': nameinnav, 'caption': 'Photos'}))
            else:
                self.response.write(template.render({'title': "Home",'header': 'Home', 'caption1': 'HOME', 'caption2': 'Guestbook', 'caption3': 'Projects', 'caption': 'Photos'})) 
            logging.info("This is a get")
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/home.html')
            self.response.write(template.render({'title': "Home",'header': 'Home', 'caption1': 'HOME', 'caption2': 'Guestbook', 'caption3': 'Projects', 'caption': 'Photos'})) 
            logging.info("This is a get")

class LoggingHandler(webapp2.RequestHandler):
    def get(self):  
    	template = JINJA_ENVIRONMENT.get_template('templates/logging.html')
    	self.response.write(template.render({'title': 'Photos','header': 'Photos', 'caption1': 'Home', 'caption2': 'Guestbook', 'caption3': 'Projects', 'caption': 'PHOTOS'})) 
        logging.info("This is a get")
       

class GuestbookHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/attract.html')
        self.response.write(template.render({'title': 'GUESTBOOK','header': 'Guestbook', 'caption1': 'Home', 'caption2': 'GUESTBOOK', 'caption3': 'Projects', 'caption': 'Photos'})) 


    def post(self):
        text = cgi.escape(self.request.get('content'))
        template = JINJA_ENVIRONMENT.get_template('templates/guestbook.html')
        self.response.write(template.render({'title': 'Guest Book','header': 'Guestbook', 'caption1': 'Home', 'caption2': 'Guestbook', 'caption3': 'Projects', 'caption': 'Photos', 'msg':"Thank you for your comments!", 'msg2':" You wrote:" , 'msg3':text })) 


class ProjectsHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/projects.html')
        self.response.write(template.render({'title': 'Projects','header': 'Projects', 'caption1': 'Home', 'caption2': 'Guestbook', 'caption3': 'PROJECTS', 'caption': 'Photos'})) 

    def post(self):
        user_address = self.request.get('email')
        sender_address = "jasmitk@gmail.com"
        subject = "TEST"
        body = self.request.get('message')
    

        mail.send_mail(sender_address, user_address, subject, body)

        template = JINJA_ENVIRONMENT.get_template('templates/emailconfirm.html')
        self.response.write(template.render({'title': 'Projects','header': 'Projects', 'caption1': 'Home', 'caption2': 'Guestbook', 'caption3': 'Projects', 'caption': 'Photos', 'msg':"Thank you for email!", 'msg2':" An email confirmation is on its way. I will get back you soon!"  })) 



app = webapp2.WSGIApplication([  
    ('/home.html', HomeHandler),
    ('/projects.html', ProjectsHandler),
    ('/logging.html', LoggingHandler),
    ('/attract.html', GuestbookHandler),
    ('/.*', HomeHandler)


   
], debug=True)
