#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ror6ax'
SITENAME = u'https://ntuukpi.github.io/asu/'
SITEURL = 'https://ntuukpi.github.io/asu/'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

TIMEZONE = 'Europe/Paris'
THEME = 'Flex'
DEFAULT_LANG = u'ua'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PAGE_PATHS = ['pages']
# Blogroll
LINKS = (('kpi.ua', 'http://kpi.ua'),)
STATIC_PATHS = ['images', 'materials']
# Social widget

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'National Technical University of Ukraine',
    },
}
