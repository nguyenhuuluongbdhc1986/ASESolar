from django.conf.urls import url
from .views import IndexClass1,IndexClass2,IndexClass3,IndexClass4,IndexClass5,IndexClass6,IndexClass7,IndexClass8,IndexClass9
app_name = 'home'
urlpatterns = [
    url(r'^u/', IndexClass1.as_view(),name='u'),
    url(r'^ppd/', IndexClass2.as_view(),name='ppd'),   
    url(r'^pout/', IndexClass3.as_view(),name='pout'),
    url(r'^ed/', IndexClass4.as_view(),name='ed'),
    url(r'^em/', IndexClass5.as_view(),name='em'),
    url(r'^ey/', IndexClass6.as_view(),name='ey'),
    url(r'^et/', IndexClass7.as_view(),name='et'),
    url(r'^ppy/', IndexClass8.as_view(),name='ppy'), 
    url(r'^i/', IndexClass9.as_view(),name='i')    
]