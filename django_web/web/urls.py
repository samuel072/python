#!/usr/bin/python3.5
# -*- coding utf-8

# web 包下面的url映射

from django.urls import path
from . import index

urlpatterns = [
    path("", index.index, name="index")
]
