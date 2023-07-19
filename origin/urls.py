from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
router.register('category', views.CategoryViewSet, basename='category')
router.register('subcategory', views.SubCategoryViewSet, basename='subcategory')
router.register('posts', views.PostViewSet, basename='posts')
router.register('contact', views.ContactViewSet, basename='contact')
router.register('introduce', views.IntroduceViewSet, basename='introduce')
router.register('tagfield', views.TagFieldViewSet, basename='tagfield')




urlpatterns = [
    path('admin/', admin_site.urls),
    # path('', views.index, name="index"),
    path('', include(router.urls)),

]

