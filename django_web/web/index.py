#!/usr/bin/python3.5
# -*- coding utf-8

# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context["username"] = "kaiji"
    return render(request, "index.html", context)
