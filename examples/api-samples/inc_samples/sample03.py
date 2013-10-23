####<i>This sample will show how to use <b>Upload</b> method from Storage Api to upload file to GroupDocs Storage </i>

####Set variables and get POST data

#Import of classes from libraries
import base64
import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample03(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    guid = ""
    name = ""
    # Checking clientId and privateKey
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample03.pt',
                                  { 'error' : 'You do not enter your User Id or Private Key' })
####Create Signer, ApiClient and Storage Api objects

#Create signer object
    signer = GroupDocsRequestSigner(privateKey)
#Create apiClient object
    apiClient = ApiClient(signer)
#Create Storage Api object
    api = StorageApi(apiClient)
    #Check base path
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
    #Set base path
    api.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = api.UploadWeb(clientId, url)
            guid = upload.result.guid
            try:
                ####Make a request to Storage API using clientId

                #Obtaining all Entities from current user
                files = api.ListEntities(userId = clientId, path = 'My Web Documents', pageIndex = 0)
                #Obtaining file name
                for item in files.result.files:
                    #selecting file names
                    if item.guid == guid:
                        name = item.name

            except Exception, e:
                return render_to_response('__main__:templates/sample03.pt',
                    { 'error' : str(e) })

        except Exception, e:
            return render_to_response('__main__:templates/sample03.pt',
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
            guid = response.result.guid
            name = inputFile.filename
        except Exception, e:
            return render_to_response('__main__:templates/sample03.pt',
                { 'error' : str(e) })
    #Generation of Embeded Viewer URL with uploaded file GuId
    iframe = ''
    if basePath == "https://api.groupdocs.com/v2.0":
        iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + guid
    #iframe to dev server
    elif basePath == "https://dev-api.groupdocs.com/v2.0":
        iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + guid
    #iframe to test server
    elif basePath == "https://stage-api.groupdocs.com/v2.0":
        iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + guid
    #Iframe to realtime server
    elif basePath == "http://realtime-api.groupdocs.com":
        iframe = 'https://realtime-apps.groupdocs.com/document-viewer/embed/' + guid
    iframe = signer.signUrl(iframe)
    message = '<p>File was uploaded to GroupDocs. Here you can see your <strong>' + name + '</strong> file in the GroupDocs Embedded Viewer.</p>'

    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample03.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'iframe' : iframe,
                               'message' : message},
                              request=request)
