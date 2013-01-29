### This sample will show how to insert Assembly questionary into webpage

# Import of classes from libraries
from pyramid.renderers import render_to_response

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample16(request):

    fileId = request.POST.get('fileId')

    if IsNotNull(fileId) == False:
        return render_to_response('__main__:templates/sample16.pt',
                { 'error' : 'You do not enter all parameters' })

    # Construct iframe using fileId
    iframe = '<iframe src="https://apps.groupdocs.com/assembly2/questionnaire-assembly/' + fileId + '" frameborder="0" width="100%" height="600""></iframe>'

    # Set variables for template
    return render_to_response('__main__:templates/sample16.pt',
            {
            'fileId' : fileId,
            'iframe' : iframe,
            },
        request=request)