from .models import BlogPost, Screening

from django.contrib import admin


class ScreeningAdmin(admin.ModelAdmin):
    exclude = ('description',)


class BlogPostAdmin(admin.ModelAdmin):
    exclude = ('slug', 'text')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Screening, ScreeningAdmin)
