from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path("feature/", FeatureView.as_view(), name='feature'),
    path("team/", TeamView.as_view(), name='team'),
    path("menu/", MenuView.as_view(), name='menu'),
    path("category/<int:cat_id>/", CategoryView.as_view(), name='category'),
    path("booking/", BookingView.as_view(), name='booking'),
    path("order/", OrderView.as_view(), name='order'),
    path("blog/", BlogView.as_view(), name='blog'),
    path("detail/<int:id>/", DetailBlog.as_view(), name='detail'),
    path("search/<int:id>/", DetailBlog.as_view(), name="search"),
    path("comment/<int:id>/", CommentView.as_view(), name="comment"),
    path("register/", register_1, name='register'),
    path("login/", login_user, name='login'),
    path("logout/", log_out, name='logout'),
    path("contact/", ContactView.as_view(), name='contact'),
]