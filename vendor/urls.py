from django.urls import path
import vendor.views

urlpatterns = [
    path('apply/', vendor.views.create_vendor, name='create_vendor_route'),
    path('profile/', vendor.views.view_vendor_profile, name='view_vendor_profile_route')

]