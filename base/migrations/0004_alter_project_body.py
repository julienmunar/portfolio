# Generated by Django 3.2.5 on 2021-08-01 09:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_skills_fonticon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]