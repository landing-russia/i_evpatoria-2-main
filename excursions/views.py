from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Excursion


def home(request):
    return render(request, 'excursions/index.html', {'section': 'excursions'})


class HomeExcursions(ListView):
    model = Excursion
    template_name = 'excursions/index.html'
    context_object_name = 'excursions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'excursions'
        return context


class ExcursionDetail(DetailView):
    model = Excursion
    template_name = 'excursions/detail.html'
    context_object_name = 'excursion'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'excursions'
        return context

