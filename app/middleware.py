# translator/middleware.py
from django.utils.translation import activate


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Target language is on processing to convert")
        language_code = request.session.get('language', 'en')
        activate(language_code)
        response = self.get_response(request)
        print("Now it's converted")
        return response
