# Generated by Django 4.1.7 on 2023-06-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppc', '0003_alter_component_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='link',
            field=models.CharField(max_length=150),
        ),
    ]