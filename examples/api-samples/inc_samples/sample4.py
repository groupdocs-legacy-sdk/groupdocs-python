####<i>This sample will show how to use <b>GetFile</b> method from Storage Api to download a file from GroupDocs Storage</i>

#Import of classes from libraries
import base64
import os
import shutil
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample4(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    
    file_id = request.POST.get('fileId')
    # Checking clientId, privateKey and file_Id
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(file_id) == False:
        return render_to_response('__main__:templates/sample4.pt', 
                                  { 'error' : 'You do not enter all parameters' })

    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    api = StorageApi(apiClient)

    ####Make a request to Storage API using clientId

    try:
        #Obtaining all Entities from current user
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        #Selecting file names
        for item in files.result.files: #selecting file names
            #Obtaining file name for entered file Id
           if item.guid == file_id:
               fileName = item.name

        ####Make a request to Storage Api for dowloading file

        #Obtaining file stream of downloading file and definition of folder where to download file
        currentDir = os.path.dirname(os.path.realpath(__file__))
        
        newpath = currentDir + "/../tmp/"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        #Downlaoding of file
        fs = api.GetFile(clientId, file_id);

        if fs:

            filePath = newpath + fileName
        
            with open(filePath, 'wb') as fp:
                shutil.copyfileobj(fs.inputStream, fp)
            
            message = '<font color="green">File was downloaded to the <font color="blue">' + filePath + '</font> folder</font> <br />';
        else:
			raise Exception('Wrong file ID!')
    except Exception, e:
        return render_to_response('__main__:templates/sample4.pt', 
                                  { 'error' : str(e) })
    #If request was successfull - set message variable for template
    return render_to_response('__main__:templates/sample4.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'file_Id' : file_id, 
                               'message' : message },
                              request=request)
