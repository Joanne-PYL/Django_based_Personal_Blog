# Generated by Django 4.0.5 on 2022-06-12 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='name',
        ),
    ]
