### This sample will show how create or update user and add him to collaborators using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.MgmtApi import MgmtApi
from groupdocs.models.UserInfo import UserInfo
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

import json

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample22(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileId = request.POST.get('fileId')
    email = request.POST.get('email')
    name = request.POST.get('first_name')
    lastName = request.POST.get('last_name')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileId) == False or IsNotNull(email) == False or IsNotNull(name) == False or IsNotNull(lastName) == False:
        return render_to_response('__main__:templates/sample22.pt',
            { 'error' : 'You do not enter all parameters' })

    #### Create Signer, ApiClient and Annotation Api objects
    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create mgmtApi object
    mgmt = MgmtApi(apiClient)
    # Create AntApi object
    ant = AntApi(apiClient)

    # reate User info object
    user = UserInfo
    user.nickname = name
    user.firstname = name
    user.lastname = lastName
    user.primary_email = email

    iframe = ''
    message = ''

    # Creating of new user
    newUser = mgmt.UpdateAccountUser(clientId, email, user)

    # Check the result of the request
    if newUser.status == "Ok":

        # Make request to Ant api for set new user as annotation collaborator
        ant.SetAnnotationCollaborators(clientId, fileId, "2.0", body=[email])

        # Make request to Annotation api to receive all collaborators for entered file id
        getCollaborators = ant.GetAnnotationCollaborators(clientId, fileId)

        #Set reviewers rights for new user. $newUser->result->guid - GuId of created user, $fileId - entered file id,
        ant.SetReviewerRights(clientId, fileId, getCollaborators.result.collaborators)

        # Generating iframe for template
        iframe = '<iframe src="https://apps.groupdocs.com//document-annotation2/embed/' + fileId + '?&uid=' + newUser.result.guid +  '&download=true frameborder="0" width="720" height="600"><iframe>';

    else :
        message = newUser.error_message

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample22.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'fileId' : fileId,
            'email':email,
            'name':name,
            'lastName': lastName,
            'iframe': iframe,
            'message': message
            },
        request=request)