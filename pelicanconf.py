#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hugo'
SITENAME = 'Hugo Alvarado'
SITEURL = 'https://hugoalvarado.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'pelican-hyde'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('email', 'hugo102@gmail.com'),
		 ('twitter', 'https://twitter.com/_hugoalvarado'),
		  ('github', 'https://github.com/hugoalvarado'),
          ('linkedin', 'https://cr.linkedin.com/in/hugoalvarado'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

BIO = "Hello! I'm Hugo Alvarado, working as Software Engineer, living in a cave."
PROFILE_IMAGE = "avatar.jpg"
