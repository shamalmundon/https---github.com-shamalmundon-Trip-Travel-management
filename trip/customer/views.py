from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from account.models import Tour,Popular

# Create your views here.


class HomeView(ListView):
    template_name = 'index.html'
    context_object_name = "tour"
    
    def get_queryset(self):
        return Tour.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popular"] = Popular.objects.all()
        return context

class GallaryView(TemplateView):
    template_name = 'gallary.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class PackageView(TemplateView):
    template_name = 'package.html'

class PopularView(TemplateView):
    template_name = 'popular.html'

class DetailView(DetailView):
    template_name = 'det.html'
    queryset = Tour.objects.all()
    pk_url_kwarg="id"
    context_object_name="tour"

class DetailedView(DetailView):
    model = Popular
    queryset = Popular.objects.all()
    pk_url_kwarg="pk"
    template_name = 'detail.html'
    context_object_name = 'popular'
    




