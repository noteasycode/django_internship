from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse('Главная страница')


def redirect(request):
    return HttpResponseRedirect('https://onix.kr.ua/')


def exponentiation(request, pk):
    result = pk**2
    return HttpResponse(f'Число {pk} возведенное во вторую степень будет равно: {result}.')
