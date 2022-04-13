from django.urls import path
from .views import TestViewAdmin, TestViewAll, TestViewUser
urlpatterns = [
    path('admin/', TestViewAdmin.as_view()), 
    path('user/', TestViewUser.as_view()),
    path('all/',TestViewAll.as_view())
]