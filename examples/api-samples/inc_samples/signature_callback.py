import os
import json
import shutil
import time

from pyramid.renderers import render_to_response
from pyramid.response import Response

from groupdocs.ApiClient import ApiClient
from groupdocs.SignatureApi import SignatureApi
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

def signature_callback(request):
    currentDir = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(currentDir + '/../user_info.txt'):
        f = open(currentDir + '/../user_info.txt')
        lines = f.readlines()
        f.close()
        clientId = lines[0].replace("\r\n", "")
        privateKey = lines[1]

    if IsNotNull(request.json_body):
        jsonPostData = request.json_body
        envelopId = jsonPostData['SourceId']
        # Create signer object
        signer = GroupDocsRequestSigner(privateKey)
        # Create apiClient object
        apiClient = ApiClient(signer)
        # Create AsyncApi object
        signature = SignatureApi(apiClient)
        # Create Storage object
        api = StorageApi(apiClient)
        if envelopId != '':
            time.sleep(5)
            print envelopId
            document = signature.GetEnvelopeDocuments(envelopId, clientId)

            if document.status == "Ok":
                guid = document.result.documents[0].documentId
                name = document.result.documents[0].name
                currentDir = os.path.dirname(os.path.realpath(__file__))
                downloadFolder = currentDir + '/../downloads/'
                if not os.path.isdir(downloadFolder):
                    os.makedirs(downloadFolder)

                #Downlaoding of file
                fs = api.GetFile(clientId, guid);

                if fs:

                    filePath = downloadFolder + name

                    with open(filePath, 'wb') as fp:
                        shutil.copyfileobj(fs.inputStream, fp)