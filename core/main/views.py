from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Category, Shoos, Firm
# Create your views here.


class HomeView(ListView):
    model = Shoos
    template_name = 'home.html'
    ordering = ['-id']
    def get(self, request):
        categ = Category.objects.all()
        return render(request, self.template_name, {'categ':categ})

def CategoryView(request, cats):
    categorys = Shoos.objects.filter(category=cats)
    return render(request, 'home_detail.html',  {'cats':cats, 'categorys':categorys})
# class CategoryListView(ListView):
#     template_name = 'home.html'

#     def get(self, request):
#         categorys = Category.objects.all()
#         return render(request, self.template_name, {'categorys':categorys})

class CategoryListView(View):
    template_name = 'home.html'

    def get(self, request):
        categoryes = Category.objects.all()
        for cat in categoryes:
            shosse = Shoos.objects.filter(category_id = cat.id)
        return render(request, self.template_name, {'categoryes':categoryes, 'shosse':shosse})

# class CategoryDetailView(DetailView):
#     template_name = 'second.html'

#     def get(self, request, category_id):
#         shooss = Shoos.objects.get(category_id=category_id)
#         return render(request, self.template_name, {'shooss':shooss})