from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class CatalogListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/catalog_detail.html"


class ContactTemplateView(TemplateView):
    template_name = "contacts.html"

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"{name} {phone} {message}")
        return render(request, "contacts.html")
