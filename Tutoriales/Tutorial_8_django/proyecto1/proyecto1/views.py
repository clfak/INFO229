from django.http import HttpResponse

#definimos la primera vista 
def holamundo(request): 
    return HttpResponse("Hola mundo")
    