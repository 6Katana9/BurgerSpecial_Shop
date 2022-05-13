from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.get_menu_list, name='menu'),
    path('adda/', views.create_or_update_product, name='adda'),
    path('menu/<int:pk>', views.NewDetailView.as_view(), name="menu_detail"),
    path('<int:pk>/update', views.NewUpdateView.as_view(), name="menu_update"),
    path('delete_menu/<int:id>/', views.delete_products, name='delete_menu' ),
]