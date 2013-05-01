####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.FileStream import FileStream

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample10(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    guid = ""
    email = request.POST.get('email')
    #Checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(email) == False:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'error' : 'You do not enter all parameters' })
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    api = StorageApi(apiClient)
    docApi = DocApi(apiClient)
    ####Make request to DocApi using user id
    #Check base path
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    docApi.basePath = basePath
    api.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = api.UploadWeb(clientId, url)
            guid = upload.result.id
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample10.pt',
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
            response = api.Upload(clientId, inputFile.filename, fs)
            guid = response.result.id
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample10.pt',
                { 'error' : str(e) })
    if fileId != '':
        try:
            #Geting all Entities from current user
            files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
            #Selecting file names
            for item in files.result.files:
                if item.guid == fileId:
                    guid = item.id
        except Exception, e:
            return render_to_response('__main__:templates/sample10.pt',
                { 'error' : str(e) })
    try:

        #Make request to user storage for sharing document
        docApi.ShareDocument(clientId, guid, body = [ email, ])
    except Exception, e:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'error' : str(e) })
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample10.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'fileId' : guid,
                               'email' : email }, 
                              request=request)
