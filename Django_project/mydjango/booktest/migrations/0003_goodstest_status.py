# Generated by Django 2.1 on 2020-05-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20200502_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodstest',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '下架'), (1, '上架')], default=1, verbose_name='商品状态'),
        ),
    ]