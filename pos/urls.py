from django.urls import path
from pos import views
from rest_framework import routers
from pos import print_views

router = routers.DefaultRouter()
# router.register(r'unit',views.UnitViewSet, basename='unit'),

urlpatterns = [


# Home Page Before Login
   path('', views.home, name='home'),
# -------------------------------------------------------------------------
# Dashboard , POS
# -----------------------------------------------------------------------------
   path('dashboard/',views.dashboard, name='dashboard'),
   path('pos/',views.pos, name="pos"),
# -------------------------------------------------------------------------------
]