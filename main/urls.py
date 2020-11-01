from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add,name='add'),
    # path('update/',views.update ),
    #path('update/<int:pk>/', views.update, name="update"),
    path('update/<int:item_id>/', views.update, name="update"),
]
