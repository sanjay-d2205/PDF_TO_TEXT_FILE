from django.conf.urls import url
from . import views
urlpatterns = [
 url('',views.index,name="index"),
 url('textFileConverter',views.textFileConverter,name="textFileConverter"),
 url('export_text_file', views.export_text_file, name='export_text_file'),
]