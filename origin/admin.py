from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, SubCategory, Posts, Contact, Introduce, TagField, User





class LawFirmAppAdminSite(admin.AdminSite):
    site_header = "CÔNG TY LUẬT TNHH MTV PHÚC MINH ANH"


admin_site = LawFirmAppAdminSite('MyLawFirm')


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = "__all__"


class IntroduceForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    search_fields = ['id', 'name', 'category__name']
    list_filter = ['name', 'category__name']


class PostsAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title', 'disc', 'image', 'created_date', 'updated_date', 'active', 'content', 'file_upload',
    #                 'subcategory', "author"]
    list_display = ['id', 'title', 'image', 'created_date', 'updated_date', 'active', 'subcategory', "author"]
    search_fields = ['id', 'title', 'created_date', 'subcategory__name', "author__name"]
    list_filter = ['id', 'title', 'disc', 'image', 'created_date', 'subcategory__name', "author__first_name"]
    form = PostForm

    class Media:
        css = {
            "all": ('/static/css/main.css',)
        }
        js = ("/static/js/script.js",)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'area', 'address', 'phone', 'email']
    search_fields = ['id', 'name', 'area', 'address', 'phone', 'email']
    list_filter = ['name', 'area', 'address', 'phone', 'email']


class IntroduceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manager', 'content']
    search_fields = ['id', 'name']
    list_filter = ['name']
    form = IntroduceForm


class TagFieldyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['name']


admin_site.register(User)
admin_site.register(Category, CategoryAdmin)
admin_site.register(SubCategory, SubCategoryAdmin)
admin_site.register(Posts, PostsAdmin)
admin_site.register(Contact, ContactAdmin)
admin_site.register(Introduce, IntroduceAdmin)
admin_site.register(TagField, TagFieldyAdmin)



# Register your models here.
