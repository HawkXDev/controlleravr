# Generated by Django 4.0 on 2021-12-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr', '0002_alter_avrindex_extension_module_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avrindex',
            name='documentation',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
