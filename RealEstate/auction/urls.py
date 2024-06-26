from django.urls import path
from . import views

urlpatterns = [
    path('', views.auction_list, name='auction_list'),
    path('auction/<int:pk>/', views.auction_detail, name='auction_detail'),
    path('create_auction/', views.create_auction, name='create_auction'),
    path('create_auction_data/<str:property_type>/', views.create_auction_data, name='create_auction_data'),
    path('auction/<int:pk>/bid/', views.place_bid, name='place_bid'),
    path('property/<int:property_id>/documents/', views.view_auction_property_documents, name='view_auction_property_documents'),
    path('property/<int:property_id>/property-details/', views.auc_property_detail, name = 'auc_property_detail'),
]
