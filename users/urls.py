from django.urls import path
from .views import MyProtectedView

urlpatterns = [
    path('protected/', MyProtectedView.as_view(), name='protected'),
]