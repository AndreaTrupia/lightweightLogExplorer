from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from explorer.utils import list_files


# Create your views here.
def home(request: WSGIRequest):
    files = list_files("../observed")
    context: dict = {"files": files}
    file_name: str = request.GET.get("file_name")
    if file_name:
        with open(f"../observed/{file_name}", "r") as file:
            content = file.read()
            context["content"] = content
    return render(request, "home.html", context)