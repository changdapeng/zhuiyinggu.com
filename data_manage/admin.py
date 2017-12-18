"""
data_manage/admin.py
"""

from django.contrib import admin

from data_manage.models import Data, Book, Music



# Data Admin管理界面管理器
# ------------------------
class DataAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'step', 'data_type', 'size', 'creator', 'create_date', 'address_type', 'address', 'path',)
    list_filter = ('data_type', 'step', 'creator', 'create_date',)
    fieldsets = (
        ('Data info', {'fields': ('name', 'description', 'step', 'data_type', 'size', 'address_type', 'address', 'path',)}),
        ('create info', {'fields': ('creator', 'create_date',)}),
    )
    search_fields = ('name', 'path', 'step', 'data_type')
    ordering = ('name', 'size',)


admin.site.register(Data, DataAdmin)



# Music Admin管理界面管理器
# -------------------------
class MusicAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'singer', 'album', 'music_format', 'music_type', 'music_step', 'music_file', 'creator', 'create_date', 'update_date',)
    list_filter = ('singer', 'album', 'music_format', 'music_type', 'music_step', 'create_date',)
    fieldsets = (
        ('Music info', {'fields': ('name', 'description', 'singer', 'album', 'music_format', 'music_type', 'music_step', 'music_file',)}),
        ('create info', {'fields': ('creator', )}),
    )
    search_fields = ('name', 'singer', 'album', 'music_type', 'music_step')
    ordering = ('name', 'singer',)


admin.site.register(Music, MusicAdmin)



# Book Admin管理界面管理器
# ------------------------
class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'author', 'book_type', 'book_step', 'book_file', 'creator', 'create_date', 'update_date',)
    list_filter = ('author', 'book_type', 'book_step', 'create_date',)
    fieldsets = (
        ('Book info', {'fields': ('name', 'description', 'author', 'book_type', 'book_step', 'book_file',)}),
        ('create info', {'fields': ('creator', )}),
    )
    search_fields = ('name', 'author', 'book_step', 'book_type')
    ordering = ('name', 'author',)


admin.site.register(Book, BookAdmin)