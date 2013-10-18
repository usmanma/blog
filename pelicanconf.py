#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


SITENAME = 'Particult'
# SITESUBTITLE = 'Random musings'
SITEURL = 'http://localhost:8000'
AUTHOR = 'Usman Malik'

DEFAULT_CATEGORY = 'writings'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 1

DELETE_OUTPUT_DIRECTORY = True

DIRECT_TEMPLATES = (
    'index',
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATH = 'pelican_plugins'
PLUGINS = ['assets',]

SUMMARY_MAX_LENGTH = None

THEME = 'themes/asterias'

TIMEZONE = 'Europe/London'
TYPOGRIFY = True

# WITH_FUTURE_DATES = False

PYGMENTS_RST_OPTIONS = {
    'linenos': 'table',
    # 'nobackground': True,
}

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ARTICLE_URL = '{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

# ARTICLE_LANG_URL = '{lang}/' + ARTICLE_URL
# ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'

PAGE_URL = 'page/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

# PAGE_LANG_URL = PAGE_URL
# PAGE_LANG_SAVE_AS = PAGE_SAVE_AS

# CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = False # CATEGORY_URL + 'index.html'

# TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = False # TAG_URL + 'index.html'

# TAGS_URL = 'tags/'
TAGS_SAVE_AS = False # TAGS_URL + 'index.html'

# AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = False # AUTHOR_URL + 'index.html'

# AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = False # AUTHORS_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%b}/{date:%d}/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}', '{base_name}/page/{number}/index.html'),
)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
# )

# Social widget
# SOCIAL = (
#     ('You can add links in your config file', '#'),
#     ('Another social link', '#'),
# )
