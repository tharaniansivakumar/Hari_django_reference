from django.conf.urls import patterns , include , url

urlpatterns = patterns('workout.views',
url(r'^$', 'index', name='index'),
url(r'^userdet$', 'userdet', name='userdet'),
url(r'^showcolor/$', 'showcolor', name='showcolor'),
url(r'^login/$', 'login', name='login'),
url(r'^indexId/', 'indexId', name='indexId'),
url(r'^indexDish/', 'indexDish', name='indexDish'),
url(r'^indexAll/(?P<id>[0-9]+)/$', 'indexAll', name='indexAll'),
url(r'^indexAll/(?P<id>[\w]+)/(?P<attr>[\w]{0,4})/$', 'indexAll', name='indexAll'),
url(r'^indexAll/$', 'indexAll', name='indexAll'),
url(r'^indexCreate/', 'indexCreate', name='indexCreate'),
url(r'^orderid$', 'orderid', name='orderid'),
url(r'^product$', 'product', name='product'),
url(r'^product/(?P<name>[\w]+)$', 'product', name='product'),
url(r'^product/(?P<name>[\w]+)/(?P<id>[\d]+)$', 'product', name='product'),
url(r'^verify/', 'verify', name='verify'),
url(r'^delete/', 'delete', name='delete'),
url(r'^fileRead/', 'fileRead', name='fileRead'),

url(r'^fileDisp/', 'imageRes', name='imageRes'),
url(r'^pdf$','some_view', name='some_view'),
url(r'^party$','thirdparty', name='thirdparty'),
url(r'^parchild$','parchild', name='parchild'),
url(r'^manyparchild$','manyparchild', name='manyparchild'),

url(r'^forgetpassword$','forgetpassword', name='forgetpassword'),

url(r'^auth$','auth', name='auth'),
url(r'^logout$','logout', name='logout'),
url(r'^mail$','mail', name='mail'),

url(r'^verifytoken$','verifytoken', name='verifytoken'),

url(r'^readcsv$','readcsv', name='readcsv'),
url(r'^writecsv$','writecsv', name='writecsv'),
url(r'^writepdf$','writepdf', name='writepdf'),
url(r'^confirmpassword/(?P<mail>.*)/(?P<id>.*)$','confirmpassword', name='confirmpassword'),
)