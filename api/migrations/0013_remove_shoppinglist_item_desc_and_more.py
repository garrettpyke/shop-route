# Generated by Django 4.0.3 on 2022-04-14 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_shoppinglist_item_desc_shoppinglist_item_loc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='item_desc',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='item_loc',
        ),
    ]
