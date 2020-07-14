config.source('qutewal.py')


c.tabs.position = "left"
c.tabs.width = "10%"
c.colors.hints.fg = "#FFF"

# password manager
config.bind(',p', 'spawn --userscript qute-pass --dmenu-invocation dmenu')

# Tabs and statusbar toggling
config.bind('xx', 'config-cycle tabs.show always switching')
config.bind('xz', 'config-cycle statusbar.hide')
config.bind('xc', 'config-cycle statusbar.hide ;; config-cycle tabs.show always switching')


# Umpv
config.bind(',m', 'spawn umpv {url}')
config.bind(',M', 'hint links spawn umpv {hint-url}')
config.bind(';M', 'hint --rapid links spawn umpv {hint-url}')

c.url.searchengines = {
   "DEFAULT":'https://duckduckgo.com/?q={}',
   'ap': 'https://archlinux.org/packages/?q={}',
   'aur': 'https://aur.archlinux.org/packages.php?K={}',
   'ar': 'https://wiki.archlinux.org/?search={}',
   "c": 'https://boards.4chan.org/{}/',
   "r": 'https://www.reddit.com/r/{}',
   "l": 'https://www.liveleak.com/browse?q={}',
   "w": 'https://en.wikipedia.org/wiki/={}',
   "y": 'https://www.youtube.com/results?search_query={}',
   "g": "https://www.github.com/{}"
}
