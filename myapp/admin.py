from django.contrib import admin
from myapp.models import job_detail

# Register your models here.
admin.site.register(job_detail)
admin.site.site_header = '人脸识别考勤系统'
admin.site.site_title = 'GZHU人脸识别管理系统'