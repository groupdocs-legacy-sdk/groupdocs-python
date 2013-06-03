#####<i>This sample will show how to use <b>Login object</b> to be authorized at GroupDocs and how to get GroupDocs user infromation using Python SDK</i>

#Import of classes from libraries
import base64
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.SharedApi import SharedApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample26(request):
    login = request.POST.get('login')
    password = request.POST.get('password')

    if IsNotNull(login) == False or IsNotNull(password) == False:
        return render_to_response('__main__:templates/sample26.pt',
                                  { 'error' : 'You do not enter you login or password' })
####Create Signer, ApiClient and Shared Api objects

#Create signer object
    signer = GroupDocsRequestSigner("123")
#Create apiClient object
    apiClient = ApiClient(signer)
#Create Management Api object
    api = SharedApi(apiClient)
    #Encode unicode to str
    encodedPassword = password.encode('utf-8')

    try:
        ####Make a request to Management API using clientId
		userInfo = api.LoginUser(login, encodedPassword)
        
    except Exception, e:
        return render_to_response('__main__:templates/sample26.pt',
                                  { 'error' : str(e) })
#If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample26.pt',
                              {
                               'userInfo' : userInfo.result.user
                              }, 
                              request=request)
