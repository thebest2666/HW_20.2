from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, ProductDetailView, ContactTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="product"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
