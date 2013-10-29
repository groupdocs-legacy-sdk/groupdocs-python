####<i>This sample will show how to convert several HTML documents to PDF and merge them to one document</i>

#Import of classes from libraries
import base64
import os
import shutil
import random
import time

from pyramid.renderers import render_to_response
from groupdocs.StorageApi import StorageApi
from groupdocs.AsyncApi import AsyncApi
from groupdocs.ApiClient import ApiClient
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner
from groupdocs.models.JobInfo import JobInfo

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample33(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    firstUrl = request.POST.get('url1')
    secondUrl = request.POST.get('url2')
    thirdUrl = request.POST.get('url3')
    basePath = request.POST.get('server_type')
    message = ""
    iframe = ""
    # Checking clientId, privateKey and file_Id
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample33.pt',
                                  { 'error' : 'You do not enter all parameters' })

    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    storageApi = StorageApi(apiClient)
    #Create Async api object
    asyncApi = AsyncApi(apiClient)
    #Set base Path
    if basePath == "":
        basePath = "https://api.groupdocs.com/v2.0"
    storageApi.basePath = basePath
    asyncApi.basePath = basePath
    #Create list of URL's
    urlList = [firstUrl, secondUrl, thirdUrl]
    #Create empty list for uploaded files GUID's
    guidList = []
    for url in urlList:
        try:
            #Upload file
            upload = storageApi.UploadWeb(clientId, url)
            if upload.status == "Ok":
                #Add GUID of uploaded file to list
                guidList.append(upload.result.guid)
            else:
                raise Exception(upload.error_message)
        except Exception, e:
            return render_to_response('__main__:templates/sample33.pt',
                { 'error' : str(e) })
    ####Make a request to Signature API using clientId
    try:
        #Create list of result document type
        convertType = []
        convertType.append("pdf")
        #Create JobInfo object and set attributes
        jobInfo = JobInfo()
        jobInfo.actions = "convert, combine"
        jobInfo.out_formats = convertType
        jobInfo.status = "-1"
        jobInfo.email_results = True
        rand = random.randint(0, 500)
        jobInfo.name = "test" + str(rand)
        #Create job
        createJob = asyncApi.CreateJob(clientId, jobInfo)
        if createJob.status == "Ok":
            for guid in guidList:
                try:
                    #Add all uploaded files to created job
                    addJobDocument = asyncApi.AddJobDocument(clientId, createJob.result.job_id, guid, False)
                    if addJobDocument.status != "Ok":
                        raise Exception(addJobDocument.error_message)
                except Exception, e:
                    return render_to_response('__main__:templates/sample33.pt',
                        { 'error' : str(e) })
            #Change job status
            jobInfo.status = "0"
            try:
                #Update job with new status
                updateJob = asyncApi.UpdateJob(clientId,createJob.result.job_id, jobInfo)
                if updateJob.status == "Ok":
                    time.sleep(5)
                    try:
                        #Get result file from job by it's ID
                        getJobDocument = asyncApi.GetJobDocuments(clientId, createJob.result.job_id)

                        if getJobDocument.status == "Ok":
                            fileGuid = getJobDocument.result.outputs[0].guid
                            #Generation of iframe URL using $pageImage->result->guid
                            #iframe to prodaction server
                            if basePath == "https://api.groupdocs.com/v2.0":
                                iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + fileGuid
                            #iframe to dev server
                            elif basePath == "https://dev-api.groupdocs.com/v2.0":
                                iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + fileGuid
                            #iframe to test server
                            elif basePath == "https://stage-api.groupdocs.com/v2.0":
                                iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + fileGuid
                            elif basePath == "http://realtime-api.groupdocs.com":
                                iframe = 'http://realtime-apps.groupdocs.com/document-viewer/embed/' + fileGuid
                            iframe = signer.signUrl(iframe)

                        else:
                            raise Exception(getJobDocument.error_message)
                    except Exception, e:
                        return render_to_response('__main__:templates/sample33.pt',
                            { 'error' : str(e) })
                else:
                    raise Exception(updateJob.error_message)
            except Exception, e:
                return render_to_response('__main__:templates/sample33.pt',
                    { 'error' : str(e) })
        else:
            raise Exception(createJob.error_message)
    except Exception, e:
        return render_to_response('__main__:templates/sample33.pt',
            { 'error' : str(e) })

    #If request was successfull - set message variable for template
    return render_to_response('__main__:templates/sample33.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey,
                               'url1' : firstUrl,
                               'url2' : secondUrl,
                               'url3' : thirdUrl,
                               'iframe' : iframe,
                               'message' : message },
                              request=request)
