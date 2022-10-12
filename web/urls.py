from django.urls import path
from web.views import index, GoodListView
urlpatterns = [
    path('', GoodListView.as_view(), name='home')
]