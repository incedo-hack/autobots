from django import template
from predire.static.scripts.recruit_predict import recprec

register = template.Library()

@register.assignment_tag()
def getList():
    obj = recprec()
    return obj.html_load_json("data.json")