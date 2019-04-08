from django.conf.urls import url
from assets import views

app_name = 'assets'
urlpatterns = [
    url(r'^report/', views.report, name='report')
]
