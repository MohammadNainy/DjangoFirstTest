from django.contrib import admin
from .models import Article, Category

# Register your models here.
@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")

@admin.action(description="پیش نویس شدن مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    queryset.update(status="d") 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','parent','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {
        'slug':('title',)
    }

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','jpublish','status','category_to_str')
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