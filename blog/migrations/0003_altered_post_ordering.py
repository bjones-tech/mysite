# Generated by Django 2.0.2 on 2018-05-03 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_altered_content_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date']},
        ),
    ]
