# Generated by Django 2.1.2 on 2019-03-12 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]