### This sample will show how to add collaborator to doc with annotations

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AntApi import AntApi
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.FileStream import FileStream

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample13(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    guid = ""
    email = request.POST.get('email')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(email) == False:
        return render_to_response('__main__:templates/sample13.pt',
                { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create Annotation object
    ant = AntApi(apiClient)
    api = StorageApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    ant.basePath = basePath
    api.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = api.UploadWeb(clientId, url)
            guid = upload.result.guid
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample13.pt',
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
            return render_to_response('__main__:templates/sample13.pt',
                { 'error' : str(e) })
    if fileId != '':
        guid = fileId
    try:
        # Make a request to Annotation API
        ant.SetAnnotationCollaborators(clientId, guid, "v2.0", body=[email])

    except Exception, e:
        return render_to_response('__main__:templates/sample13.pt',
                { 'error' : str(e) })

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample13.pt',
            {
                'userId' : clientId,
                'privateKey' : privateKey,
                'fileId' : guid,
                'email' : email
            },
        request=request)