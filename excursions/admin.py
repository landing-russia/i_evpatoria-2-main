from django.contrib import admin
from django.utils.html import mark_safe
from .models import Excursion, Photo, Tag


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('get_thumbnail', 'name', 'excursion',)
    list_filter = ('excursion__name',)
    fields = ('image', 'name', 'excursion',)
    search_fields = ['name',
                     'excursion__name', ]

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.image.url}" />')

    get_thumbnail.short_description = 'Фото'


class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ('image_preview', 'image', 'name')
    readonly_fields = ('image_preview',)
    max_num = 5


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Экскурсия',
            {
                'fields': (
                    'name', 'slug',
                    'description', 'types', 'tags', 'extra',
                    'location', 'duration',
                    'start_time',
                    'max_people_count',
                    'price',
                    'price_child',
                    'price_group',
                    'is_published',
                    'guide',
                )
            }
        ),
    )
    list_display = ('name',
                    'guide',
                    'duration',
                    'max_people_count',
                    'types',
                    'is_published',)

    list_filter = ('is_published', 'types', 'tags')
    search_fields = ['name',
                     'guide__email', ]
    # filter_horizontal = ('tags',)

    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ('guide',)
    inlines = (PhotoInline,)


class GuideAdminArea(admin.AdminSite):
    site_header = 'Админка для гидов'
    site_title = 'Администрирование экскурсий'
    index_title = 'Экскурсии'


class GuideAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Экскурсия',
            {
                'fields': (
                    'name', 'slug',
                    'description', 'types', 'tags', 'extra',
                    'location', 'duration',
                    'start_time',
                    'max_people_count',
                    'price',
                    'price_child',
                    'price_group',
                    'is_published',
                    # 'guide',
                )
            }
        ),
    )
    list_display = ('name',
                    # 'guide',
                    'duration',
                    'max_people_count',
                    'types',
                    'is_published',)

    list_filter = ('is_published', 'types', 'tags')
    search_fields = ['name',
                     'guide__email', ]
    # filter_horizontal = ('tags',)

    prepopulated_fields = {"slug": ("name",)}
    # raw_id_fields = ('guide',)
    inlines = (PhotoInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(guide=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'guide', None) is None:
            obj.guide = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        # if not is_superuser:
            # form.base_fields['guide'] = request.user
            # form.base_fields['guide'].disabled = True
            # form.base_fields['slug'].disabled = True

        return form


class TagExcursionAdmin(admin.ModelAdmin):
    pass


guide_site = GuideAdminArea(name='Администрирование экскурсий')

guide_site.register(Excursion, GuideAdmin)
# guide_site.register(Photo, PhotoAdmin)
guide_site.register(Tag, TagExcursionAdmin)
