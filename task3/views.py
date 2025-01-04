from django.shortcuts import render
from django.views.generic import TemplateView


class PlatformTemplate(TemplateView):
    template_name = 'third_task/platform.html'


class CartTemplate(TemplateView):
    template_name = 'third_task/cart.html'


class CosmeticsTemplate(TemplateView):
    template_name = 'third_task/cosmetics.html'
    extra_context = {
        'title': 'Каблучки макияж',
        'mascara': 'Тушь для ресниц VIVIENNE SABO Grotesquee',
        'pomade': 'Жидкая матовая помада с плампинг-эффектом VIVIENNE SABO Volummatte',
        'pencil': 'Устойчивый гелевый карандаш для губ VIVIENNE SABO Le Grand volume',
        'tint': 'VIVIENNE SABO Tititint',
        'blush': ' VIVIENNE SABO Палетка румян  Naturel',
    }
