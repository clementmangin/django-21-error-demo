from django.contrib import admin

from .models import Parent, Child


class ChildInline(admin.TabularInline):

    model = Child
    extra = 0


class ParentAdmin(admin.ModelAdmin):

    inlines = [
        ChildInline,
    ]


admin.site.register(Parent, ParentAdmin)
