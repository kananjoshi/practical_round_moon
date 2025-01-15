from django.urls import path

from user_management.views import UserManagementViews


urlpatterns = [
    path('signup/', UserManagementViews.as_view({'post': 'signup'}), name='signup'),
    path('login/', UserManagementViews.as_view({'post': 'login'}), name='login'),
]
