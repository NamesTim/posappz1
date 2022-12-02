from django.http import HttpResponse
def about(request):
    context={
        'page-content':'content'
    }
    return HttpResponse(request,context)
