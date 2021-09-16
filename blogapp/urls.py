from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='hm'),
    path('delete/<int:blogid>', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

]
