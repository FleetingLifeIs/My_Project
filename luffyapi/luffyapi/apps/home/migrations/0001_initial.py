# Generated by Django 2.2.6 on 2019-11-05 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='广告图片')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='广告标题')),
                ('link', models.CharField(blank=True, max_length=512, null=True, verbose_name='广告链接')),
                ('orders', models.IntegerField(default=1, verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上架')),
                ('note', models.TextField(verbose_name='备注信息')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'ly_banner',
            },
        ),
    ]
