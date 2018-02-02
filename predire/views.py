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
    id_mapping = {}
    obj = recprec()
    id = request.GET.get('id')
    submit = request.GET.get('submit')

    mapping_desc = obj.get_switch()

    for val in mapping_desc:
        desc, weight = val.split("|")
        print desc + "|" + str(weight)

        switch = request.GET.get(desc)
        if desc == "radio":
            desc = switch
            switch = "on"
            dict[desc] = weight

        if switch == "on":
            dict[desc] = weight

    calc_weight, id_name, id_mapping = obj.calc_weight_switch(dict, id, submit)
    for key in id_mapping:
        if id_mapping[key] == "on":
            id_mapping[key]= "checked"

    print calc_weight
    # if calc_weight > 100:
    #     calc_weight= 100

    id_mapping["weight"]= calc_weight
    id_mapping["name"] = id_name
    id_mapping["id"]= id

    return render_to_response(
        "dashboard.html",
        id_mapping
    )
