from django.contrib import admin
from mainsite.models import Post, AccessInfo, PlayList, Video, Branch, StoreIncome, PlayList1, PlayList2, PlayList3

class PostAdmin(admin.ModelAdmin):
   list_display = ('name','picture','video','wiki','pub_date')
admin.site.register(PlayList, PostAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('name','picture','video','wiki','pub_date')
admin.site.register(PlayList1, PostAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('name','picture','video','wiki','pub_date')
admin.site.register(PlayList2, PostAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('name','picture','video','wiki','pub_date')
admin.site.register(PlayList3, PostAdmin)

class VideoAdmin(admin.ModelAdmin):
   list_display = ('title', 'vid')
admin.site.register(Video, VideoAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('title','slug','pub_date')
admin.site.register(Post,PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
   list_display = ('title','name')
admin.site.register(Branch,BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
   list_display = ('branch','income_year','income_month','income')
admin.site.register(StoreIncome,StoreIncomeAdmin)