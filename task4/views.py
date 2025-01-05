from django.shortcuts import render
from django.views.generic import TemplateView


class PlatformTemplate(TemplateView):
    template_name = 'fourth_task/platform.html'


class CartTemplate(TemplateView):
    template_name = 'fourth_task/cart.html'


class CosmeticsTemplate(TemplateView):
    template_name = 'fourth_task/cosmetics.html'
    extra_context = {
        'cosmetics': ['Тушь для ресниц VIVIENNE SABO Grotesquee',
                      'Жидкая матовая помада с плампинг-эффектом VIVIENNE SABO Volummatte',
                      'Устойчивый гелевый карандаш для губ VIVIENNE SABO Le Grand volume', 'VIVIENNE SABO Tititint',
                      ' VIVIENNE SABO Палетка румян  Naturel']
    }
