from django import template

register = template.Library()


@register.filter
def media(data):
    if data:
        return f"/media/{data}"
    return "/static/img/image_cap.jpg"


@register.filter
def text(data):
    if data:
        return data
    return "Текст отсутствует"
