from django.contrib import admin
from matrix.models import Subject, Matrix, Block


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class BlockInline(admin.StackedInline):
    model = Block


@admin.register(Matrix)
class MatrixAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlockInline]
