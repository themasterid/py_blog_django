from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.simple_tag
def get_companion(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None
