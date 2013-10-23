### This sample will show how to Create and Upload Envelop to GroupDocs account using Python SDK

# Import of classes from libraries
import os, random

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.SignatureApi import SignatureApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.models.WebhookInfo import WebhookInfo
from groupdocs.models.SignatureEnvelopeFieldSettingsInfo import SignatureEnvelopeFieldSettingsInfo

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample21(request):

    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    email = request.POST.get('email')
    name = request.POST.get('name')
    lastName = request.POST.get('lastName')
    inputFile = request.POST.get('file')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    callbackUrl = request.POST.get('callbackUrl')
    guid = ""
    fileName = ""
    iframe = ''
    message = ''
    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(email) == False or IsNotNull(name) == False or IsNotNull(lastName) == False:
        return render_to_response('__main__:templates/sample21.pt',
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
    # Create StorageApi object
    storage = StorageApi(apiClient)
    # Create SignatureApi object
    signature = SignatureApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
        #Set base path
    storage.basePath = basePath
    signature.basePath = basePath
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            upload = storage.UploadWeb(clientId, url)
            guid = upload.result.guid
            try:
                ####Make a request to Storage API using clientId

                #Obtaining all Entities from current user
                files = storage.ListEntities(userId = clientId, path = 'My Web Documents', pageIndex = 0)
                #Obtaining file name
                for item in files.result.files:
                    #selecting file names
                    if item.guid == guid:
                        fileName = item.name

            except Exception, e:
                return render_to_response('__main__:templates/sample21.pt',
                    { 'error' : str(e) })
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample21.pt',
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
            fileName = inputFile.filename
            fileId = ""
        except Exception, e:
            return render_to_response('__main__:templates/sample21.pt',
                { 'error' : str(e) })
    if fileId != '':
        guid = fileId
        try:
            ####Make a request to Storage API using clientId

            #Obtaining all Entities from current user
            files = storage.ListEntities(userId = clientId, path = 'My Web Documents', pageIndex = 0)
            #Obtaining file name
            for item in files.result.files:
                #selecting file names
                if item.guid == guid:
                    fileName = item.name

        except Exception, e:
            return render_to_response('__main__:templates/sample21.pt',
                { 'error' : str(e) })
    try:
        # Create envelope using user id and entered by user name
        envelop = signature.CreateSignatureEnvelope(clientId, name=fileName)
        if envelop.status == "Ok":
            # Add uploaded document to envelope
            addDocument = signature.AddSignatureEnvelopeDocument(clientId, envelop.result.envelope.id, guid)
            if addDocument.status == "Ok":
                # Get role list for curent user
                recipient = signature.GetRolesList(clientId)
                if recipient.status == "Ok":
                    # Get id of role which can sign
                    roleId = None
                    for item in recipient.result.roles:
                        if item.name == "Signer":
                            roleId = item.id

                    # add recipient
                    addRecipient = signature.AddSignatureEnvelopeRecipient(clientId, envelop.result.envelope.id, email, name, lastName, roleId)
                    if addRecipient.status == "Ok":
                        # Get recipient id
                        getRecipient = signature.GetSignatureEnvelopeRecipients(clientId, envelop.result.envelope.id)
                        if getRecipient.status == "Ok":
                            recipientId = getRecipient.result.recipients[0].id
                            if (IsNotNull(callbackUrl)):
                                webHook = WebhookInfo
                                webHook.callbackUrl = callbackUrl

                            else:
                                webHook = WebhookInfo
                                webHook.callbackUrl = ''
                            getEnvelopDocument = signature.PublicGetEnvelopeDocuments(envelop.result.envelope.id,  recipientId)
                            if getEnvelopDocument.status == "Ok":
                                rand = random.randint(0, 500)
                                SignatureEnvelopeFieldSettings = SignatureEnvelopeFieldSettingsInfo
                                SignatureEnvelopeFieldSettings.locationX = "0.15"
                                SignatureEnvelopeFieldSettings.locationY = "0.73"
                                SignatureEnvelopeFieldSettings.locationWidth = "150"
                                SignatureEnvelopeFieldSettings.locationHeight = "50"
                                SignatureEnvelopeFieldSettings.name = "test" + str(rand)
                                SignatureEnvelopeFieldSettings.forceNewField = True
                                SignatureEnvelopeFieldSettings.page = "1"
                                addField = signature.AddSignatureEnvelopeField(clientId, envelop.result.envelope.id, getEnvelopDocument.result.documents[0].documentId, recipientId, "0545e589fb3e27c9bb7a1f59d0e3fcb9", body=SignatureEnvelopeFieldSettings)
                                if addField.status == "Ok":
                                    send = signature.SignatureEnvelopeSend(clientId, envelop.result.envelope.id, body=webHook)
                                    # make result messages
                                    if send.status == "Ok":
                                        message = '<p>File was uploaded to GroupDocs. Here you can see your <strong>' + name +  '</strong> file in the GroupDocs Embedded Viewer.</p>';
                                        # Generation of iframe URL using jobInfo.result.outputs[0].guid
                                        if basePath == "https://api.groupdocs.com/v2.0":
                                            iframe = 'https://apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId
                                        elif basePath == "https://dev-api.groupdocs.com/v2.0":
                                            iframe = 'https://dev-apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId
                                        elif basePath == "https://stage-api.groupdocs.com/v2.0":
                                            iframe = 'https://stage-apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId
                                        iframe = signer.signUrl(iframe)
                                    else:
                                        return render_to_response('__main__:templates/sample21.pt',
                                            { 'error' : send.error_message})
                                else:
                                    return render_to_response('__main__:templates/sample21.pt',
                                        { 'error' : addField.error_message })
                            else:
                                return render_to_response('__main__:templates/sample21.pt',
                                    { 'error' : getEnvelopDocument.error_message })
                        else:
                            return render_to_response('__main__:templates/sample21.pt',
                                { 'error' : getRecipient.error_message })
                    else:
                        return render_to_response('__main__:templates/sample21.pt',
                            { 'error' : addRecipient.error_message })
                else:
                    return render_to_response('__main__:templates/sample21.pt',
                        { 'error' : recipient.error_message })
            else:
                return render_to_response('__main__:templates/sample21.pt',
                    { 'error' : addDocument.error_message })
        else:
            return render_to_response('__main__:templates/sample21.pt',
                { 'error' : envelop.error_message })
    except Exception, e:
        return render_to_response('__main__:templates/sample21.pt',
            { 'error' : str(e) })


    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample21.pt',
        {'userId' : clientId, 'privateKey' : privateKey, 'email':email, 'name':name, 'lastName': lastName, 'envId' : envelop.result.envelope.id, 'iframe': iframe, 'message': message, 'roleId' : roleId, 'callbackUrl' : callbackUrl},
        request=request)