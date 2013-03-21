# coding: utf-8
from django.shortcuts import render_to_response
import requests
from bs4 import BeautifulSoup

def index(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
    else:
        q = ""
    google_search = 'https://www.google.com/search?hl=zh-CN&q=site:huaban.com+' + q
    
    # dict
    result = {}
    
    # requests
    r = requests.get(google_search)
    
    # beautifulsoup
    html_doc = r.text
    soup = BeautifulSoup(html_doc)
    h3 = soup.find_all("h3")
    for a in h3:
        result[a.find('a').get('href')] = a.find('a').get_text()

    # template
    return render_to_response('huaban/index.html',
                              {
                                  'result':result,
                                  'google_search':google_search,
                                  'q':q,
                                  'active':'index',
                              })

def about(request):
    return render_to_response('huaban/about.html',
                            {
                                 'active':'about'
                            })