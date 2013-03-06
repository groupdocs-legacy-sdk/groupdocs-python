#!/usr/bin/env python
"""
Copyright 2012 GroupDocs.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *
from groupdocs.FileStream import FileStream
from groupdocs.ApiClient import ApiException

class SharedApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.__basePath = "https://dev-api.groupdocs.com/v2.0"

    @property
    def basePath(self):
        return self.__basePath
    
    @basePath.setter
    def basePath(self, value):
        self.__basePath = value

    
    def Download(self, guid, fileName, **kwargs):
        """Download

        Args:
            guid, str: GUID (required)
            fileName, str: File name (required)
            render, bool: Render (optional)
            
        Returns: stream
        """
        if( guid == None or fileName == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['guid', 'fileName', 'render']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Download" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shared/files/{guid}?filename={fileName}&render={render}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('fileName' in params):
            queryParams['filename'] = self.apiClient.toPathValue(params['fileName'])
        if ('render' in params):
            queryParams['render'] = self.apiClient.toPathValue(params['render'])
        if ('guid' in params):
            replacement = str(self.apiClient.toPathValue(params['guid']))
            resourcePath = resourcePath.replace('{' + 'guid' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        return self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams, FileStream)
        
    def GetXml(self, guid, **kwargs):
        """Get xml

        Args:
            guid, str: GUID (required)
            
        Returns: stream
        """
        if( guid == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['guid']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetXml" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shared/files/{guid}/xml'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('guid' in params):
            replacement = str(self.apiClient.toPathValue(params['guid']))
            resourcePath = resourcePath.replace('{' + 'guid' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        return self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams, FileStream)
        
    def GetPackage(self, path, **kwargs):
        """Get package

        Args:
            path, str: Path (required)
            
        Returns: stream
        """
        if( path == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetPackage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shared/packages/{*path}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        return self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams, FileStream)
        
    


