from django.urls import path
from . import views
urlpatterns = [
    path('',views.mission),
    path('',views.vision),

]
