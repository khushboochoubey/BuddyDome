# Generated by Django 4.1.4 on 2023-01-29 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0006_guide_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='name',
            new_name='nameb',
        ),
    ]