import re
import urllib2

def get_site_html(url):
    source = urllib2.urlopen(url).read()
    return source
    
if __name__ == '__main__':
    output = get_site_html('http://www.women2.org') 
    h = re.compile('<h2.*>.*</h2>')
    headlines = h.findall(output)
    i = re.compile('title=".*"')
    for headline in headlines: 
       snout = headline.find('Permalink to')
       tail = headline.find('" rel="bookmark"')
       unsufficientheadline = headline[(snout + 13):tail]
       a = unsufficientheadline.replace('&#8217;','\'').replace('&#8220;','"').replace('&#8221','"').replace('&amp;','&')
       print a
