from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class job_detail(models.Model):
    ## 定义枚举值状态
    JOB_TYPE_STATUS_GP = '01'
    JOB_TYPE_STATUS_DEFAULT = '02'
    JOB_TYPE_STATUS_CHOICES = (
        (JOB_TYPE_STATUS_GP, 'Greenplum函数'),
        (JOB_TYPE_STATUS_DEFAULT, '其他'),
    )

    CREATED_BY = models.CharField('创建人',max_length=32) # 创建人
    CREATED_TIME = models.DateTimeField('创建时间',default=timezone.now) # 创建时间
    UPDATED_BY = models.CharField('更新人',max_length=32) # 更新人
    UPDATED_TIME = models.DateTimeField('更新时间',default=timezone.now)  # 更新时间
    JOB_TYPE = models.CharField('任务类型',max_length=32,
                                choices=JOB_TYPE_STATUS_CHOICES,
                                default=JOB_TYPE_STATUS_DEFAULT
                                ) # 任务类型 01：gp任务；02：datax任务；03：kafka推送任务；04：http请求任务
    JOB_NAME = models.CharField('任务名称',max_length=128) # 任务名称
    JOB_COMMENT = models.CharField('任务描述',max_length=128)  # 任务描述
    IN_PARA = models.CharField('输入参数定义',max_length=32) # 输入参数定义 参数使用英文逗号分隔
    IN_PARA_COMMENT = models.CharField('输入参数描述',max_length=1024)  # 输入参数描述
    OUT_PARA = models.CharField('输出参数定义',max_length=32)  # 输出参数定义 参数使用英文逗号分隔
    OUT_PARA_COMMENT = models.CharField('输出参数描述',max_length=1024)  # 输出参数描述
    VERSION = models.CharField('版本号',max_length=32) # 版本号
    IS_DELETE = models.CharField('是否删除',max_length=1, default='N')  # 逻辑删除 Y:删除；N:正常
    PRO_STATUS = models.CharField('发布状态',max_length=1,default='N') # 发布状态 Y:发布；N:开发
