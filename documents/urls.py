from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(MainPage.as_view()), name='home'),
    path('document_detail/<slug:document_slug>', DetailDocument.as_view(), name='document_detail'),
    path('add/page/', AddDocument.as_view(), name="addpage"),
    path('add/cat/', AddCategoryView.as_view(), name="addcat"),
    path('delete/document/<slug:document_slug>', DeleteDocumentView.as_view(), name='delete_document'),
]