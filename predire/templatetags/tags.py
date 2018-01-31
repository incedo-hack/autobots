from django import template

from predire.static.scripts.recruit_predict import recprec

register = template.Library()

@register.assignment_tag()
def genList(arg1, arg2):
    return "response"