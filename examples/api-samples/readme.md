###Installation instruction

	1) Clone Git repo
	
	2) cd examples/api-samples
	
	3) Create a Virtualenv http://pypi.python.org/pypi/virtualenv:
	virtualenv venv --distribute

	3.1* ) To activate local environment:
	source venv/bin/activate

	4) To install all requrments:
	pip install -r requirements.txt

	5) To start app: python app.py

	6) Your app available by url: http://localhost:8080/

/* Steps are not required but highly recommended.

### List of samples:

* How to authorize to GroupDocs using the API and get user info
* How to list files within GroupDocs Storage using the Storage API
* How to upload a file to GroupDocs using the Storage API
* How to download a file from GroupDocs Storage using the Storage API
* How to copy / move a file using the GroupDocs Storage API
* How to add a Signature to a document in GroupDocs Signature
* How to create a list of thumbnails for a document
* How to return a URL representing a single page of a Document
* How to generate an embedded Viewer URL for a Document
* How to share a document to other users
* How programmatically create and post an annotation into document. How to delete the annotation
* How to list all annotations from document
* How to add collaborator to doc with annotations
* How to check the list of shares for a folder
* How to check the number of document's views
* How to insert Assembly questionary into webpage
* How to upload a file into the storage and compress it into zip archive
* How to convert Doc to Docx, Docx to Doc, Docx to PDF and PPT to PDF
* How to Compare documents 
* How to Get Compare Change list for document
* How to Create and Upload Envelop to GroupDocs account
* This sample will show how create or update user and add him to collaborators 
* How to View Document pages as images
* How to use StorageApi to upload file from URL to GroupDocs account
* How to merge data fields in docx file with data source and get result file as PDF file
