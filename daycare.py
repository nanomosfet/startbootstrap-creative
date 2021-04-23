# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os
import time
import json
import xml.etree.ElementTree as ET
from google.appengine.api.files.file import listdir as ls

from google.appengine.api import mail

template_dir = os.path.join(os.path.dirname(__file__), "pages")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                            autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class mainpageHandler(Handler):
    def get(self):
        self.render('index.html')

class show_documents(Handler):
    def get(self):
        files = os.listdir('./docs')
        self.render('show_docs.html', files = files)





app = webapp2.WSGIApplication([
    ('/', mainpageHandler),
    ('/documents', show_documents),

], debug=True)
