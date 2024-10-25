from django import template

register = template.Library()

@register.simple_tag
def render_json(data):
    """
    Renderiza JSON recursivamente. Dependiendo de si es dict, list o un valor,
    se renderiza con el template adecuado.
    """
    context = {"data": data}
    return context
