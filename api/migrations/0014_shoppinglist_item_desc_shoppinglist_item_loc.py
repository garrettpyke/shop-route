# Generated by Django 4.0.3 on 2022-04-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_shoppinglist_item_shoppinglist_item_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='item_desc',
            field=models.CharField(db_index=True, default='potatoes', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='item_loc',
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
    ]