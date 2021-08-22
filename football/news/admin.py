from django.contrib import admin
from .models import Article
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from jalali_date import datetime2jalali,date2jalali
# Register your models here.

class ArticleAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('title','slug','publish_fa','status')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('-publish','-status')
    def publish_fa(self,obj):
        return datetime2jalali(obj.publish).strftime('%y/%m/%d _ %H:%M:%S')
    publish_fa.short_description='زمان انتشار'

admin.site.register(Article,ArticleAdmin)