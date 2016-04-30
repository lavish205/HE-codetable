from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Crypto.Hash import MD5
from .models import CodeUrls
import requests
# Create your views here.

class CodeView(APIView):

    def get(self, request, format=None):
        return render(request, 'index.html')

    def post(self, request, format=None):
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
        print context
        return render(request, 'index.html', context)

    def put(self, request, format=None):
        code = str(self.request.data.get('code'))
        lang = str(self.request.data.get('language'))
        print type(code), type(lang)
        code_snippet = CodeUrls.objects.create(code=code, lang=lang)
        code_snippet.url = str(int(MD5.new(str(code_snippet.id)).hexdigest(), 16) % (10 ** 8))
        code_snippet.save()
        response = {"url": code_snippet.url}
        return Response(response)


class CodeDetailView(APIView):

    def get(self, request, id, format=None):
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

