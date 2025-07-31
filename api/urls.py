from django.urls import path
from .views import calculate_sum

urlpatterns = [
    path('sum', calculate_sum, name='calculate_sum'),
]
'''
from django.urls import path
from .views import SumAPIView

urlpatterns = [
    path('sum/', SumAPIView.as_view(), name='sum-api'),
]
'''