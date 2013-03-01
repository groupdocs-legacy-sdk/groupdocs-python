.. GroupDocs Python SDK documentation master file, created by
   sphinx-quickstart on Tue Nov 27 21:40:40 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GroupDocs Python SDK's documentation!
################################################

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


Contents:
*********

.. toctree::
   :maxdepth: 2
   
   groupdocs


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
