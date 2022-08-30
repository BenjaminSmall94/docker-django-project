from django.urls import path
from .views import StuffList, StuffDetail, StuffUpdateDestroy, StuffCreate

urlpatterns = [
    path("view", StuffList.as_view(), name="stuff_list"),
    path("create", StuffCreate.as_view(), name="stuff_create"),
    path("view/<int:pk>/", StuffDetail.as_view(), name="stuff_detail"),
    path("update_delete/<int:pk>", StuffUpdateDestroy.as_view(), name="stuff_up_del"),
]
