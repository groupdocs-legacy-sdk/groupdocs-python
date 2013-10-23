### This sample will show how to Compare documents using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.ComparisonApi import ComparisonApi
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.FileStream import FileStream
from groupdocs.AsyncApi import AsyncApi

import os, time

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample19(request):

    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    source = request.POST.get('sourceFileId')
    target = request.POST.get('targetFileId')
    callbackUrl = request.POST.get('callbackUrl')
    sourceFileId = ""
    targetFileId = ""
    iframe = ''
    sourceFile = request.POST.get('file')
    targetFile = request.POST.get('target_file')
    url = request.POST.get('url')
    target_url = request.POST.get('target_url')
    basePath = request.POST.get('server_type')
    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample19.pt',
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
    ### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create ComparisonApi object
    compare = ComparisonApi(apiClient)
    api = StorageApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    api.basePath = basePath
    compare.basePath = basePath
    if url != "" or target_url != "":
        if url != "":
            try:
                # Upload file to current user storage using entere URl to the file
                upload = api.UploadWeb(clientId, url)
                sourceFileId = upload.result.guid

            except Exception, e:
                return render_to_response('__main__:templates/sample19.pt',
                    { 'error' : str(e) })
        if target_url != "":
            try:
                # Upload file to current user storage using entere URl to the file
                upload = api.UploadWeb(clientId, target_url)
                targetFileId = upload.result.guid

            except Exception, e:
                return render_to_response('__main__:templates/sample19.pt',
                    { 'error' : str(e) })
    if sourceFile != "" or targetFile != "":
        if sourceFile != "":
            try:
                #A hack to get uploaded file size
                sourceFile.file.seek(0, 2)
                fileSize = sourceFile.file.tell()
                sourceFile.file.seek(0)

                fs = FileStream.fromStream(sourceFile.file, fileSize)
                ####Make a request to Storage API using clientId

                #Upload file to current user storage
                response = api.Upload(clientId, sourceFile.filename, fs)
                sourceFileId = response.result.guid

            except Exception, e:
                return render_to_response('__main__:templates/sample19.pt',
                    { 'error' : str(e) })
        if targetFile != "":
            try:
                #A hack to get uploaded file size
                targetFile.file.seek(0, 2)
                fileSize = targetFile.file.tell()
                targetFile.file.seek(0)

                fs = FileStream.fromStream(targetFile.file, fileSize)
                ####Make a request to Storage API using clientId

                #Upload file to current user storage
                response = api.Upload(clientId, targetFile.filename, fs)
                targetFileId = response.result.guid

            except Exception, e:
                return render_to_response('__main__:templates/sample19.pt',
                    { 'error' : str(e) })
    if source != '' or target != "":
        if source != "":
            sourceFileId = source

        if target != "":
            targetFileId = target
    # complare files
    info = compare.Compare(clientId, sourceFileId, targetFileId, callbackUrl)
    if info.status == "Ok":
        # Create AsyncApi object
        async = AsyncApi(apiClient)
        async.basePath = basePath
        time.sleep(5)
        # get job info
        jobInfo = async.GetJobDocuments(clientId, info.result.job_id)

        # construct result

        if jobInfo.status == "Ok":
            # Generation of iframe URL using jobInfo.result.outputs[0].guid
            if basePath == "https://api.groupdocs.com/v2.0":
                iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + jobInfo.result.outputs[0].guid
            elif basePath == "https://dev-api.groupdocs.com/v2.0":
                iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + jobInfo.result.outputs[0].guid
            elif basePath == "https://stage-api.groupdocs.com/v2.0":
                iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + jobInfo.result.outputs[0].guid
            iframe = signer.signUrl(iframe)
        else:
            return render_to_response('__main__:templates/sample19.pt',
                { 'error' : info.error_message })
    else:
        return render_to_response('__main__:templates/sample19.pt',
            { 'error' : info.error_message })
    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample19.pt',
        {'userId' : clientId,
         'privateKey' : privateKey,
         'sourceFileId' : sourceFileId,
         'targetFileId' : targetFileId,
         'callbackUrl' : callbackUrl,
         'iframe': iframe
        },
        request=request)