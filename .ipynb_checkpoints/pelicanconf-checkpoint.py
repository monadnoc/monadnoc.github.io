#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jordan Nelson'
SITENAME = 'JNN Personal Site'
SITEURL = 'itsnotyou-its.me'

# Categories
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

# Pages
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'
STATIC_PATHS = ['images']
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Will change this to 10 when publishing; 3 is easier to do theme dev with
DEFAULT_PAGINATION = 4

# Period Archive formats
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'

# URL settings -- leads to clean slug urls instead of having .html after everything
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Theme Settings
THEME = 'themes/brutalist'
## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'site-cover.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Personal website for Jordan Nelson'
## path to favicon
FAVICON = 'favi.png'
## path to logo for nav menu (optional)
#LOGO = 'pelly.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Jordan'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@nerrlerryday'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
# ATTRIBUTION = True
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [('tags', '/tags')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
#STRAVA = 'https://www.strava.com/athletes/27234301'
TWITTER = 'https://twitter.com/nerrlyerrday'
INSTAGRAM = 'https://instagram.com/monadknock'
GITHUB = 'https://github.com/monadnoc'
#TELEGRAM = 'https://t.me/mcman_s'
#GOODREADS = 'https://www.goodreads.com/user/show/48849158-matthew-mcmanus'
#FOURSQUARE = 'https://foursquare.com/mcman_s'
#UNTAPPD = 'https://untappd.com/user/mcman_s'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
DISQUS_SITENAME = 'jordannn'
## Gravatar
GRAVATAR = 'https://www.gravatar.com/avatar/b250ebf2d0ef095eb8c1dc253513dbc2'


# PLUGINS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'category_order', 'w3c_validate', 'optimize_images', 'gzip_cache']

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}

## Github URL for fork ribbon
## Only used on theme site, not personal blog
#GITHUB_URL = 'https://github.com/mamcmanus/brutalistpelican'
#GITHUB_POSITION = 'left'