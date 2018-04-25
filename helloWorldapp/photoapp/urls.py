from django.conf.urls import url
from photoapp import views

urlpatterns = [
    url(r'^index/$', views.indexPage, name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    # url(r'^index/', views.index, name='index'),
    url(r'^uploadPhoto/$', views.uploadPhoto, name='uploadPhoto'),
    url(r'^comments_upload/$', views.comments_upload, name='comments_upload'),
    url(r'^$', views.testAjax, name='testAjax'), # Notice the URL has been named
]