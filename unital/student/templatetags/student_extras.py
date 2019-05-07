from django import template
from forum.models import *
from datetime import date, timedelta, datetime, timezone

register = template.Library()

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def replies(Question):
    return Reply.objects.filter(question = Question).order_by('posted_on')

@register.filter
def get_due_date_string(value):
    td = datetime.now(timezone.utc) - (value)
    days, hours, minutes = td.days, td.seconds // 3600, td.seconds // 60

    if days > 0:
        return str(days)    + ' days ago'

    if td.seconds < 60:
        return str(td.seconds) + ' sec. ago'
    elif minutes < 60:
        return str(minutes) + ' min. ago'
    else: # elif hours < 24:
        return str(hours)   + ' hours ago'
    # else:
    #     return str(days)    + ' days ago'