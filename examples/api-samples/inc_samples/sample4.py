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

# Sample 4
def sample4(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    
    file_id = request.POST.get('file_id')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(file_id) == False:
        return render_to_response('__main__:templates/sample4.pt', 
                                  { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)
               
    try:
        
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        for item in files.result.files: #selecting file names
           if item.guid == file_id:
               fileName = item.name
               
        currentDir = os.path.dirname(os.path.realpath(__file__))
        
        newpath = currentDir + "/../tmp/"
        if not os.path.exists(newpath):
            os.makedirs(newpath)   
         
        fs = api.GetFile(clientId, file_id);

        if fs:
            #~ import pdb;  pdb.set_trace()
            filePath = newpath + fileName
        
            with open(filePath, 'wb') as fp:
                shutil.copyfileobj(fs.inputStream, fp)
            
            massage = '<font color="green">File was downloaded to the <font color="blue">' + filePath + '</font> folder</font> <br />';
        else:
			raise Exception('Wrong file ID!')
    except Exception, e:
        return render_to_response('__main__:templates/sample4.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample4.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'file_Id' : file_id, 
                               'massage' : massage }, 
                              request=request)
