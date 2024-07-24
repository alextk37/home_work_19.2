from django import template

register = template.Library()


@register.filter
def media(data):
    if data:
        return f"/media/{data}"
    return "/static/img/image_cap.jpg"
