# Generated by Django 4.0.3 on 2022-04-14 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_item_name_shoppinglist_item_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='item_qty',
        ),
    ]
