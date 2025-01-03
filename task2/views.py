from django.shortcuts import render
from django.views.generic import TemplateView


def get_class(request):
    return render(request, 'second_task/class_template.html')


class GetFunc(TemplateView):
    template_name = 'second_task/func_template.html'
