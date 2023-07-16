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
    TagField.objects.get_or_create(name="Dân sự")
    TagField.objects.get_or_create(name="Hình sự")
    TagField.objects.get_or_create(name="Hôn nhân")
    TagField.objects.get_or_create(name="Đất đai")
    TagField.objects.get_or_create(name="Doanh nghiệp")
    TagField.objects.get_or_create(name="Sở hữu trí tuệ")
    TagField.objects.get_or_create(name="Lao động")
    TagField.objects.get_or_create(name="Đấu thầu")
    TagField.objects.get_or_create(name="Hành chính")


    # Category.objects.get_or_create(name="DỊCH VỤ LUẬT SƯ", slug="dich-vu-luat-su")
    # Category.objects.get_or_create(name="TƯ VẤN PHÁP LUẬT", slug="tu-van-phap-luat")
    # Category.objects.get_or_create(name="VĂN BẢN PHÁP LUẬT", slug="van-ban-phap-luat")
    # Category.objects.get_or_create(name="BIÊU MẪU", slug="bieu-mau")
    # Category.objects.get_or_create(name="GIÁO DỤC", slug="giao-duc")


    # cate = Category.objects.get(pk=2)
    # SubCategory.objects.create(name="Tư vấn luật doanh nghiệp", slug="tu-van-luat-doanh-nghiep",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật lao động", slug="tu-van-luat-lao-dong",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật sở hữu trí tuệ", slug="tu-van-luat-so-huu-tri-tue",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật dân sự", slug="tu-van-luat-dan-su",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật đất đai", slug="tu-van-luat-dat-dai",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật bảo hiểm xã hội", slug="tu-van-luat-bao-hiem-xa-hoi",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật hành chính", slug="tu-van-luat-hanh-chinh",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật nghĩa vụ quân sự", slug="tu-van-luat-nghia-vu-quan-su",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật cạnh tranh", slug="tu-van-luat-canh-tranh",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật giáo dục", slug="tu-van-luat-giao-duc",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật đầu tư", slug="tu-van-luat-dau-tu",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật thuế", slug="tu-van-luat-thue",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật hình sự", slug="tu-van-luat-hinh-su",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật thừa kế", slug="thua-ke",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật hôn nhân", slug="tu-van-luat-hon-nhan",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật giao thông", slug="tu-van-luat-giao-thong",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật đấu thầu", slug="tu-van-luat-dau-thau",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật chứng khoán", slug="tu-van-luat-chung-khoan",  category=cate)
    # SubCategory.objects.create(name="Tư vấn luật môi trường", slug="tu-van-luat-moi-truong",  category=cate)
    # SubCategory.objects.create(name="Từ điển pháp luật", slug="tu-dien-phap-luat",  category=cate)




    # if not User.objects.filter(is_superuser=True).first():
    #     # user = User.objects.filter(is_superuser=True).first()
    #     # user.delete()
    #     user = User.objects.create(
    #         username='admin',
    #         email='luatsuhuyvinh@gmail.com',
    #         is_superuser=True,
    #
    #     )
    #     user.set_password('huyvinh1986')
    #     user.save()

    return render(request, template_name="index.html", context={
        'name': "Mai tri Tue"
    })


