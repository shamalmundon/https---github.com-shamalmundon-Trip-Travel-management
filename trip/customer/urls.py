from django.urls import path
from .views import *

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('gallary',GallaryView.as_view(),name='gallary'),
    path('contact',ContactView.as_view(),name='contact'),
    path('package',PackageView.as_view(),name='package'),
    path('popular',PopularView.as_view(),name='popular'),
    path('Det/<int:id>',DetailView.as_view(),name='Det'),
    path('popular/<int:pk>/', DetailedView.as_view(), name='popular_detail'),
]