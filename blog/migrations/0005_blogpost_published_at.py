# Generated by Django 5.0.3 on 2024-11-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_image_alter_blogpost_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
