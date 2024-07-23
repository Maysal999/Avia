import requests

from rest_framework.pagination import PageNumberPagination


class TicketBasePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5 

# def passenger_depth(request):
#     reques = r

#     if reques == 'GET':
#         return 2
#     else: 
#         return 0
