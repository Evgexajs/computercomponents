# Generated by Django 4.1.7 on 2023-06-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppc', '0004_alter_component_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='details',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='component',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='component',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]