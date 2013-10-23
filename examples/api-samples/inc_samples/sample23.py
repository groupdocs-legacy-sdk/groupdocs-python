### This sample will show how to View Document pages as images using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample23(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    guid = ""

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample23.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Doc Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create DocApi object
    doc = DocApi(apiClient)
    # Create StorageApi object
    storage = StorageApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    storage.basePath = basePath
    # Set url to choose whot server to use
    doc.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = storage.UploadWeb(clientId, url)
            guid = upload.result.guid
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample16.pt',
                { 'error' : str(e) })

    if inputFile != "":
        try:
            #A hack to get uploaded file size
            inputFile.file.seek(0, 2)
            fileSize = inputFile.file.tell()
            inputFile.file.seek(0)

            fs = FileStream.fromStream(inputFile.file, fileSize)
            ####Make a request to Storage API using clientId

            #Upload file to current user storage
            response = storage.Upload(clientId, inputFile.filename, fs)
            guid = response.result.guid

            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample16.pt',
                { 'error' : str(e) })
    if fileId != '':
        guid = fileId
    # Make request yo the Api to get images for all document pages
    pageImage = doc.ViewDocument(clientId, guid, pageNumber=0, pageCount=-1, width=100)

    # Check the result of the request
    if pageImage.status == "Ok":
        # Generation of iframe URL using pageImage.result.guid
        if basePath == "https://api.groupdocs.com/v2.0":
            iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + pageImage.result.guid
        elif basePath == "https://dev-api.groupdocs.com/v2.0":
            iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + pageImage.result.guid
        elif basePath == "https://stage-api.groupdocs.com/v2.0":
            iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + pageImage.result.guid
        iframe = signer.signUrl(iframe)
    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample23.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'fileId' : guid,
            'iframe' : iframe
        },
        request=request)