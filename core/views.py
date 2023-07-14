from django.shortcuts import render
from django.views.generic import TemplateView

# Index
class IndexView(TemplateView):
    template_name = 'index.html'
