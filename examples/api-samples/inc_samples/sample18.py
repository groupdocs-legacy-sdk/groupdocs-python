### This sample will show how to convert Doc to Docx, Docx to Doc, Docx to PDF and PPT to PDF

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AsyncApi import AsyncApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

import time

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 18
def sample18(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileId = request.POST.get('fileId')
    targetType = request.POST.get('convert_type')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileId) == False or IsNotNull(targetType) == False:
        return render_to_response('__main__:templates/sample18.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and AsyncApi objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create AsyncApi object
    async = AsyncApi(apiClient)

    try:
        convert = async.Convert(clientId, fileId, targetType=targetType)
        # check request status
        if convert.status == "Ok":
            # Delay necessary that the inquiry would manage to be processed
            time.sleep(5)
            # Make request to api for get document info by job id
            jobs = async.GetJobDocuments(clientId, convert.result.job_id)
            # Get file guid
            guid = jobs.result.inputs[0].outputs[0].guid
            # Generating iframe
            iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/embed/' + guid + '" frameborder="0" width="100%" height="600"></iframe>'

    except Exception, e:
        return render_to_response('__main__:templates/sample18.pt',
            { 'error' : str(e) })


    # Set variables for template
    return render_to_response('__main__:templates/sample18.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'fileId' : fileId,
            'targetType' : targetType,
            'iframe' : iframe
            },
        request=request)