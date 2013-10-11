####<i>This sample will show how to create signature form, publish it and configure notification when it was signed</i>

#Import of classes from libraries
import base64
import os
import shutil
import random
from pyramid.renderers import render_to_response
from groupdocs.SignatureApi import SignatureApi
from groupdocs.ApiClient import ApiClient
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.models.WebhookInfo import WebhookInfo
from groupdocs.models.SignatureFormSettingsInfo import SignatureFormSettingsInfo

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample32(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    formGuid = request.POST.get('form_guid')
    templateGuid = request.POST.get('template_guid')
    callbackUrl = request.POST.get('callbackUrl')
    basePath = request.POST.get('server_type')
    email = request.POST.get('email')
    message = ""
    # Checking clientId, privateKey and file_Id
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample32.pt',
                                  { 'error' : 'You do not enter all parameters' })

    #Create text file
    fp = open(currentDir + '/../user_info.txt', 'w')
    #Write user info to text file
    fp.write(clientId + "\r\n" + privateKey + "\r\n" + email)
    fp.close()
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    signatureApi = SignatureApi(apiClient)
    #Set base Path
    if basePath == "":
        basePath = "https://api.groupdocs.com/v2.0"
    signatureApi.basePath = basePath
    #Create webHook and set callback URL
    webHook = WebhookInfo()
    webHook.callbackUrl = callbackUrl
    ####Make a request to Signature API using clientId
    if formGuid != "":
        try:
            #Post form by entered form GUID
            postForm = signatureApi.PublishSignatureForm(clientId, formGuid, body=webHook)
            if postForm.status == "Ok":
                message = '<font color="green">Form is published successfully</font>'
                #Generate iframe url
                if basePath == "https://api.groupdocs.com/v2.0":
                    iframe = 'https://apps.groupdocs.com/signature2/forms/signembed/' + formGuid
                #iframe to dev server
                elif basePath == "https://dev-api.groupdocs.com/v2.0":
                    iframe = 'https://dev-apps.groupdocs.com/signature2/forms/signembed/' + formGuid
                #iframe to test server
                elif basePath == "https://stage-apps-groupdocs.dynabic.com/v2.0":
                    iframe = 'https://stage-apps-groupdocs.dynabic.com/signature2/forms/signembed/' + formGuid
                elif basePath == "http://realtime-api.groupdocs.com":
                    iframe = 'https://relatime-apps.groupdocs.com/signature2/forms/signembed/' + formGuid
            else:
                raise Exception(postForm.error_message)
        except Exception, e:
            return render_to_response('__main__:templates/sample32.pt',
                { 'error' : str(e) })
    #If user select template GUID
    else:
        #Create SignatureFormSettingsInfo object and set parameters values
        formSettings = SignatureFormSettingsInfo()
        formSettings.notifyOwnerOnSign = True
        rand = random.randint(0, 500)
        formName = 'test' + str(rand)
        try:
            #Create form from template
            createForm = signatureApi.CreateSignatureForm(clientId, name=formName, templateGuid=templateGuid, body=formSettings)

            if createForm.status == "Ok":
                try:
                    #Publish created form
                    postForm = signatureApi.PublishSignatureForm(clientId, createForm.result.form.id, body=webHook)
                    if postForm.status == "Ok":
                        message = '<font color="green">Form is published successfully</font>'
                        #Generate iframe url
                        if basePath == "https://api.groupdocs.com/v2.0":
                            iframe = 'https://apps.groupdocs.com/signature2/forms/signembed/' + createForm.result.form.id
                        #iframe to dev server
                        elif basePath == "https://dev-api.groupdocs.com/v2.0":
                            iframe = 'https://dev-apps.groupdocs.com/signature2/forms/signembed/' + createForm.result.form.id
                        #iframe to test server
                        elif basePath == "https://stage-apps-groupdocs.dynabic.com/v2.0":
                            iframe = 'https://stage-apps-groupdocs.dynabic.com/signature2/forms/signembed/' + createForm.result.form.id
                        elif basePath == "http://realtime-api.groupdocs.com":
                            iframe = 'https://relatime-apps.groupdocs.com/signature2/forms/signembed/' + createForm.result.form.id
                    else:
                        raise Exception(postForm.error_message)
                except Exception, e:
                    return render_to_response('__main__:templates/sample32.pt',
                        { 'error' : str(e) })
            else:
                raise Exception(createForm.error_message)
        except Exception, e:
            return render_to_response('__main__:templates/sample32.pt',
                { 'error' : str(e) })
    #If request was successfull - set message variable for template
    return render_to_response('__main__:templates/sample32.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'form_guid' : formGuid,
                               'template_guid' : templateGuid,
                               'url' : iframe,
                               'email' : email,
                               'message' : message },
                              request=request)
