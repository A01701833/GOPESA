from django.urls import path
from principal import views
from django.conf.urls import url
#------------------------------------------ END OF IMPORTING LIBRARIES ------------------------------

# APPLICATION NAME

app_name = 'principal'

# URL PATTERNS FOR APPLICATION "PRINCIPAL"
urlpatterns =[
    path('',views.index,name='index'),
    path('properties/',views.properties,name='properties'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('properties/<int:id>/<slug:slug>',views.properties_detail, name="properties_detail")
]
#------------------------------------------ END OF URLS ------------------------------
