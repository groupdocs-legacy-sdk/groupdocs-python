####<i>This sample will show how to use <b>Upload</b> method from Storage Api to upload file to GroupDocs Storage </i>

####Set variables and get POST data

#Import of classes from libraries
import base64
import os
import time
import shutil
from pyramid.renderers import render_to_response

import pdb;

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.AsyncApi import AsyncApi
from groupdocs.DocApi import DocApi
from groupdocs.MergeApi import MergeApi
from groupdocs.models.Datasource import Datasource
from groupdocs.models.DatasourceField import DatasourceField
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample25(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    fileId = request.POST.get('fileId')
    url = request.POST.get('url')
    basePath = request.POST.get('server_type')
    fileGuId = ""

    # Checking clientId and privateKey
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample25.pt',
                                  { 'error' : 'You do not enter your User Id or Private Key' })
####Create Signer, ApiClient and Storage Api objects

#Create signer object
    signer = GroupDocsRequestSigner(privateKey)
#Create apiClient object
    apiClient = ApiClient(signer)
#Create Storage Api object
    storage = StorageApi(apiClient)
#Create AsyncApi object
    async = AsyncApi(apiClient)
#Create MergeApi object
    merg = MergeApi(apiClient)
#Create DocApi object
    doc = DocApi(apiClient)
#Check is base path entered
    if basePath == "":
        #If base path empty set base path to the dev server
        basePath = 'https://api.groupdocs.com/v2.0'
#Set base path for api
    storage.basePath = basePath
    async.basePath = basePath
    merg.basePath = basePath
    doc.basePath = basePath
#If user choose local file upload
    if inputFile.filename != "":

            #A hack to get uploaded file size
            inputFile.file.seek(0, 2)
            fileSize = inputFile.file.tell()
            inputFile.file.seek(0)

            fs = FileStream.fromStream(inputFile.file, fileSize)
            ####Make a request to Storage API using clientId
            try:

                #Upload file to current user storage
                upload = storage.Upload(clientId, inputFile.filename, fs)
                if upload.status == "Ok":
                    #Get file guid
                    fileGuId = upload.result.guid
            except Exception, e:
                return render_to_response('__main__:templates/sample25.pt',
                                          { 'error' : str(e) })
   #If user choose upload file from web
    if url != "":
        try:
            # Upload file to current user storage using entere URl to the file
            uploadWeb = storage.UploadWeb(clientId, url)
            # Check if file uploaded successfully
            if uploadWeb.status == "Ok":
                #Get file guid
                fileGuId = uploadWeb.result.guid
        except Exception, e:
            return render_to_response('__main__:templates/sample25.pt',
                { 'error' : str(e) })
    #If user choose file from GroupDocs
    if fileId != "":
        fileGuId = fileId

    try:
        #Get all fields from template
        fields = doc.GetTemplateFields(clientId, fileGuId)
        #Create Datasource object
        dataSource = Datasource
        #Create empty list
        fieldsList = []
        #Create list of values
        values = ["value1", "value2"]
        #Create DatasourceField object and set data to it
        for field in fields.result.fields:
            dataFieled = DatasourceField()
            dataFieled.name = field.name
            dataFieled.type = "text"
            dataFieled.values = values
            fieldsList.append(dataFieled)
        #Set Datasource fileds
        dataSource.fields = fieldsList

        try:
            #Add new Datasource to GroupDocs
            add = merg.AddDataSource(clientId, dataSource)

            try:
                #Merge new Datasource to document and convert document to pdf
                merge = merg.MergeDatasource(clientId, fileGuId, add.result.datasource_id, targetType = "pdf")

                i = 0
                counter = 5
                #Check job status
                while (i < counter):
                    time.sleep(5)
                    try:
                        #Get job info
                        jobInfo = async.GetJobDocuments(clientId, merge.result.job_id)
                        #If status Completed or Archived break loop
                        if jobInfo.result.job_status == "Completed" or jobInfo.result.job_status == "Archived":
                            break
                        #If job status Postponed return error
                        if jobInfo.result.job_status == "Postponed":
                            return render_to_response('__main__:templates/sample25.pt',
                                { 'error' : str(e) })
                    except Exception, e:
                        return render_to_response('__main__:templates/sample25.pt',
                            { 'error' : str(e) })
                    i = i + 1
                #Get guid and file name from job info
                guid = jobInfo.result.inputs[0].outputs[0].guid
                name = jobInfo.result.inputs[0].outputs[0].name

                #Obtaining file stream of downloading file and definition of folder where to download file
                currentDir = os.path.dirname(os.path.realpath(__file__))

                newpath = currentDir + "/../tmp/"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                #Downlaoding of file
                fs = storage.GetFile(clientId, guid)

                if fs:

                    filePath = newpath + name

                    with open(filePath, 'wb') as fp:
                        shutil.copyfileobj(fs.inputStream, fp)

                    message = 'File was downloaded to the <font color="blue">' + filePath + '</font> folder</font> <br />';
                    ### If request was successfull
                    #Generation of iframe URL using $pageImage->result->guid
                    #iframe to prodaction server
                    if basePath == "https://api.groupdocs.com/v2.0":
                        iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + guid
                    #iframe to dev server
                    elif basePath == "https://dev-api.groupdocs.com/v2.0":
                        iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + guid
                    #iframe to test server
                    elif basePath == "https://stage-api.groupdocs.com/v2.0":
                        iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + guid
                    elif basePath == "http://realtime-api.groupdocs.com":
                        iframe = 'http://realtime-apps.groupdocs.com/document-viewer/embed/' + guid
                    iframe = signer.signUrl(iframe)
                else:
                    raise Exception('Download file failed')
            except Exception, e:
                return render_to_response('__main__:templates/sample25.pt',
                    { 'error' : str(e) })

        except Exception, e:
            return render_to_response('__main__:templates/sample25.pt',
                { 'error' : str(e) })

    except Exception, e:
        return render_to_response('__main__:templates/sample25.pt',
            { 'error' : str(e) })





    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample25.pt',
                              { 'userId' : clientId,
                               'privateKey' : privateKey,
                               'iframe' : iframe,
                               'message' : message},
                              request=request)
