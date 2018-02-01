# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response

from predire.static.scripts.recruit_predict import recprec

# Create your views here.
def index(request):
    name = request.GET.get('name')
    return render_to_response("index.html", {'name':name})

def dashboard(request):
    dict = {}
    obj = recprec()
    switch = obj.get_switch()
    for val in switch:
        desc, weight = val.split("|")
        switch = request.GET.get(desc)
        if switch == "on":
            dict[desc] = weight
    calc_weight = obj.calc_weight_switch(dict)
    return render_to_response("dashboard.html", {'weight':calc_weight})
