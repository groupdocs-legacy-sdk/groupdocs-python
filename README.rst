GroupDocs Python SDK |Build Status|_
####################################

Latest SDK version 1.7.0.

Requirements
************

-  SDK requires Python 2.6 (or later). If you need Python 3 version of
   SDK please go to `groupdocs-python3`_

Installation
************

You can use the `Pip`_ to download and install SDK. GroupDocs SDK is now
in `PyPi`_.

Usage Example
*************

::

    apiClient = ApiClient(GroupDocsRequestSigner(privateKey))
    api = AntApi(apiClient)
    response = api.ListAnnotations(userId, fileId)

`Sign, Manage, Annotate, Assemble, Compare and Convert Documents with GroupDocs`_
*********************************************************************************

1. `Sign documents online with GroupDocs Signature`_
2. `PDF, Word and Image Annotation with GroupDocs Annotation`_
3. `Online DOC, DOCX, PPT Document Comparison with GroupDocs
   Comparison`_
4. `Online Document Management with GroupDocs Dashboard`_
5. `Doc to PDF, Doc to Docx, PPT to PDF, and other Document Conversions
   with GroupDocs Viewer`_
6. `Online Document Automation with GroupDocs Assembly`_

License
*******

::

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

.. _Build Status: http://travis-ci.org/groupdocs/groupdocs-python
.. _groupdocs-python3: https://github.com/groupdocs/groupdocs-python3
.. _Pip: http://www.pip-installer.org/
.. _PyPi: http://pypi.python.org/pypi/groupdocs-python
.. _Sign, Manage, Annotate, Assemble, Compare and Convert Documents with GroupDocs: http://groupdocs.com
.. _Sign documents online with GroupDocs Signature: http://groupdocs.com/apps/signature
.. _PDF, Word and Image Annotation with GroupDocs Annotation: http://groupdocs.com/apps/annotation
.. _Online DOC, DOCX, PPT Document Comparison with GroupDocs Comparison: http://groupdocs.com/apps/comparison
.. _Online Document Management with GroupDocs Dashboard: http://groupdocs.com/apps/dashboard
.. _Doc to PDF, Doc to Docx, PPT to PDF, and other Document Conversions with GroupDocs Viewer: http://groupdocs.com/apps/viewer
.. _Online Document Automation with GroupDocs Assembly: http://groupdocs.com/apps/assembly

.. |Build Status| image:: https://secure.travis-ci.org/groupdocs/groupdocs-python.png