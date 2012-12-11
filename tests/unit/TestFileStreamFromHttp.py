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
 
import os
import unittest2
from groupdocs.FileStream import FileStream

class TestFileStreamFromHttp(unittest2.TestCase):

    def setUp(self):
        # TODO mock http response
        response = {} 
        response.closed = False
        self.fs = FileStream.fromHttp(response) 

    @unittest2.skip("TODO")
    def test_size(self):
        expected = 29696L
        self.assertEquals(expected, self.fs.size)

    @unittest2.skip("TODO")
    def test_contentType(self):
        expected = "application/msword"
        self.assertEquals(expected, self.fs.contentType)

    @unittest2.skip("TODO")
    def test_fileName(self):
        expected = "test.doc"
        self.assertEquals(expected, self.fs.fileName)

    @unittest2.skip("TODO")
    def test_inputStream(self):
        expected = True
        self.assertEquals(expected, not self.fs.inputStream.closed)

    
if __name__ == '__main__':
    unittest2.main()
