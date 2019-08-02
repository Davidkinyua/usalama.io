from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from products.models import Category
from products.models import Product



class CategoryListView(ListView):
    """ """
    model = Category
    context_object_name = "categories"


class CategoryDetailView(ListView):
    """ """
    template_name = 'product_catalog/category_detail.html'
    context_object_name = "product_list"
    paginate_by = PAGINATION

    def get_queryset(self, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.published.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
