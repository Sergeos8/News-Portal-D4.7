# Generated by Django 4.1.3 on 2022-12-07 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='feedback_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categoryType',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='text',
        ),
    ]