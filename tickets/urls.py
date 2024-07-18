from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter


from .views import (
    PlaneViewSets,
    TicketViewSets,
    BagViewSets,
    PassengerViewSet,
    AeroportViewSets,
    CityViewSets,
    TicketFilterApiView
    

)

router = DefaultRouter()
router.register(r'plane/list',PlaneViewSets)
router.register(r'bag/list',BagViewSets)
router.register(r'ticket/list',TicketViewSets)
router.register(r'buy_ticket/list',PassengerViewSet)
router.register(r'aeroport/list',AeroportViewSets)
router.register(r'city/list',CityViewSets)
# router.register(r'tl_filter/',TicketFilterApiView)

simple_router = SimpleRouter()
# simple_router.register('tlfilter/',TicketFilterApiView)
# router.register(r'city1/list',Cit1ViewSets)

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(simple_router.urls)),


    path(r'ticket_filter/',TicketFilterApiView.as_view(),name='ticket')
]
