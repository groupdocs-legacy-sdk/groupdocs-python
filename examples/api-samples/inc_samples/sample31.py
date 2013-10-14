### This sample will show how to Create and Upload Envelop to GroupDocs account using Python SDK

# Import of classes from libraries
import os, time, random

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.SignatureApi import SignatureApi
from groupdocs.DocApi import DocApi
from groupdocs.AsyncApi import AsyncApi
from groupdocs.MergeApi import MergeApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.models.Datasource import Datasource
from groupdocs.models.DatasourceField import DatasourceField
from groupdocs.models.SignatureFieldSettingsInfo  import SignatureFieldSettingsInfo
from groupdocs.models.SignatureEnvelopeFieldSettingsInfo import SignatureEnvelopeFieldSettingsInfo

import pdb
# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample31(request):

    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    email = request.POST.get('email')
    name = request.POST.get('name')
    country = request.POST.get('country')
    street = request.POST.get('street')
    city = request.POST.get('city')
    basePath = request.POST.get('server_type')
    fileId = request.POST.get('fileId')
    callbackUrl = request.POST.get('callbackUrl')
    iframe = ''
    message = ''
    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(email) == False or IsNotNull(name) == False or IsNotNull(country) == False or IsNotNull(street) == False or IsNotNull(city) == False:
        return render_to_response('__main__:templates/sample31.pt',
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
    docApi = DocApi(apiClient)
    mergeApi = MergeApi(apiClient)
    asyncApi = AsyncApi(apiClient)
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
    #Set base path
    storage.basePath = basePath
    signature.basePath = basePath
    docApi.basePath = basePath
    mergeApi.basePath = basePath
    asyncApi.basePath = basePath
    guid = fileId
    #Create list with entered data
    enteredData = {"email": email, "country": country, "name": name, "street": street, "city": city}
    #Create new Datasource object
    dataSource = Datasource
    array = []
    #Create DataSourceField object and filing it with entered data
    for key, data in enteredData.iteritems():
        value = [data]
        field = DatasourceField()
        field.name = key
        field.type = "text"
        field.values = value
        array.append(field)
    #Set DataSourceField object to the fields parameter of the DataSource object
    dataSource.fields = array
    try:
        #Add DataSource to GroupDocs
        addDataSource = mergeApi.AddDataSource(clientId, dataSource)
        #Check status
        if addDataSource.status == "Ok":
            try:
                #Merge DataSource with documnet and convert it to PDF
                job = mergeApi.MergeDatasource(clientId, guid, addDataSource.result.datasource_id, targetType = "pdf")

                if job.status == "Ok":
                    #Time delay necessary for server side processing
                    time.sleep(5)
                    i = 0
                    for counter in range(5):
                        # Make request to api for get document info by job id
                        try:
                            jobInfo = asyncApi.GetJobDocuments(clientId, job.result.job_id)

                            if jobInfo.result.job_status == "Completed" or jobInfo.result.job_status == "Archived":
                                break;

                        except Exception, e:
                            return render_to_response('__main__:templates/sample31.pt',
                                { 'error' : str(e) })
                        i = i + 1
                    #If job status Postponed throw exception with error
                    if jobInfo.result.job_status == "Postponed":
                        return render_to_response('__main__:templates/sample31.pt',
                            { 'error' : 'Merge datasource is failed' })
                    fileGuid = jobInfo.result.inputs[0].outputs[0].guid

                    try:
                        # Create envelope using user id and entered by user name
                        envelop = signature.CreateSignatureEnvelope(clientId, name=jobInfo.result.inputs[0].outputs[0].name)

                        if envelop.status == "Ok":
                            time.sleep(3)
                            try:
                                # Add uploaded document to envelope
                                addDocument = signature.AddSignatureEnvelopeDocument(clientId, envelop.result.envelope.id, fileGuid)

                                if addDocument.status == "Ok":
                                    # Get role list for curent user
                                    try:
                                        recipient = signature.GetRolesList(clientId)

                                        if recipient.status == "Ok":
                                            # Get id of role which can sign
                                            roleId = None
                                            for item in recipient.result.roles:
                                                if item.name == "Signer":
                                                    roleId = item.id
                                            #Generate random field name
                                            rand = random.randint(0, 500)
                                            fieldName = "singSample" + str(rand)
                                            #Create SignatureFieldSettings object
                                            fieldSettings = SignatureFieldSettings
                                            fieldSettings.name = fieldName
                                            try:
                                                #Create signatureField
                                                createField = signature.CreateSignatureField(clientId, body = fieldSettings)

                                                if createField.status == "Ok":
                                                    # add recipient
                                                    try:
                                                        addRecipient = signature.AddSignatureEnvelopeRecipient(clientId, envelop.result.envelope.id, email, name, "lastName", roleId)

                                                        if addRecipient.status == "Ok":
                                                            # Get recipient id
                                                            getRecipient = signature.GetSignatureEnvelopeRecipients(clientId, envelop.result.envelope.id)

                                                            if getRecipient.status == "Ok":
                                                                #Get recipient id
                                                                recipientId = getRecipient.result.recipients[0].id
                                                                #Convert callback string to stream
                                                                if (IsNotNull(callbackUrl)):
                                                                    import StringIO as sio
                                                                    stream = sio.StringIO()
                                                                    stream.write(str(callbackUrl))
                                                                    callback = FileStream(None, None, stream.getvalue())

                                                                else:
                                                                    callback = ''
                                                                try:
                                                                    #Get SignatureEnvelopDocuments
                                                                    getDocuments = signature.GetSignatureEnvelopeDocuments(clientId, envelop.result.envelope.id)

                                                                    if getDocuments.status == "Ok":
                                                                        #Create signature field for sign (max LocationX,Y can bee 1.0)
                                                                        signatureSettings = SignatureEnvelopeFieldSettings
                                                                        signatureSettings.locationX = "0.15"
                                                                        signatureSettings.locationY = "0.73"
                                                                        signatureSettings.locationWidth = "150"
                                                                        signatureSettings.locationHeight = "50"
                                                                        signatureSettings.name = fieldName
                                                                        signatureSettings.forceNewField = True
                                                                        signatureSettings.page = "1"
                                                                        try:
                                                                            #Add created sign field to the envelop
                                                                            addSignatureField = signature.AddSignatureEnvelopeField(clientId, envelop.result.envelope.id, getDocuments.result.documents[0].documentId, recipientId, "0545e589fb3e27c9bb7a1f59d0e3fcb9", body = signatureSettings)

                                                                            if addSignatureField.status == "Ok":
                                                                                #Send created envelop
                                                                                send = signature.SignatureEnvelopeSend(clientId, envelop.result.envelope.id, callback)
                                                                                # make result messages

                                                                                if send.status == "Ok":
                                                                                    message = '<p>File was uploaded to GroupDocs. Here you can see your <strong>' + name +  '</strong> file in the GroupDocs Embedded Viewer.</p>';
                                                                                    # Generation of iframe URL using jobInfo.result.outputs[0].guid
                                                                                    if basePath == "https://api.groupdocs.com/v2.0":
                                                                                        iframe = '<iframe src="https://apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId + '" frameborder="0" width="720" height="600"></iframe>'
                                                                                    elif basePath == "https://dev-api.groupdocs.com/v2.0":
                                                                                        iframe = '<iframe src="https://dev-apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId + '" frameborder="0" width="720" height="600"></iframe>'
                                                                                    elif basePath == "https://stage-api.groupdocs.com/v2.0":
                                                                                        iframe = '<iframe src="https://stage-apps.groupdocs.com/signature/signembed/' + envelop.result.envelope.id + '/' + recipientId + '" frameborder="0" width="720" height="600"></iframe>'
                                                                                else:
                                                                                    return render_to_response('__main__:templates/sample31.pt',
                                                                                        { 'error' : send.error_message })
                                                                        except Exception, e:
                                                                            return render_to_response('__main__:templates/sample31.pt',
                                                                                { 'error' : str(e) })
                                                                    else:
                                                                        return render_to_response('__main__:templates/sample31.pt',
                                                                            { 'error' : getDocuments.error_message })
                                                                except Exception, e:
                                                                    return render_to_response('__main__:templates/sample31.pt',
                                                                        { 'error' : str(e) })
                                                            else:
                                                                return render_to_response('__main__:templates/sample31.pt',
                                                                    { 'error' : addRecipient.error_message })
                                                    except Exception, e:
                                                        return render_to_response('__main__:templates/sample31.pt',
                                                            { 'error' : str(e) })
                                                else:
                                                    return render_to_response('__main__:templates/sample31.pt',
                                                        { 'error' : createField.error_message })
                                            except Exception, e:
                                                return render_to_response('__main__:templates/sample31.pt',
                                                    { 'error' : str(e) })
                                        else:
                                            return render_to_response('__main__:templates/sample31.pt',
                                                { 'error' : recipient.error_message })
                                    except Exception, e:
                                        return render_to_response('__main__:templates/sample31.pt',
                                            { 'error' : str(e) })
                                else:
                                    return render_to_response('__main__:templates/sample31.pt',
                                        { 'error' : addDocument.error_message })
                            except Exception, e:
                                return render_to_response('__main__:templates/sample31.pt',
                                    { 'error' : str(e) })
                        else:
                            return render_to_response('__main__:templates/sample31.pt',
                                { 'error' : envelop.error_message })
                    except Exception, e:
                                return render_to_response('__main__:templates/sample31.pt',
                                    { 'error' : str(e) })
                    except Exception, e:
                        return render_to_response('__main__:templates/sample31.pt',
                            { 'error' : str(e) })
                else:
                    return render_to_response('__main__:templates/sample31.pt',
                        { 'error' : job.error_message })
            except Exception, e:
                return render_to_response('__main__:templates/sample31.pt',
                    { 'error' : str(e) })
        else:
            return render_to_response('__main__:templates/sample31.pt',
                { 'error' : addDataSource.error_message })
    except Exception, e:
        return render_to_response('__main__:templates/sample31.pt',
            { 'error' : str(e) })

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample31.pt',
        {'userId' : clientId, 'privateKey' : privateKey, 'email':email, 'name':name, 'envId' : envelop.result.envelope.id, 'iframe': iframe, 'message': message, 'roleId' : roleId, 'callbackUrl' : callbackUrl},
        request=request)