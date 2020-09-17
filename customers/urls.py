from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from customers import views
from .views import CustomerViewSet


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet),
# urlpatterns = router.urls

urlpatterns = [
    url(r'^api/customers/$', views.customer_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.customer_detail)
    # path('<int:id>/delete/', views.deleteById),
    # path('<int:id>/update', views.update),
    # path(r'', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
]
