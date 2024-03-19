from django.urls import path

from counter import views
from counter.views import CounterListView

urlpatterns = [
    path('', CounterListView.as_view(), name='index'),
    path('update', views.update, name='update'),
]