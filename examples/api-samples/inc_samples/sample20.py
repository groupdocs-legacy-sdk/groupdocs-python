### This sample will show how to Get Compare Change list for document using PHP SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.ComparisonApi import ComparisonApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample20(request):

    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    resultFileId = request.POST.get('resultFileId')
    basePath = request.POST.get('server_type')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(resultFileId) == False:
        return render_to_response('__main__:templates/sample20.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create ComparisonApi object
    compare = ComparisonApi(apiClient)

    compare.basePath = basePath

    # get changes
    info = compare.GetChanges(clientId, resultFileId)

    # construct table results
    result = ""
    if info.status == "Ok":
        if info.result.changes is not None:
            result = "<table class='border'>"
            result += "<tr><td><font color='green'>Change Name</font></td><td><font color='green'>Change</font></td></tr>"
            for item in info.result.changes:
                for key in item.__dict__:
                    if key != 'swaggerTypes':
                        if type(item.__dict__[key]).__name__ == 'instance':
                            for value in item.__dict__[key].__dict__:
                                if value != "swaggerTypes":
                                    result += "<tr><td>" + value + "</td><td>" + unicode(item.__dict__[key].__dict__[value]) + "</td></tr>"
                        else:
                            result += "<tr><td>" + key + "</td><td>" + unicode(item.__dict__[key]) + "</td></tr>"

                result += "<tr bgcolor='#808080'><td></td><td></td></tr>"
            result += "</table>"

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample20.pt',
        {'userId' : clientId,
         'privateKey' : privateKey,
         'resultFileId' : resultFileId,
         'result' : result},
        request=request)