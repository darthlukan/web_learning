import urllib2

'''
    To download a file:
    provide the remote filename (url)
    provide the (new) local location and name of the file you'd like to save as.
'''
def get_file(remoteFileName, saveFileNameLoc):
    
    urllib2.urlopen(remoteFileName, saveFileNameLoc)
    
'''
    Simple URL open.
'''
def open_url(url):
    
    urllib2.urlopen(url)
    
'''
    Get the response from opening the url.
    
    Displays some added info available to the response object.
'''
def get_responses(url):
    # Create our response object
    response = urllib2.urlopen(url)
    # Get the url from our object
    response_url = response.geturl()
    # Get the headers from our object
    response_headers = response.info()
    # This object is iterable using obj.read() and obj.readlines()
    response_data = response.read()