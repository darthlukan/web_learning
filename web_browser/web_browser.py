import webbrowser

# Basic usage:
# Opens a web browser pointing to url.
webbrowser.open(url)

# Opens a new tab in the web browser
webbrowser.open_new_tab(url)

# Opens a new web browser
webbrowser.open_new(url)

# Advanced usage:
# Open a specific web browser
browser = webbrowser.get('mozilla')
browser.open(url)

# Available browsers:
"""
taken from http://docs.python.org/2/library/webbrowser.html

Type Name	Class Name	Notes
'mozilla'	Mozilla('mozilla')	 
'firefox'	Mozilla('mozilla')	 
'netscape'	Mozilla('netscape')	 
'galeon'	Galeon('galeon')	 
'epiphany'	Galeon('epiphany')	 
'skipstone'	BackgroundBrowser('skipstone')	 
'kfmclient'	Konqueror()	(1)
'konqueror'	Konqueror()	(1)
'kfm'	Konqueror()	(1)
'mosaic'	BackgroundBrowser('mosaic')	 
'opera'	Opera()	 
'grail'	Grail()	 
'links'	GenericBrowser('links')	 
'elinks'	Elinks('elinks')	 
'lynx'	GenericBrowser('lynx')	 
'w3m'	GenericBrowser('w3m')	 
'windows-default'	WindowsDefault	(2)
'macosx'	MacOSX('default')	(3)
'safari'	MacOSX('safari')	(3)
"""
