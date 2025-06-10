from django.contrib import admin
from .models import Article, Category
from django.contrib import messages  # برای ارسال پیام به ادمین
from django.utils.translation import ngettext  # برای ترجمه و نمایش پیام‌های وابسته به تعداد

# Admin header changes
admin.site.site_header = "اولین وبلاگ جنگویی من(پنل ادمین)"

# Register your models here.
@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله منتشر شد",
            "%d مقاله منتشر شدند",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )



@admin.action(description="پیش نویس شدن مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status="d")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله پیش نویس شد",
            "%d مقاله پیش نویس شدند",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','parent','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {
        'slug':('title',)
    }

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','jpublish','status','category_to_str')
    list_filter = ('publish','status')
    search_fields = ('title','describtion')
    prepopulated_fields = {
        'slug':('title',)
    }
    ordering = ('-status','-publish')
    actions = [make_published, make_draft]

    def category_to_str(self,obj):
        return ", ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = "دسته بندی"

admin.site.register(Article, ArticleAdmin)

