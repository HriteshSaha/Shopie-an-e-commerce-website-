# Generated by Django 4.2.6 on 2023-11-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]
