'''
Created on 21.11.2017

@author: Lars Feldeisen
'''


import sys
import webbrowser

__SEARCH_DOMAIN__ = "https://google.com/search?q="

def main():
    search_string = ' '.join(sys.argv[1:])
    
    if (sys.version_info > (3, 0)):
        import urllib.parse
        search_string = urllib.parse.quote(search_string)
    else:
        import urllib
        search_string = urllib.quote(search_string, safe='')
    
    webbrowser.open(__SEARCH_DOMAIN__ + search_string)
    
    
