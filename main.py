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
#
import webapp2
import random

def getRandomFortune():
	
	fortunes = ["The world is yours", "You will be a great coder!","You will be in control of your own Fortune"]
	index = random.randint(0,2)

	return fortunes[index]



class MainHandler(webapp2.RequestHandler):
    def get(self):
    	header = "<h1>Frotune Cookie</h1>"

    	fortune = "<strong>" + getRandomFortune() + "</strong>"
    	fortune_sent = "Your Fortune: " + fortune
    	fortune_paragraph = "<p>" + fortune_sent + "</p>"
    	

    	lucky_number = "<strong>" + str(random.randrange(100)) + "</strong>"
    	number_sent = '<p>Your lucky number: ' + lucky_number + '</p>' 
        
        cookie_again_button = "<a href='.'><button>Another cookie please</button></a>"

        content = header + fortune_paragraph + number_sent + cookie_again_button



        self.response.write(content)
        


        self.response.write('<a href="localhost:8080/login"><button>Login</button></a>')


class LoginHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Love is the best')

routes = [
	('/', MainHandler),
	('/login', LoginHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)

