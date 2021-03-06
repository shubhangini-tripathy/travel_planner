from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('travel/<int:pk>/', views.TravelDetailView.as_view(), name='travel_detail'),
    path('travel/new/', views.TravelCreateView.as_view(), name='travel_new'),
    path('travel/<int:pk>/edit/',
        views.TravelUpdateView.as_view(), name='travel_edit'),
    path('travel/<int:pk>/delete/',
        views.TravelDeleteView.as_view(), name='travel_delete'),

]
