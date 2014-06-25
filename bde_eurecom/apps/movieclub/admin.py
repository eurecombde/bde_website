from .models import BlogPost, Screening

from django.contrib import admin


class ScreeningAdmin(admin.ModelAdmin):
    exclude = ('description',)


class BlogPostAdmin(admin.ModelAdmin):
    exclude = ('slug', 'text', 'author')

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not hasattr(instance, 'author'):
            instance.author = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Screening, ScreeningAdmin)
