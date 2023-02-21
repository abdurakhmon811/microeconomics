from django import template


register = template.Library()

@register.filter
def truncate(text, length):
    
    if len(text) <= length:
        return text[:int(length)]
    else:
        return f'{text[:int(length)]}...'
