"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from website.views import *
from django.urls import include, path
from django.conf import settings
'''
urlpatterns = [
    path('website/',include('website.urls')),
    path('vision/',include('Vision.urls')),
    path('mission/',include('Mission.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
'''

urlpatterns = [
    path('',front_page),
    path('website/',include('website.urls')),
    path('admin/', admin.site.urls),
    path('principal_desk/',get_principal_desk),
#   path('disp/',base_fet),
    path('mission/',get_mission),
    path('vision/',get_vision),
    path('goals/',get_goals),
    path('history/',get_history),
    path('campus/',get_campus),
    path('balance_sheets/',get_bsheets),
    path('get_stat_bog/',get_stat_bog),
    path('get_stat_AC/',get_stat_AC),
    path('get_stat_BOS/',get_stat_BOS),
    path('get_non_stat/',get_non_stat),
    path('get_stat_FC/',get_Finance_Committe),
    path('get_Cultural_Committee_desc/',Cultural_Committee_page),
    path('get_Cultural_Committee_achv/',Cultural_Committee_Achievements_page),
    path('Members_of_Examination_Branch_input/',Members_of_Examination_Branch_get_page),
    path('Software_Automation_Committee_Input/', Software_Automation_Committee_get_page),
    path('Supporting_Staff_Input/',Supporting_Staff_get_page),
    path('Roll_of_Honour_input/',Roll_of_Honour_get_page),
#   path('front/',base_fet),
    path('display/<int:pgid>/',frontend_views),
]

if settings.DEBUG:
         from django.conf.urls.static import static
         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

