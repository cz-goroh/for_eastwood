
from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


app_name = 'employee'
urlpatterns = [
    re_path(r'^$', views.index, name='index' ),
    path('list/', views.EmployeeList.as_view(), name = 'list'),
    re_path(r'^detail/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name = 'detail'),
    path('alfabet/',views.EmployeeAlfabet.as_view(), name = 'alfabet')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
