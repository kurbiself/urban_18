from django.shortcuts import render
from django.views.generic import TemplateView


class PlatformTemplate(TemplateView):
    template_name = 'third_task/platform.html'


class CartTemplate(TemplateView):
    template_name = 'third_task/cart.html'


class CosmeticsTemplate(TemplateView):
    template_name = 'third_task/cosmetics.html'
