####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64

from pyramid.renderers import render_to_response
from groupdocs.ApiClient import ApiClient
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.FileStream import FileStream
from groupdocs.StorageApi import StorageApi
# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample09(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    guid = ""
    width = request.POST.get('width') or '300'
    height = request.POST.get('height') or '200'
    #Checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample09.pt',
                                  { 'error' : 'You do not enter all parameters' })
        ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    api = StorageApi(apiClient)
    ####Make request to DocApi using user id
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
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample09.pt',
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
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample09.pt',
                { 'error' : str(e) })
    if fileId != '':
        guid = fileId
    #Generation of iframe URL using fileGuId
    if basePath == "https://api.groupdocs.com/v2.0":
        iframe_url = 'https://apps.groupdocs.com/document-viewer/embed/' + guid + '?frameborder=0&width=' + width + '&height=' + height
    #iframe to dev server
    elif basePath == "https://dev-api.groupdocs.com/v2.0":
        iframe_url = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + guid + '?frameborder=0&width=' + width + '&height=' + height
    #iframe to test server
    elif basePath == "https://stage-api.groupdocs.com/v2.0":
        iframe_url = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + guid + '?frameborder=0&width=' + width + '&height=' + height
    #Iframe to realtime server
    elif basePath == "http://realtime-api.groupdocs.com":
        iframe_url = 'https://realtime-apps.groupdocs.com/document-viewer/embed/' + guid + '?frameborder=0&width=' + width + '&height=' + height

    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample09.pt',
                              { 'userId' : clientId,
                                'privateKey' : privateKey,
                               'iframe_url' : iframe_url,
                               'fileId' : guid,
                               'width' : width,
                               'height' : height },
                              request=request)
