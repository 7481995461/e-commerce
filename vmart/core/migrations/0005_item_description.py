# Generated by Django 4.2.5 on 2023-10-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a text description '),
            preserve_default=False,
        ),
    ]
