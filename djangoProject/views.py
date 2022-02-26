from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("겟으로")
        return render(request, "jaestagram/main.html")

    def post(self, request):
        print("포스트로")
        return render(request, "jaestagram/main.html")