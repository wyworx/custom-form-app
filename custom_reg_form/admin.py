from django.contrib import admin
from .models import ExtraInfo
import csv
from django.http import HttpResponse
from io import StringIO


class ExtraInfoAdmin(admin.ModelAdmin):
    actions = ['download_csv'] 
    list_display = ('user', 'nationality', 'age', 'phone_number',)
    list_display_links = ('user', 'nationality', 'age', 'phone_number',)
    list_filter = ('user',)
    search_fields = ('user', 'nationality', 'age', 'phone_number',)
    list_per_page = 25  
    def download_csv(self, request, queryset,*args, **kwargs):
        import csv
        f = open('some.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['user', 'nationality', 'age', 'phone_number',])
        for s in queryset:
            writer.writerow([s.user, s.nationality, s.age, s.phone_number])
        
        f.close()
        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response    
    download_csv.short_description = "Download CSV "



admin.site.register(ExtraInfo, ExtraInfoAdmin)
     
