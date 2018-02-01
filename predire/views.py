# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    name = request.GET.get('name')
    return render_to_response("index.html", { 'name' : name})

def score(request):
    return render_to_response("base-score.html")