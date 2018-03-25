from django.contrib import admin
from .models import Movie, Person


admin.site.register(Person)


class MovieInline(admin.TabularInline):

    model = Movie.starring.through
    verbose_name = u"Starrings"
    verbose_name_plural = u"Starrings"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    exclude = ("starring", )
    inlines = (
        MovieInline,
    )