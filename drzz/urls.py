"""drzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from allauth.account.views import confirm_email

from rest_framework import routers
from users import views as users_views
from stores import views as stores_views
from courses import views as courses_views
from reviews import views as reviews_views
from drzz import views

from testapp import views as test_views

urlpatterns = [
    path('admin', admin.site.urls),

    #path('user/login', include('dj_rest_auth.urls')),
    # path('user/login', include('rest_auth.urls')),
    # path('user/regist', include('rest_auth.registration.urls')),
    # path('user', include('allauth.urls'))
    # path('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email')
    #path('user/login', include('users.urls')),
    
    path('user/create', users_views.user_create),
    path('user/<int:id>', users_views.user),
    path('user/<int:id>/courses', courses_views.course_list),
    path('user/<int:id>/course/<int:cid>', courses_views.course),
    path('user/<int:id>/muckets', users_views.mucket_list),
    path('user/<int:id>/friends', users_views.friend_list),
    path('user/<int:id>/reviews', users_views.review_list),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    path('stores', stores_views.store_list),
    path('stores/<str:keyword>', stores_views.store_search),
    path('stores/recommend/<int:uid>', stores_views.store_recommend),
    path('store/<int:id>', stores_views.store),
    path('store/<int:id>/reviews', reviews_views.review_list),
    path('store/<int:id>/review/<int:rid>', reviews_views.review),
    path('store/<int:id>/likes', stores_views.store_likes),
    path('store/<int:id>/like/<int:uid>', stores_views.store_like),

    path('reviews/update', reviews_views.score_update),
    #path('stores/update', reviews_views.store_score_update),

    path('tests', test_views.test_list ),
    path('test/<int:id>', test_views.test),

    #path('stores', stores_views.store)
    #path('google/login', users_views.google_login, name='google_login'),
    #path('google/callback', users_views.google_callback,      name='google_callback'),  
    #path('google/login/finish', users_views.GoogleLogin.as_view(), name='google_login_todjango'),
]
