### This sample will show how to Compare documents using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.ComparisonApi import ComparisonApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.AsyncApi import AsyncApi

import os, time

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample19(request):

    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    sourceFileId = request.POST.get('sourceFileId')
    targetFileId = request.POST.get('targetFileId')
    callbackUrl = request.POST.get('callbackUrl')
    basePath = request.POST.get('server_type')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(sourceFileId) == False or IsNotNull(targetFileId) == False:
        return render_to_response('__main__:templates/sample19.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create ComparisonApi object
    compare = ComparisonApi(apiClient)
    # Create AsyncApi object
    async = AsyncApi(apiClient)

    async.basePath = basePath

    # complare files
    info = compare.Compare(clientId, sourceFileId, targetFileId, callbackUrl)
    # wait some time when conversation finished
    time.sleep(5)

    # get job info
    jobInfo = async.GetJobDocuments(clientId, info.result.job_id)

    # construct result
    iframe = ''
    if jobInfo.status == "Ok" and jobInfo.result.outputs[0].guid is not None:
        # Generation of iframe URL using jobInfo.result.outputs[0].guid
        if basePath == "https://api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/embed/' + jobInfo.result.outputs[0].guid + ' frameborder="0" width="720" height="600"><iframe>'
        elif basePath == "https://dev-api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://dev-apps.groupdocs.com/document-viewer/embed/' + jobInfo.result.outputs[0].guid + ' frameborder="0" width="720" height="600"><iframe>'
        elif basePath == "https://stage-api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://stage-apps.groupdocs.com/document-viewer/embed/' + jobInfo.result.outputs[0].guid + ' frameborder="0" width="720" height="600"><iframe>'

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