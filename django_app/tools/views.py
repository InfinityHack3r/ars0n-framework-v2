from django.http import Http404
from django.shortcuts import render

from .config import TOOLS, get_tool


def index(request):
    return render(request, "tools/index.html", {"tools": TOOLS})


def detail(request, slug: str):
    tool = get_tool(slug)
    if tool is None:
        raise Http404("Tool not found")
    return render(request, "tools/detail.html", {"tool": tool})
