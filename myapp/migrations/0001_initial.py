# Generated by Django 3.2 on 2021-04-20 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATED_BY', models.CharField(max_length=32, verbose_name='创建人')),
                ('CREATED_TIME', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('UPDATED_BY', models.CharField(max_length=32, verbose_name='更新人')),
                ('UPDATED_TIME', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('JOB_TYPE', models.CharField(choices=[('01', 'Greenplum函数'), ('02', '其他')], default='02', max_length=32, verbose_name='任务类型')),
                ('JOB_NAME', models.CharField(max_length=128, verbose_name='任务名称')),
                ('JOB_COMMENT', models.CharField(max_length=128, verbose_name='任务描述')),
                ('IN_PARA', models.CharField(max_length=32, verbose_name='输入参数定义')),
                ('IN_PARA_COMMENT', models.CharField(max_length=1024, verbose_name='输入参数描述')),
                ('OUT_PARA', models.CharField(max_length=32, verbose_name='输出参数定义')),
                ('OUT_PARA_COMMENT', models.CharField(max_length=1024, verbose_name='输出参数描述')),
                ('VERSION', models.CharField(max_length=32, verbose_name='版本号')),
                ('IS_DELETE', models.CharField(default='N', max_length=1, verbose_name='是否删除')),
                ('PRO_STATUS', models.CharField(default='N', max_length=1, verbose_name='发布状态')),
            ],
        ),
    ]