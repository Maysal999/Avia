from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter


from .views import (
    PlaneViewSets,
    TicketViewSets,
    PassengerViewSet,
    AeroportViewSets,
    CityViewSets,
    TicketCreateAPIView,
    # TicketFilterApiView
    

)

router = DefaultRouter()
router.register(r'plane/list',PlaneViewSets)
router.register(r'ticket/list',TicketViewSets)
router.register(r'buy_ticket/list',PassengerViewSet)
router.register(r'aeroport/list',AeroportViewSets)
router.register(r'city/list',CityViewSets)


simple_router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'create_ticket/',TicketCreateAPIView.as_view(),name='ticket')
]
