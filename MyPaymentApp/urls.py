from django.conf.urls import url
from .views import StoreDetails, MyPayment, home


urlpatterns = [
	url(r'^org$', StoreDetails.as_view(), name='org'),
    url(r'^payment$', MyPayment.as_view(), name='payment'),
    url(r'^$', home, name='home'),
	]
