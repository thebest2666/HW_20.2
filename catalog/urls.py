from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", product, name="product"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
]
