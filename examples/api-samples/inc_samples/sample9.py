import base64

from pyramid.renderers import render_to_response

# Sample 9
def sample9(request):
    fileGuId = request.POST.get('fileId')
    width = request.POST.get('width') or '300'
    height = request.POST.get('height') or '200'
    if fileGuId == None or fileGuId == '':
        return render_to_response('__main__:templates/sample9.pt', 
                                  { 'error' : 'You do not enter all parameters' })

    iframe_url = 'https://apps.groupdocs.com/document-viewer/embed/' + fileGuId + '?frameborder="0" width="' + width + '" height="' + height + '"'

    return render_to_response('__main__:templates/sample9.pt', 
                              { 
                               'iframe_url' : iframe_url,
                               'fileId' : fileGuId,
                               'width' : width,
                               'height' : height }, 
                              request=request)
