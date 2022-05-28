from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Shoos, Firm
# Create your views here.


class CategoryListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        categorys = Category.objects.all()
        return render(request, self.template_name, {'categorys':categorys})


class CategoryDetailView(DetailView):
    template_name = 'second.html'

    def get(self, request, category_id):
        shooss = Shoos.objects.get(pk=category_id)
        return render(request, self.template_name, {'shooss':shooss})