### This sample will show how to Create and Upload Envelop to GroupDocs account using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.SignatureApi import SignatureApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

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

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(email) == False or IsNotNull(name) == False or IsNotNull(lastName) == False:
        return render_to_response('__main__:templates/sample21.pt',
            { 'error' : 'You do not enter all parameters' })

    #### Create Signer, ApiClient and Annotation Api objects
    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create StorageApi object
    storage = StorageApi(apiClient)


    try:
        # a hack to get uploaded file size
        inputFile.file.seek(0, 2)
        fileSize = inputFile.file.tell()
        inputFile.file.seek(0)

        fs = FileStream.fromStream(inputFile.file, fileSize)
        #~ import pdb;  pdb.set_trace()

        # upload file and get response
        upload = storage.Upload(clientId, inputFile.filename, fs)

        # Check if file uploaded successfully
        if upload.status == "Ok":

            iframe = ''
            message = ''

            # Create SignatureApi object
            signature = SignatureApi(apiClient)

            # Create envelope using user id and entered by user name
            envelop = signature.CreateSignatureEnvelope(clientId, name=inputFile.filename)

            # Add uploaded document to envelope
            signature.AddSignatureEnvelopeDocument(clientId, envelop.result.envelope.id, upload.result.guid)

            # Get role list for curent user
            recipient = signature.GetRolesList(clientId)

            # Get id of role which can sign
            roleId = None
            for item in recipient.result.roles:
                if item.name == "Signer":
                    roleId = item.id

            # add recipient
            signature.AddSignatureEnvelopeRecipient(clientId, envelop.result.envelope.id, email, name, lastName, roleId)

            # Get recipient id
            getRecipient = signature.GetSignatureEnvelopeRecipients(clientId, envelop.result.envelope.id)
            recipientId = getRecipient.result.recipients[0].id

            # save and send
            send = signature.SignatureEnvelopeSend(clientId, envelop.result.envelope.id)

            # make result messages
            if send.status == "Ok":
                message = '<p>File was uploaded to GroupDocs. Here you can see your <strong>' + inputFile.filename +  '</strong> file in the GroupDocs Embedded Viewer.</p>';
                iframe = '<iframe src="https://apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId + '" frameborder="0" width="720" height="600"></iframe>'


    except Exception, e:
        return render_to_response('__main__:templates/sample21.pt',
            { 'error' : str(e) })


    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample21.pt',
        {'userId' : clientId, 'privateKey' : privateKey, 'email':email, 'name':name, 'lastName': lastName, 'envId' : envelop.result.envelope.id, 'iframe': iframe, 'message': message, 'roleId' : roleId},
        request=request)