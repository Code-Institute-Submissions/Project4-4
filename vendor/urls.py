from django.urls import path
import vendor.views
import food.views

urlpatterns = [
    path('apply/', vendor.views.create_vendor, name='create_vendor_route'),
    path('profiles', vendor.views.view_vendor_profiles, name='view_vendor_profiles_route'),
    path('profiles/<vendor_profile_id>', vendor.views.edit_vendor_profile, name='edit_vendor_profile_route'),
    path('profiles/delete/<vendor_profile_id>', vendor.views.delete_vendor_profile, name='delete_vendor_profile_route'),
    path('profiles/<vendor_profile_id>/delivery_area', vendor.views.create_delivery_area, name='create_delivery_area_route'),
    path('profiles/<vendor_profile_id>/delivery_area/remove_town_vendor/<town_vendor_id>', vendor.views.remove_town_vendor, name='remove_town_vendor_route'),
    path('profiles/<vendor_profile_id>/delivery_area/remove_postal_vendor/<postal_vendor_id>', vendor.views.remove_postal_vendor, name='remove_postal_vendor_route'),
    path('profiles/<vendor_profile_id>/food_gallery', food.views.view_vendor_food_gallery, name='view_vendor_food_gallery_route'),
    path('profiles/<vendor_profile_id>/food_gallery/add_food', food.views.add_vendor_food, name='add_vendor_food_route'),
    path('profiles/<vendor_profile_id>/food_gallery/edit/<vendor_food_id>', food.views.edit_vendor_food, name='edit_vendor_food_route'),
    path('profiles/<vendor_profile_id>/food_gallery/delete/<vendor_food_id>', food.views.delete_vendor_food, name='delete_vendor_food_route'),
    path('profiles/<vendor_profile_id>/orders', vendor.views.view_vendor_orders, name='view_vendor_orders_route')

]