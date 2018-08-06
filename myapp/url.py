from django.conf.urls import patterns , include , url

urlpatterns = patterns('myapp.views',
                       url(r'^$', 'index', name='index'),
    url(r'^hello1/','hello1',name='hello1'),
    url(r'^hello/','hello',name='hello'),
url(r'^crudops/','crudops',name='crudops'),
#url(r'^addDet/','addDet',name='addDet'),
url(r'^insert/','insert',name='insert'),
url(r'^display/','display',name='display'),
url(r'^update/','update',name='update'),
#url(r'^display/(?P<user_id>[0-9]+)/$','displayAll',name='displayAll'),
url(r'^js/','js',name='js'),
)