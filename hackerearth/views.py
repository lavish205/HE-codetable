from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class CodeView(APIView):

    def get(self, request, format=None):
        return render(request, 'index.html')