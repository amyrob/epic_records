from django.http import HttpResponse

def index(request):
    return HttpResponse("Homepage - Welcome to Epic Records")

def about(request):
    return HttpResponse("about epic")
