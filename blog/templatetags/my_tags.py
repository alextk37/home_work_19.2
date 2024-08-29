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


@register.filter
def no_name(data):
    if data:
        return data
    return "Юзер"


@register.filter
def no_avatar(data):
    if data:
        return f"/media/{data}"
    return "/static/img/no_avatar.jpg"


@register.filter
def is_in_group(user, group):
    return user.groups.filter(name=group).exists()
