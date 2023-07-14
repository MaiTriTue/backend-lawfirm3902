from rest_framework.serializers import ModelSerializer
from .models import User, Category, SubCategory, Posts, Contact, Introduce, TagField


class TagFieldSerealizer(ModelSerializer):
    class Meta:
        model = TagField
        fields = ["id", "name"]

class UserSerealizer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "avatar", "position", "field", "experience", "level", "phone", "tagsField"]

    tagsField = TagFieldSerealizer(many=True)

class CategorySerealizer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name" ]


class SubCategorySerealizer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "name" ]


class PostSerealizer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "title", "disc", "image", "created_date", "updated_date", "active", "content", "file_upload", "subcategory" ]


class ContactSerealizer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "area", "address", "phone", "email"]


class IntroductSerealizer(ModelSerializer):
    class Meta:
        model = Introduce
        fields = ["id", "name", "manager", "content"]








