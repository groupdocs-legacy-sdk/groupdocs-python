####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64
import json, time



from pyramid.renderers import render_to_response
from pyramid.response import Response

from groupdocs.ApiClient import ApiClient
from groupdocs.SignatureApi import SignatureApi
from groupdocs.models.SignatureSignDocumentSettings import SignatureSignDocumentSettings
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample06(request):
    if request.content_type != 'application/json':
        return render_to_response('__main__:templates/sample06.pt', { })
    #Request to json

    jsonPostData = request.json_body
#    import pdb; pdb.set_trace()
    #Get parameters
    clientId = jsonPostData["userId"]
    privateKey = jsonPostData["privateKey"]
    documents = jsonPostData['documents']
    signers = jsonPostData['signers']
    #Checking parameters

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(documents) == False or IsNotNull(signers) == False:
        return render_to_response('__main__:templates/sample06.pt',
                                  { 'error' : 'You do not enter you User id or Private key' })
    #Determination of placeSignatureOn parameter
    for i, signer in enumerate(signers):
        signers[i]['placeSignatureOn'] = ''
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signerReq = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signerReq)
    #Create Signsture API object
    signatureApi = SignatureApi(apiClient)
#    signatureApi.basePath = basePath
    #Create setting variable for signature SignDocument method
    settings = SignatureSignDocumentSettings()
    settings.documents = documents
    settings.signers = signers
####Make a request to Signature Api for sign document

#Sign document using current user id and sign settings
    response = signatureApi.SignDocument(clientId, body = settings)

    #If request was successfull - set variables for template
    error = ''
    if response.status == 'Ok':
        time.sleep(5)
        getDocumentStatus = signatureApi.GetSignDocumentStatus(clientId, response.result.jobId);
        if getDocumentStatus.status == "Ok":

            guid = getDocumentStatus.result.documents[0].documentId

            iframe = ''
#            if basePath == "https://api.groupdocs.com/v2.0":
            iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + guid
#            elif basePath == "https://dev-api-groupdocs.dynabic.com/v2.0":
#                iframe = 'https://dev-apps-groupdocs.dynabic.com/document-viewer/embed/' + guid
#            elif basePath == "https://stage-api-groupdocs.dynabic.com/v2.0":
#                iframe = 'https://stage-apps-groupdocs.dynabic.com/document-viewer/embed/' + guid
            return_data = json.dumps({ 'responseCode' : 200, 'url' : iframe })
            return Response(body = return_data, content_type = 'application/json')
        else:
            error = getDocumentStatus.error_message
            return render_to_response('__main__:templates/sample06.pt',
                { 'error' : response.error_message })
    else:
        error = response.error_message
        return render_to_response('__main__:templates/sample06.pt',
                          { 'error' : response.error_message })
