# Generated by Django 5.1.4 on 2024-12-10 16:11

import ckeditor_uploader.fields
import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='articles/')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
