from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, Category, SubCategory, Posts, Contact, Introduce, TagField
from .serializers import UserSerealizer, CategorySerealizer, SubCategorySerealizer, PostSerealizer, ContactSerealizer, IntroductSerealizer, TagFieldSerealizer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerealizer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerealizer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerealizer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerealizer

    def list(self, request, *args, **kwargs):
        posts = Posts.objects.filter(active=True)
        serializer = PostSerealizer(posts, many=True)

        return Response(data=serializer.data)

    def retrieve(self, request, pk):
        try:
            post = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404("No MyModel matches the given query.")



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerealizer


class IntroduceViewSet(viewsets.ModelViewSet):
    queryset = Introduce.objects.all()
    serializer_class = IntroductSerealizer


class TagFieldViewSet(viewsets.ModelViewSet):
    queryset = TagField.objects.all()
    serializer_class = TagFieldSerealizer

def index(request):
    return render(request, template_name="index.html", context={
        'name': "Mai tri Tue"
    })

