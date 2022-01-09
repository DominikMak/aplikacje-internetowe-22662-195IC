from django.urls import path
from .views import HomePageView, find_element, search_id, FindIDView, FindClassView, examples
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', views.find_element, name='search_results'),
    path('search_id/', FindIDView.as_view(), name='search_id'),
    path('search_id_result/', views.search_id, name='search_results_id'),
    path('search_class/', FindClassView.as_view(), name='search_class'),
    path('search_class_result/', views.search_class, name='search_results_class'),
    path('lxml_XPath/', views.examples, name='random'),
]