from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

# Register your models here.
admin.AdminSite.site_header = "پنل مدیریت جنگو"
admin.AdminSite.site_title = "پنل جنگو"
admin.AdminSite.index_title = "پنل مدیریت سایت"


# Inline
# class ImageInline(admin.TabularInline):
#     model = Image
#     extra = 0
#     classes = ['collapse']
class ImageInline(admin.StackedInline):
    model = Image
    extra = 0
    classes = ['collapse']


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    classes = ['collapse']
# class CommentInline(admin.StackedInline):
#     model = Comment
#     extra = 0
#     classes = ['collapse']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # use list for customize panel admin 👇🏻
    list_display = ['title', 'author', 'category', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['status', ('publish', JDateFieldListFilter), 'author']
    search_fields = ['title', 'description']
    # list_display_links = ['author']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['status', 'category']
    inlines = [ImageInline, CommentInline]
    # use tuple for customize panel admin 👇🏻
    # list_display = ('title', 'author', 'publish', 'status')
    # ordering = ('title', 'publish')
    # list_filter = ('status', 'publish', 'author')
    # search_fields = ('title', 'description')
    # list_display_links = ['author']
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # prepopulated_fields = {'slug': ('title',)}
    # list_editable = ('status',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'email']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created', 'active']
    list_filter = ['active', ('created', JDateFieldListFilter), ('updated', JDateFieldListFilter)]
    search_fields = ['name', 'body']
    list_editable = ['active']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'title', 'created']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'bio', 'job', 'photo']
