### This sample will show how to upload a file into the storage and compress it into zip archive

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample17(request):

    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    id = ""
    name = ""
    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample17.pt',
                { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and StorageApi objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create StorageApi object
    api = StorageApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
    #Set base path
    api.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = api.UploadWeb(clientId, url)
            id = upload.result.id
            inputFile = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample17.pt',
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
            id = response.result.id

        except Exception, e:
            return render_to_response('__main__:templates/sample17.pt',
                { 'error' : str(e) })
    result = ''
    try:
        # compress file using upload response
        compress = api.Compress(clientId, id, "zip")
        if compress.status == "Ok":
            result = "Archive created and saved successfully"

    except Exception, e:
        return render_to_response('__main__:templates/sample17.pt',
            { 'error' : str(e) })

    # Set variables for template
    return render_to_response('__main__:templates/sample17.pt',
            {
            'userId' : clientId,
            'privateKey' : privateKey,
            'result' : result,
        },
        request=request)