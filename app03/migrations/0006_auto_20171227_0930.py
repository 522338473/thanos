# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0005_auto_20171224_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='recv_date',
            field=models.DateField(blank=True, null=True, verbose_name='顾问接单日期'),
        ),
        migrations.AlterField(
            model_name='courserecord',
            name='day_num',
            field=models.IntegerField(help_text='此处填写第几节课或第几天课程,必须为数字', verbose_name='节次'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.IntegerField(choices=[(1, '已报名'), (2, '未报名')], default=2, help_text='选择客户此时的状态', verbose_name='报名状态'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='record',
            field=models.CharField(choices=[('checked', '已签到'), ('vacate', '请假'), ('late', '迟到'), ('absence', '缺勤'), ('leave_early', '早退')], default='checked', max_length=64, verbose_name='上课记录'),
        ),
    ]
