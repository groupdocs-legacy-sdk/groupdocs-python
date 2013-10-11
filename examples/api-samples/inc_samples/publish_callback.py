import os
import json
import shutil
import time
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyramid.renderers import render_to_response
from pyramid.response import Response

from groupdocs.ApiClient import ApiClient
from groupdocs.SignatureApi import SignatureApi
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

def publish_callback(request):
    currentDir = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(currentDir + '/../user_info.txt'):
        f = open(currentDir + '/../user_info.txt', "r")
        lines = f.readlines()
        f.close()
        lineArray = []
        lineArray = lines[0].split()
        clientId = lineArray[0]
        privateKey = lineArray[1]
        email = lineArray[2]

    if IsNotNull(request.json_body):
        jsonPostData = request.json_body
        formId = jsonPostData['SourceId']
        #Create signer object
        signer = GroupDocsRequestSigner(privateKey)
        # Create apiClient object
        apiClient = ApiClient(signer)
        # Create AsyncApi object
        signature = SignatureApi(apiClient)
        # Create Storage object
        getFileFromForm = signature.PublicGetSignatureFormDocuments(formId)
        if getFileFromForm.status == "Ok":
            documentName = getFileFromForm.result.documents[0].name
            out = "noreply@groupdocs.com"
            to = email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Link"
            msg['From'] = out
            msg['To'] = to
            html = """\
                <html>
                  <head></head>
                  <body>
                    <p>Document""" + documentName + """ is signed</p>
                  </body>
                </html>
                """
            body = MIMEText(html, 'html')
            msg.attach(body)
            s = smtplib.SMTP('localhost')
            s.sendmail(out, to, msg.as_string())
            s.quit()