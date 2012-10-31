#!/usr/bin/env python
"""
WordAPI.py
Copyright 2012 Wordnik, Inc.

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


class ComparisonApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def DownloadResult(self, userId, resultFileId, format, **kwargs):
        """Download comparison result file

        Args:
            userId, str: User GUID (required)
            resultFileId, str: Comparison result file GUID (required)
            format, str: Comparison result file format (optional)
            
        Returns: str
        """

        allParams = ['userId', 'resultFileId', 'format']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DownloadResult" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/download?resultFileId={resultFileId}&amp;format={format}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('resultFileId' in params):
            replacement = str(self.apiClient.toPathValue(params['resultFileId']))
            resourcePath = resourcePath.replace('{' + 'resultFileId' + '}',
                                                replacement)
        if ('format' in params):
            replacement = str(self.apiClient.toPathValue(params['format']))
            resourcePath = resourcePath.replace('{' + 'format' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
    def Compare(self, userId, sourceFileId, targetFileId, **kwargs):
        """Compare

        Args:
            userId, str: User GUID (required)
            sourceFileId, str: Source File GUID (required)
            targetFileId, str: Target File GUID (required)
            
        Returns: CompareResponse
        """

        allParams = ['userId', 'sourceFileId', 'targetFileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Compare" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/compare?source={sourceFileId}&amp;target={targetFileId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('sourceFileId' in params):
            replacement = str(self.apiClient.toPathValue(params['sourceFileId']))
            resourcePath = resourcePath.replace('{' + 'sourceFileId' + '}',
                                                replacement)
        if ('targetFileId' in params):
            replacement = str(self.apiClient.toPathValue(params['targetFileId']))
            resourcePath = resourcePath.replace('{' + 'targetFileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CompareResponse')
        return responseObject
        
        
    def GetChanges(self, userId, resultFileId, **kwargs):
        """Get changes

        Args:
            userId, str: User GUID (required)
            resultFileId, str: Comparison result file GUID (required)
            
        Returns: ChangesResponse
        """

        allParams = ['userId', 'resultFileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetChanges" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/changes?resultFileId={resultFileId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('resultFileId' in params):
            replacement = str(self.apiClient.toPathValue(params['resultFileId']))
            resourcePath = resourcePath.replace('{' + 'resultFileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ChangesResponse')
        return responseObject
        
        
    def UpdateChanges(self, userId, resultFileId, body, **kwargs):
        """Update changes

        Args:
            userId, str: User GUID (required)
            resultFileId, str: Comparison result file GUID (required)
            body, List[ChangeInfo]: Comparison changes to update (accept or reject) (required)
            
        Returns: ChangesResponse
        """

        allParams = ['userId', 'resultFileId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method UpdateChanges" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/changes?resultFileId={resultFileId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('resultFileId' in params):
            replacement = str(self.apiClient.toPathValue(params['resultFileId']))
            resourcePath = resourcePath.replace('{' + 'resultFileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ChangesResponse')
        return responseObject
        
        
    def GetDocumentDetails(self, userId, guid, **kwargs):
        """Get document details

        Args:
            userId, str: User GUID (required)
            guid, str: Document GUID (required)
            
        Returns: DocumentDetailsResponse
        """

        allParams = ['userId', 'guid']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetDocumentDetails" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/document?guid={guid}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('guid' in params):
            replacement = str(self.apiClient.toPathValue(params['guid']))
            resourcePath = resourcePath.replace('{' + 'guid' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DocumentDetailsResponse')
        return responseObject
        
        
    


