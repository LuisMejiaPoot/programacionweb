# Generated by Django 4.1.3 on 2022-11-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['created_date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='capacidad',
            field=models.IntegerField(default=20),
        ),
    ]