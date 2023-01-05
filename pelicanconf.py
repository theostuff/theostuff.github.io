from pathlib import Path

AUTHOR = 'TheoStuff'
SITENAME = 'TheoStuff'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes
p = Path(__file__).parent
THEME = p / 'themes/pelican-alchemy/alchemy'