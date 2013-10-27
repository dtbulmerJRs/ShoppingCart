from django.http import HttpResponse


def index(request):
    some_string = "Hello!"
    return HttpResponse(some_string)