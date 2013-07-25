### This sample will show how to delete all annotations from document

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample28(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('fileId')
    basePath = request.POST.get('server_type')
    #Check is base path entered
    if basePath == "":
        #If base path empty set base path to the dev server
        basePath = 'https://api.groupdocs.com/v2.0'
    url = ""
    message = ""
    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False:
        return render_to_response('__main__:templates/sample28.pt',
                { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create Annotation object
    ant = AntApi(apiClient)
    ant.basePath = basePath
    try:
        # Make a request to Annotation API using clientId and fileGuId
        response = ant.ListAnnotations(clientId, fileGuId)
        if response.status == "Ok":
            if response.result.annotations:
                    i = 0
                    for annotation in response.result.annotations:
                        try:
                            #Delete annotation by it's guid
                            deleteAnnot = ant.DeleteAnnotation(clientId, response.result.annotations[i].guid)
                            if deleteAnnot.status == "Ok":
                                message = '<span style="color: red">There are no annotations</span>'
                                ### If request was successfull
                                #Generation of iframe URL using $pageImage->result->guid
                                #iframe to prodaction server
                                if basePath == "https://api.groupdocs.com/v2.0":
                                    url = 'https://apps.groupdocs.com/document-viewer/embed/' + fileGuId
                                #iframe to dev server
                                elif basePath == "https://dev-api.groupdocs.com/v2.0":
                                    url = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + fileGuId
                                #iframe to test server
                                elif basePath == "https://stage-api.groupdocs.com/v2.0":
                                    url = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + fileGuId
                                elif basePath == "http://realtime-api.groupdocs.com":
                                    url = 'http://realtime-apps.groupdocs.com/document-viewer/embed/' + fileGuId
                        except Exception, e:
                            return render_to_response('__main__:templates/sample28.pt',
                                { 'error' : str(e) })
                        i = i + 1
            else:
                message = '<span style="color: red">There are no annotations in this document</span>'
    except Exception, e:
        return render_to_response('__main__:templates/sample28.pt',
                { 'error' : str(e) })

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample28.pt',
            { 'userId' : clientId,
              'privateKey' : privateKey,
              'fileId' : fileGuId,
              'message' : message,
              'url' : url},
        request=request)