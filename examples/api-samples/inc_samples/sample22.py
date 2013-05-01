### This sample will show how create or update user and add him to collaborators using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.MgmtApi import MgmtApi
from groupdocs.models.UserInfo import UserInfo
from groupdocs.models.RoleInfo import RoleInfo
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample22(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    guid = ""
    email = request.POST.get('email')
    name = request.POST.get('first_name')
    lastName = request.POST.get('last_name')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(email) == False or IsNotNull(name) == False or IsNotNull(lastName) == False:
        return render_to_response('__main__:templates/sample22.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Mgmt Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create mgmtApi object
    mgmt = MgmtApi(apiClient)
    # Create StorageApi object
    storage = StorageApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    storage.basePath = basePath
    # Declare which server to use
    mgmt.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = storage.UploadWeb(clientId, url)
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
            response = storage.Upload(clientId, inputFile.filename, fs)
            guid = response.result.guid

            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample16.pt',
                { 'error' : str(e) })
    if fileId != '':
        guid = fileId

    #Create Role info object
    role = RoleInfo
    #Set user role Id. Can be: 1 -  SysAdmin, 2 - Admin, 3 - User, 4 - Guest
    role.id = "3"
    #Set user role name. Can be: SysAdmin, Admin, User, Guest
    role.name = "User"
    #Create dict of roles.
    roles = [role]

    # Create User info object
    user = UserInfo
    # Set nick name as entered first name
    user.nickname = name
    # Set first name as entered first name
    user.firstname = name
    # Set last name as entered last name
    user.lastname = lastName
    # Set email as entered email
    user.primary_email = email
#    user.roles = roles

    iframe = ''

    # Creating of new user
    newUser = mgmt.UpdateAccountUser(clientId, email, user)

    # Check the result of the request
    if newUser.status == "Ok":

        # Create AntApi object
        ant = AntApi(apiClient)
        ant.basePath = basePath
        # Make request to Ant api for set new user as annotation collaborator
        addCollaborator = ant.SetAnnotationCollaborators(clientId, guid, "2.0", body=[email])

        # Make request to Annotation api to receive all collaborators for entered file id
        getCollaborators = ant.GetAnnotationCollaborators(clientId, guid)

        #Set reviewers rights for new user
        setReviewer = ant.SetReviewerRights(clientId, guid, getCollaborators.result.collaborators)

        # Generating iframe for template
        if basePath == "https://api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://apps.groupdocs.com/document-annotation2/embed/' + guid + '?&uid=' + newUser.result.guid + '&download=true frameborder="0" width="720" height="600"></iframe>'
        elif basePath == "https://dev-api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://dev-apps.groupdocs.com/document-annotation2/embed/' + guid + '?&uid=' + newUser.result.guid + '&download=true frameborder="0" width="720" height="600"></iframe>'
        elif basePath == "https://stage-api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://stage-apps.groupdocs.com/document-annotation2/embed/' + guid + '?&uid=' + newUser.result.guid + '&download=true frameborder="0" width="720" height="600"></iframe>'

    errorMessage = newUser.error_message
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
            'errorMessage': errorMessage
            },
        request=request)