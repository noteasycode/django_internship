from .models import Country


def get_most_populous_countries(get_response):
    def middleware(request):
        countries = Country.objects.order_by('-population')[:10]
        response = get_response(request)
        print(f'10 most populous countries: {[country.name for country in countries]}')
        return response
    return middleware
