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


class StorageApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.__basePath = "https://api.groupdocs.com/v2.0"

    @property
    def basePath(self):
        return self.__basePath
    
    @basePath.setter
    def basePath(self, value):
        self.__basePath = value

    
    def GetStorageInfo(self, userId, **kwargs):
        """Get storage info

        Args:
            userId, str: User GUID (required)
            
        Returns: StorageInfoResponse
        """

        allParams = ['userId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetStorageInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'StorageInfoResponse')
        return responseObject
        
        
    def ListEntities(self, userId, path, pageIndex, pageSize, orderBy, orderAsc, filter, fileTypes, extended, **kwargs):
        """List entities

        Args:
            userId, str: User GUID (required)
            path, str: Path (optional)
            pageIndex, int: Page Index (optional)
            pageSize, int: Page Size (optional)
            orderBy, str: Order By (optional)
            orderAsc, bool: Order Asc (optional)
            filter, str: Filter (optional)
            fileTypes, str: File Types (optional)
            extended, bool: Indicates whether an extended information should be returned (optional)
            
        Returns: ListEntitiesResponse
        """

        allParams = ['userId', 'path', 'pageIndex', 'pageSize', 'orderBy', 'orderAsc', 'filter', 'fileTypes', 'extended']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ListEntities" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/folders/{*path}?page={pageIndex}&amp;count={pageSize}&amp;order_by={orderBy}&amp;order_asc={orderAsc}&amp;filter={filter}&amp;file_types={fileTypes}&amp;extended={extended}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        if ('pageIndex' in params):
            replacement = str(self.apiClient.toPathValue(params['pageIndex']))
            resourcePath = resourcePath.replace('{' + 'pageIndex' + '}',
                                                replacement)
        if ('pageSize' in params):
            replacement = str(self.apiClient.toPathValue(params['pageSize']))
            resourcePath = resourcePath.replace('{' + 'pageSize' + '}',
                                                replacement)
        if ('orderBy' in params):
            replacement = str(self.apiClient.toPathValue(params['orderBy']))
            resourcePath = resourcePath.replace('{' + 'orderBy' + '}',
                                                replacement)
        if ('orderAsc' in params):
            replacement = str(self.apiClient.toPathValue(params['orderAsc']))
            resourcePath = resourcePath.replace('{' + 'orderAsc' + '}',
                                                replacement)
        if ('filter' in params):
            replacement = str(self.apiClient.toPathValue(params['filter']))
            resourcePath = resourcePath.replace('{' + 'filter' + '}',
                                                replacement)
        if ('fileTypes' in params):
            replacement = str(self.apiClient.toPathValue(params['fileTypes']))
            resourcePath = resourcePath.replace('{' + 'fileTypes' + '}',
                                                replacement)
        if ('extended' in params):
            replacement = str(self.apiClient.toPathValue(params['extended']))
            resourcePath = resourcePath.replace('{' + 'extended' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ListEntitiesResponse')
        return responseObject
        
        
    def GetFile(self, userId, fileId, **kwargs):
        """Get file

        Args:
            userId, str: User GUID (required)
            fileId, str: File GUID (required)
            
        Returns: str
        """

        allParams = ['userId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/files/{fileId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
    def GetSharedFile(self, userEmail, filePath, **kwargs):
        """Get shared file

        Args:
            userEmail, str: User Email (required)
            filePath, str: File path (required)
            
        Returns: str
        """

        allParams = ['userEmail', 'filePath']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetSharedFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/shared/{userEmail}/{*filePath}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userEmail' in params):
            replacement = str(self.apiClient.toPathValue(params['userEmail']))
            resourcePath = resourcePath.replace('{' + 'userEmail' + '}',
                                                replacement)
        if ('filePath' in params):
            replacement = str(self.apiClient.toPathValue(params['filePath']))
            resourcePath = resourcePath.replace('{' + 'filePath' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
    def Upload(self, userId, path, description, body, **kwargs):
        """Upload

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            description, str: Description (optional)
            body, stream: Stream (required)
            
        Returns: UploadResponse
        """

        allParams = ['userId', 'path', 'description', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Upload" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/folders/{*path}?description={description}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        if ('description' in params):
            replacement = str(self.apiClient.toPathValue(params['description']))
            resourcePath = resourcePath.replace('{' + 'description' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UploadResponse')
        return responseObject
        
        
    def UploadWeb(self, userId, url, **kwargs):
        """Upload Web

        Args:
            userId, str: User GUID (required)
            url, str: Url (required)
            
        Returns: UploadResponse
        """

        allParams = ['userId', 'url']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method UploadWeb" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/urls?url={url}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('url' in params):
            replacement = str(self.apiClient.toPathValue(params['url']))
            resourcePath = resourcePath.replace('{' + 'url' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UploadResponse')
        return responseObject
        
        
    def UploadGoogle(self, userId, path, fileId, **kwargs):
        """Upload Google

        Args:
            userId, str: User GUID (required)
            path, str: File path (required)
            fileId, str: File unique identifier (optional)
            
        Returns: UploadResponse
        """

        allParams = ['userId', 'path', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method UploadGoogle" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/google/files/{*path}?file_id={fileId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UploadResponse')
        return responseObject
        
        
    def Delete(self, userId, fileId, **kwargs):
        """Delete

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            
        Returns: DeleteResponse
        """

        allParams = ['userId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/files/{fileId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteResponse')
        return responseObject
        
        
    def DeleteFromFolder(self, userId, path, **kwargs):
        """Delete from folder

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            
        Returns: DeleteResponse
        """

        allParams = ['userId', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteFromFolder" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/folders/{*path}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteResponse')
        return responseObject
        
        
    def MoveFile(self, userId, path, mode, **kwargs):
        """Move file

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            mode, str: Mode (optional)
            Groupdocs-Move, str: File ID (move) (optional)
            Groupdocs-Copy, str: File ID (copy) (optional)
            
        Returns: FileMoveResponse
        """

        allParams = ['userId', 'path', 'mode', 'Groupdocs-Move', 'Groupdocs-Copy']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method MoveFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/files/{*path}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('Groupdocs-Move' in params):
            headerParams['Groupdocs-Move'] = params['Groupdocs-Move']
        if ('Groupdocs-Copy' in params):
            headerParams['Groupdocs-Copy'] = params['Groupdocs-Copy']
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        if ('mode' in params):
            replacement = str(self.apiClient.toPathValue(params['mode']))
            resourcePath = resourcePath.replace('{' + 'mode' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileMoveResponse')
        return responseObject
        
        
    def MoveFolder(self, userId, path, mode, **kwargs):
        """Move folder

        Args:
            userId, str: User GUID (required)
            path, str: Destination Path (required)
            mode, str: Mode (optional)
            Groupdocs-Copy, str: Source path (copy) (optional)
            Groupdocs-Move, str: Source path (move) (optional)
            
        Returns: FolderMoveResponse
        """

        allParams = ['userId', 'path', 'mode', 'Groupdocs-Copy', 'Groupdocs-Move']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method MoveFolder" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/folders/{*path}?override_mode={mode}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('Groupdocs-Copy' in params):
            headerParams['Groupdocs-Copy'] = params['Groupdocs-Copy']
        if ('Groupdocs-Move' in params):
            headerParams['Groupdocs-Move'] = params['Groupdocs-Move']
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        if ('mode' in params):
            replacement = str(self.apiClient.toPathValue(params['mode']))
            resourcePath = resourcePath.replace('{' + 'mode' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FolderMoveResponse')
        return responseObject
        
        
    def Create(self, userId, path, **kwargs):
        """Create

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            
        Returns: CreateFolderResponse
        """

        allParams = ['userId', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Create" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/paths/{*path}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CreateFolderResponse')
        return responseObject
        
        
    def Compress(self, userId, fileId, archiveType, **kwargs):
        """Compress

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            archiveType, str: Archive type (optional)
            
        Returns: CompressResponse
        """

        allParams = ['userId', 'fileId', 'archiveType']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Compress" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/files/{fileId}/archive/{archiveType}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        if ('archiveType' in params):
            replacement = str(self.apiClient.toPathValue(params['archiveType']))
            resourcePath = resourcePath.replace('{' + 'archiveType' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CompressResponse')
        return responseObject
        
        
    def CreatePackage(self, userId, packageName, storeRelativePath, **kwargs):
        """Create Package

        Args:
            userId, str: User GUID (required)
            packageName, str: Package Name (required)
            storeRelativePath, bool: Store files using relative paths (optional)
            body, List[str]: Paths (optional)
            
        Returns: CreatePackageResponse
        """

        allParams = ['userId', 'packageName', 'storeRelativePath', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method CreatePackage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/packages/{packageName}?storeRelativePath={storeRelativePath}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('packageName' in params):
            replacement = str(self.apiClient.toPathValue(params['packageName']))
            resourcePath = resourcePath.replace('{' + 'packageName' + '}',
                                                replacement)
        if ('storeRelativePath' in params):
            replacement = str(self.apiClient.toPathValue(params['storeRelativePath']))
            resourcePath = resourcePath.replace('{' + 'storeRelativePath' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CreatePackageResponse')
        return responseObject
        
        
    def MoveToTrash(self, userId, path, **kwargs):
        """Move to trash

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            
        Returns: FolderMoveResponse
        """

        allParams = ['userId', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method MoveToTrash" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/trash/{*path}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FolderMoveResponse')
        return responseObject
        
        
    def RestoreFromTrash(self, userId, path, **kwargs):
        """Restore from trash

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            
        Returns: DeleteResponse
        """

        allParams = ['userId', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method RestoreFromTrash" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/storage/{userId}/trash/{*path}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('path' in params):
            replacement = str(self.apiClient.toPathValue(params['path']))
            resourcePath = resourcePath.replace('{' + 'path' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteResponse')
        return responseObject
        
        
    


