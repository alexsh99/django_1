# Generated by Django 3.2 on 2021-05-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_productcategory_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='id_active',
            field=models.BooleanField(default=True),
        ),
    ]
