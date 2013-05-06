####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.FileStream import FileStream

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample05(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('srcPath')
    ID = ""
    name = ''
    message = ''
    destPath = request.POST.get('destPath')
    copy = request.POST.get('copy')
    move = request.POST.get('move')

    ####Check clientId, privateKey and file Id
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(destPath) == False:
        return render_to_response('__main__:templates/sample05.pt',
                                  { 'error' : 'You do not enter all parameters' })

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
            ID = upload.result.id

            try:
                ####Make a request to Storage API using clientId

                #Obtaining all Entities from current user
                files = api.ListEntities(userId = clientId, path = 'My Web Documents', pageIndex = 0)
                #Obtaining file name
                for item in files.result.files:
                    #selecting file names
                    if item.guid == upload.result.guid:
                        name = item.name

            except Exception, e:
                return render_to_response('__main__:templates/sample05.pt',
                    { 'error' : str(e) })
        except Exception, e:
            return render_to_response('__main__:templates/sample05.pt',
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
            ID = response.result.id
            name = inputFile.filename
        except Exception, e:
            return render_to_response('__main__:templates/sample05.pt',
                { 'error' : str(e) })
    if fileId != '':

        try:
            ####Make a request to Storage API using clientId

            #Obtaining all Entities from current user
            try:
                files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
            except Exception, e:
                return render_to_response('__main__:templates/sample05.pt',
                    { 'error' : str(e) })
            #Obtaining file names
            names = ''
            for item in files.result.files:
                if item.guid == fileId:
                    #selecting file names
                    ID = item.id
                    name = item.name

        except Exception, e:
            return render_to_response('__main__:templates/sample05.pt',
                { 'error' : str(e) })
####Make a request to Storage API using clientId

    #If user choose copy
    if copy:
        try:
            file = api.MoveFile(clientId, destPath + '/' + name, Groupdocs_Copy = ID)
            message = 'File was copied to the <font color="blue">' + destPath + '/' + name + '</font> folder'
        except Exception, e:
            return render_to_response('__main__:templates/sample05.pt',
                { 'error' : str(e) })


    #If user choose move
    if move:
        try:
            file = api.MoveFile(clientId, destPath + '/' + name, Groupdocs_Move = ID)
            message = 'File was moved to the <font color="blue">' + destPath + '/' + name + '</font> folder'
        except Exception, e:
            return render_to_response('__main__:templates/sample05.pt',
                { 'error' : str(e) })

    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample05.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'message' : message},
                              request=request)
