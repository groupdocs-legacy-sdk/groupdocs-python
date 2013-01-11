from pyramid.renderers import render_to_response

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 16
def sample16(request):

    fileId = request.POST.get('file_id')

    if IsNotNull(fileId) == False:
        return render_to_response('__main__:templates/sample16.pt',
                { 'error' : 'You do not enter all parameters' })

    iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/embed/' + fileId + '" frameborder="0" width="720" height="600""></iframe>'

    return render_to_response('__main__:templates/sample16.pt',
            {
            'fileId' : fileId,
            'iframe' : iframe,
            },
        request=request)