# -*- coding: cp936 -*-
# coding = utf-8
import urllib
import json

class BaiduMap():
    def __init__(self):
        """
        access key: hYUGnhE5RFFODVyiskq9HXkf
        """
        self.urlbase = "http://api.map.baidu.com/place/v2/search"
        self.parameter = {
            'q':'',
            'region':'',
            'output':'json',
            'scope':1,
            'filter':'',
            'page_size':20,
            'page_num':1,
            'ak':'hYUGnhE5RFFODVyiskq9HXkf',
            }
    def setq(self,q):
        self._setpara('q',q)
    def setregion(self,region):
        self._setpara('region',region)
    def setoutput(self,output):
        self._setpara('output',output)
    def setscope(self,scope,thefilter):
        self._setpara('scope',scope)
        if scope is 2 :
            self._setpara('filter',thefilter)
    def _setpara(self,key,parameter):
        self.parameter[key] = parameter
    def _fetch(self,query=None,json=True):
        data = urllib.urlencode(query)
        url = self.urlbase + '?' + data
        print url
        opener = urllib.FancyURLopener()
        data = opener.open(url).read()
        if json:
            return self._tojson(data)
        else:
            return data
    def _tojson(self,data):
        try:
            js = json.loads(data,'utf-8')
        except:
            js = None
        return js
    def printtest(self):
        self.setq('房子')
        self.setregion('济南')
        
        data = self._fetch(self.parameter)
        length = len(data['results'])
        for i in range(length):
            print data['results'][i]['address']
    
