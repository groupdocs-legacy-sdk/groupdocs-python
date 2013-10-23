### This sample will show how to convert Doc to Docx, Docx to Doc, Docx to PDF and PPT to PDF

# Import of classes from libraries
import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AsyncApi import AsyncApi
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.FileStream import FileStream

import time

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 18
def sample18(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    callbackUrl = request.POST.get('callbackUrl')
    guid = ""
    iframe = ""
    targetType = request.POST.get('convert_type')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(targetType) == False:
        return render_to_response('__main__:templates/sample18.pt',
            { 'error' : 'You do not enter all parameters' })
    #Get curent work directory
    currentDir = os.path.dirname(os.path.realpath(__file__))
    #Create text file
    fp = open(currentDir + '/../user_info.txt', 'w')
    #Write user info to text file
    fp.write(clientId + "\r\n" + privateKey)
    fp.close()
    #Clear downloads folder
    if os.path.isdir(currentDir + '/../downloads'):
        #Get list of files
        for the_file in os.listdir(currentDir + '/../downloads'):
            file_path = os.path.join(currentDir + '/../downloads', the_file)
            try:
                #Delete file from folder
                os.unlink(file_path)

            except Exception, e:
                print e
    ### Create Signer, ApiClient and AsyncApi objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create AsyncApi object
    async = AsyncApi(apiClient)
    # Create Storage object
    api = StorageApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    api.basePath = basePath
    async.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = api.UploadWeb(clientId, url)
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
            response = api.Upload(clientId, inputFile.filename, fs)
            guid = response.result.guid
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample16.pt',
                { 'error' : str(e) })
    if fileId != '':
        guid = fileId

    try:
        convert = async.Convert(clientId, guid, new_type=targetType, callbackUrl = callbackUrl)
        # check request status
        if convert.status == "Ok":
            # Delay necessary that the inquiry would manage to be processed
            time.sleep(5)
            # Make request to api for get document info by job id
            jobs = async.GetJobDocuments(clientId, convert.result.job_id)
            # Get file guid
            resultGuid = jobs.result.inputs[0].outputs[0].guid
            #Generation of iframe URL using fileGuId
            if basePath == "https://api.groupdocs.com/v2.0":
                iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + resultGuid
            #iframe to dev server
            elif basePath == "https://dev-api.groupdocs.com/v2.0":
                iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + resultGuid
            #iframe to test server
            elif basePath == "https://stage-api.groupdocs.com/v2.0":
                iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + resultGuid
            #Iframe to realtime server
            elif basePath == "http://realtime-api.groupdocs.com":
                iframe = 'https://realtime-apps.groupdocs.com/document-viewer/embed/' + resultGuid
            iframe = signer.signUrl(iframe)
    except Exception, e:
        return render_to_response('__main__:templates/sample18.pt',
            { 'error' : str(e) })


    # Set variables for template
    return render_to_response('__main__:templates/sample18.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'fileId' : guid,
            'targetType' : targetType,
            'iframe' : iframe,
            'callback' : callbackUrl
            },
        request=request)