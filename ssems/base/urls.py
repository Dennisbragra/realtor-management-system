from django.urls import path, include
from . import views



urlpatterns = [
    path('home/', views.homeView, name="home"),
    path('houses/', views.mainView, name="houses"),

    path('requestunit<str:pk>/', views.requestUnit, name="requestunit"),
    path('unitsrequested/', views.unitRequested, name="requestedunits"),
    path('approverequest<str:pk>/', views.approveRequest, name="approverequest"),




    path('addunit/', views.addunitView, name="addunit"),
    path('update<str:pk>/', views.updateunitView, name="updateunit"),
    path('viewunit<str:pk>/', views.viewUnit, name="viewunit"),



    path('viewtopic<str:pk>/', views.viewTopic, name="viewtopic"),
    path('noticeboard/', views.noticeBoard, name="noticeboard"),
    path('addnotice/', views.addNotice, name="addnotice"),

    path('rentarrears/', views.rentArrears, name="rentarrears"),
    path('reviews/', views.reviewsView, name="reviews"),



    path('maintenance<str:pk>/', views.maintenanceView, name="maintenance"),  
    path('checkrequests/', views.maintenanceRequestView, name="maintenance-requests"),
    path('repairupdates<str:pk>/', views.updateMaintenanceView, name="repairupdates"),
    


]