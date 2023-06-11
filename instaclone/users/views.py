from django.http import HttpResponse

# Create your views here.
# index(request) request => HttpRequest
def index(request):
    message= f'{request.GET["my_favorite_color"]}'

    my_favorite_color = request.GET.get('my_favorite_color')
    if my_favorite_color:
        message = f'Your favorite color is {my_favorite_color}'
    else:
        message = 'You did not tell me your favorite color.'
        
    return HttpResponse(message)
