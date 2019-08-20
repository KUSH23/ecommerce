# Generated by Django 2.1.2 on 2019-04-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded'), ('created', 'Created')], default='created', max_length=120),
        ),
    ]