from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Crypto.Hash import MD5
from .models import CodeUrls
import requests
# Create your views here.


class CodeView(APIView):
    """
    API Endpoint for compile and run
    """
    def get(self, request, format=None):
        """
        render index template for codetable
        :param request: request object
        :param format: json
        :return: template page of codetable
        """
        return render(request, 'index.html')

    def post(self, request, format=None):
        """
        compile and run give code w.r.t language and optional input
        :param request: request object
        :param format: json
        :return: render template with compilation message
        """
        code = self.request.data.get('code')
        lang = self.request.data.get('language')
        custom_input = self.request.data.get('custominput')
        url = "https://api.hackerearth.com/v3/code/run/"
        params = {
            'client_secret': '3e61f5064b89df8d0fc96baba4531be02a766bef',
            'source': code,
            'lang': lang
        }
        if custom_input:
            params['input'] = custom_input

        r = requests.post(url, data=params)
        context = r.json()
        return render(request, 'index.html', context)

    def put(self, request, format=None):
        """
        Generate public url of code snippet
        :param request: request object
        :param format: json
        :return: public url
        """
        code = str(self.request.data.get('code'))
        lang = str(self.request.data.get('language'))
        print type(code), type(lang)
        code_snippet = CodeUrls.objects.create(code=code, lang=lang)
        code_snippet.url = str(int(MD5.new(str(code_snippet.id)).hexdigest(), 16) % (10 ** 8))
        code_snippet.save()
        response = {"url": code_snippet.url}
        return Response(response)


class CodeDetailView(APIView):
    """
    API Endpoint for public url code snippet
    """
    def get(self, request, id, format=None):
        """
        render template with pre filled code
        :param request: request object
        :param id: url hash
        :param format: json
        :return: render template with pre filled code
        """
        try:
            code_snippet = CodeUrls.objects.get(url=id)
            context = {
                'code': code_snippet.code,
                'language': code_snippet.lang
            }
            return render(request, 'index.html', context)
        except CodeUrls.DoesNotExist:
            print "Not Found"
            return Response(status=404)

