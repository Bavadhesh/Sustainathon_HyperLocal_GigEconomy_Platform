# Generated by Django 5.0.1 on 2024-02-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lsp', '0003_requestbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbox',
            name='customerEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
