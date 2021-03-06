# Generated by Django 2.1 on 2020-05-04 13:52

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_goodstest_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=200)),
                ('is_delete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(on_delete=None, to='booktest.BookInfo')),
            ],
        ),
        migrations.AlterModelOptions(
            name='goodstest',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterField(
            model_name='goodstest',
            name='detail',
            field=DjangoUeditor.models.UEditorField(verbose_name='商品详情'),
        ),
    ]
