from django.urls import path

from .views import SignUpView
from .views import UserList
from .views import ViewProfile,updateProfile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('explore/', UserList.as_view(), name='explore'),
    path('profile/<int:p_id>',ViewProfile,name='profile'),
    path('profile1/<int:p_id>',updateProfile,name='profile1')
]
