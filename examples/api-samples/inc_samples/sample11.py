### This sample will show how programmatically create and post an annotation into document. How to delete the annotation

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample11(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileId = request.POST.get('file_id')
    annotationType = request.POST.get('annotation_type')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileId) == False or IsNotNull(annotationType) == False:
        return render_to_response('__main__:templates/sample11.pt',
                { 'error' : 'You do not enter all parameters' })

    #### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create Annotation object
    ant = AntApi(apiClient)

    # Delete annotation if Delete Button clicked
    if request.POST.get('delete_annotation') == "1":
        try:
            ant.DeleteAnnotation(clientId, request.POST.get('annotationId'))
        except Exception, e:
            return render_to_response('__main__:templates/sample11.pt',
                { 'error' : str(e) })

    # Required parameters
    allParams = ['box.x', 'box.y', 'text']

    # Added required parameters depends on  annotation type ['text' or 'area']
    if annotationType == "text":
        allParams = allParams + ['box.width', 'box.height', 'annotationPosition.x', 'annotationPosition.y', 'range.position', 'range.length']
    elif annotationType == "area":
        allParams = allParams + ['box.width', 'box.height']

    # Checking required parameters
    for param in allParams:
        needParam = request.POST.get(param)
        if IsNotNull(needParam) == False:
            return render_to_response('__main__:templates/sample11.pt',
                    { 'error' : 'You do not enter all parameters' })

    types = {'text' : "0", "area" : "1", "point" : "2"}

    # construct requestBody
    requestBody = {
        "type": types[request.POST.get('annotation_type')],
        "replies": [ { "text": request.POST.get('text') } ],
    }

    # construct requestBody depends on annotation type
    # text annotation
    if annotationType == "text":
        requestBody = dict(requestBody.items() + {
            "box": {
                "x"         : request.POST.get('box.x'),
                "y"         : request.POST.get('box.y'),
                "width"     : request.POST.get('box.width'),
                "height"    : request.POST.get('box.height')
            },
            "textRange":{
                "position"  : request.POST.get('range.position'),
                "length"    : request.POST.get('range.length')
            },
            "annotationPosition": {
                "x" : request.POST.get('annotationPosition.x'),
                "y" : request.POST.get('annotationPosition.y')
            },
        }.items())

    # area annotation
    elif annotationType == "area":
        requestBody = dict(requestBody.items() + {
            "box": {
                "x"         : request.POST.get('box.x'),
                "y"         : request.POST.get('box.y'),
                "width"     : request.POST.get('box.width'),
                "height"    : request.POST.get('box.height')
            },
            "annotationPosition": {
                "x" : "0",
                "y" : "0"
            },
        }.items())

    # point annotation
    elif annotationType == "point":
        requestBody = dict(requestBody.items() + {
            "box": {
                "x"         : request.POST.get('box.x'),
                "y"         : request.POST.get('box.y'),
                "width"     : "0",
                "height"    : "0"
            },
            "annotationPosition": {
                "x" : "0",
                "y" : "0"
            },
        }.items())

    try:
        # Make a request to Annotation API using clientId, fileId and requestBody
        response = ant.CreateAnnotation(clientId, fileId, requestBody)
    except Exception, e:
        return render_to_response('__main__:templates/sample11.pt',
            { 'error' : str(e) })

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample11.pt',
            { 'userId' : clientId,
              'privateKey' : privateKey,
              'file_Id' : fileId,
              'annotationType' : annotationType,
              'annotationText' : request.POST.get('text'),
              'annotationId' : response.result.annotationGuid,
              'status' : response.status
        },
        request=request)