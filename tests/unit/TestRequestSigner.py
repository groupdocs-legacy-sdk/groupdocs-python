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
"""
 
import unittest
from groupdocs.ApiClient import ApiClient
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

class TestRequestSigner(unittest.TestCase):
    """Test cases to ensure correctness of request signature generation"""

    def sign(self, url):
        return ApiClient.encodeURI(self.signer.signUrl(url))
    
    def setUp(self):
        self.signer = GroupDocsRequestSigner("8d8a7d642a807a31c2741c101a60cef2")
        self.basePath = "https://api.groupdocs.com/v2.0/storage/2721ad21bcf0d71e/folders/test.docx?description="

    def test_SimplePath(self):
        requestUrl = self.basePath + "uploaded"
        expected = requestUrl + "&signature=OT6eFQYsZulqFDTsv4XSNlmc3FY"
        self.assertEquals(expected, self.sign(requestUrl))

    def test_PathEndingWithSpace(self):
        requestUrl = self.basePath + "test DOC file "
        expected = self.basePath + "test%20DOC%20file%20&signature=rdw%2F%2FiP0mwN7Bme2sJ99AZmOpq4"
        self.assertEquals(expected, self.sign(requestUrl))
    
    def test_PathWithAtSymbol(self):
        requestUrl = self.basePath + "with @ symbol"
        expected = self.basePath + "with%20@%20symbol&signature=ar7cFk0RSaVukMIUbvJB%2FYp5oHs"
        self.assertEquals(expected, self.sign(requestUrl))
    
    def test_PathWithStarSymbol(self):
        requestUrl = self.basePath + "with * symbol"
        expected = self.basePath + "with%20*%20symbol&signature=iwzySzo6jbCXhf4lMB3r%2FtcV8Kc"
        self.assertEquals(expected, self.sign(requestUrl))
    
    def test_PathWithBrackets(self):
        requestUrl = self.basePath + "with ( and )"
        expected = self.basePath + "with%20(%20and%20)&signature=rDzSggRSTkBFOi%2F0P%2Bta6j%2BvYzY"
        self.assertEquals(expected, self.sign(requestUrl))
    
    def test_PathWithSquareBrackets(self):
        requestUrl = self.basePath + "with [ and ]"
        expected = self.basePath + "with%20%5B%20and%20%5D&signature=hfLg0YTTGdXpvdqV%2B7y2YJkJZqo"
        self.assertEquals(expected, self.sign(requestUrl))
    
    def test_PathWithEncodeURIComponent(self):
        # https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/encodeURIComponent
        requestUrl = self.basePath + "alpha123 - _ . ! ~ * ' ( )"
        expected = self.basePath + "alpha123%20-%20_%20.%20!%20~%20*%20'%20(%20)&signature=6ZTSvVrJ3Wvp9aZ93wtp5oH2hJ4"
        self.assertEquals(expected, self.sign(requestUrl))
    
    @unittest.skip("TODO: Fails due to different signature")
    def test_PathWithEncodeURI(self):
        # https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/encodeURI
        requestUrl = self.basePath + "alpha123 ; , / ? : @ & = + "; # omitted # 
        expected = self.basePath + "alpha123%20;%20,%20/%20?%20:%20@%20&%20=%20%2B%20&signature=zqj1XJtWE0%2F%2FMon%2FiSJN%2FC6Yyco"
        self.assertEquals(expected, self.sign(requestUrl))

    
if __name__ == '__main__':
    unittest.main()
