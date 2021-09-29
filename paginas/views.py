# TemplateView para criar páginas simples
from django.views.generic import TemplateView


# Classe IndexView "extends" TemplateView
class IndexView(TemplateView):
    template_name = 'paginas/base.html'


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
