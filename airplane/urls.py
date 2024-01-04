from django.urls import path

from airplane import views
urlpatterns = [
    path('', views.AirplaneView.as_view(), name="airplane-view"),
    path('<int:plane_id>', views.AirplaneView.as_view(), name="airplane-view"),

]

