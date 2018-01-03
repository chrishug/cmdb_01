# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-02 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cmdb_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='execl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=20, null=True, verbose_name='城市')),
                ('room', models.CharField(blank=True, max_length=20, null=True, verbose_name='机房')),
                ('floor', models.CharField(blank=True, max_length=20, null=True, verbose_name='楼层')),
                ('location', models.CharField(blank=True, max_length=30, null=True, verbose_name='机架位')),
                ('location_num', models.IntegerField(blank=True, null=True, verbose_name='机架编号')),
                ('size', models.CharField(blank=True, max_length=20, null=True, verbose_name='尺寸')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='SN号')),
                ('manufacture', models.CharField(blank=True, max_length=128, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号/规格')),
                ('client_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='客户编码')),
                ('OS', models.CharField(blank=True, max_length=20, null=True, verbose_name='OS')),
                ('client', models.CharField(blank=True, max_length=20, null=True, verbose_name='客户')),
                ('print_label', models.BooleanField(default=False, verbose_name='是否打印标签')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('vlan_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.CharField(blank=True, max_length=128, null=True, verbose_name='内网IP')),
            ],
        ),
    ]
