from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('engineers/', views.EngineerListView.as_view(), name='engineers'),
    path('engineer/<int:pk>', views.EngineerDetailView.as_view(), name='engineer-detail'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('team/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]

#add, update, delete engineers
urlpatterns +=[
    path('engineers/create/', views.EngineerCreate.as_view(), name='engineer_create'),
    path('engineer/<int:pk>/update/', views.EngineerUpdate.as_view(), name='engineer_update'),
    path('engineer/<int:pk>/delete/', views.EngineerDelete.as_view(), name='engineer_delete')
]

#add, update, delete teams
urlpatterns +=[
    path('teams/create/', views.TeamCreate.as_view(), name='team_create'),
    path('team/<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
    path('team/<int:pk>/delete/', views.TeamDelete.as_view(), name='team_delete')
]

#add, update, delete products
urlpatterns +=[
    path('products/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete')
]

urlpatterns +=[
    path('advice/', views.advice, name='advice'),
    path('advice/add/', views.add, name='add'),
    path('techtalk/', views.techtalk, name='techtalk'),
    path('resource/', views.resource, name='resource'),
]
