from django.conf.urls import url
from django.urls import path, include
from djoser.views import UserViewSet 

list_paths = UserViewSet.as_view({"post": "list"})
me_paths = UserViewSet.as_view({"get": "me", "put": "me","patch": "me","delete": "me",})
activation_path = UserViewSet.as_view({"post": "activation"})
resend_activation = UserViewSet.as_view({"post": "resend_activation"})
set_password = UserViewSet.as_view({"post": "set_password"})
reset_password = UserViewSet.as_view({"post": "reset_password"})
reset_password_confirm = UserViewSet.as_view({"post": "reset_password_confirm"})
set_email = UserViewSet.as_view({"post": "set_username"})
reset_email = UserViewSet.as_view({"post": "reset_username"})
reset_email_confirm = UserViewSet.as_view({"post": "reset_username_confirm"})

DJOSER_URLS = [
    path("users/", list_paths, name="user-list"),
    path("users/me/", me_paths, name="me-detail"),
    path("users/activation/", activation_path, name="user-activation"),
    path("users/resend_activation/",resend_activation,name="resend_activation"),
    path("users/set_password/",set_password,name="set_password"),
    path("users/reset_password/",reset_password,name="reset_password"),
    path("users/reset_password_confirm/",reset_password_confirm,name="reset_password_confirm"),
    path("users/set_email/",set_email,name="set_email"),
    path("users/reset_email/",reset_email,name="reset_email"),
    path("users/reset_email_confirm/",reset_email_confirm,name="reset_email_confirm"),
]

urlpatterns = [
    url(r'', include(DJOSER_URLS)),
]
