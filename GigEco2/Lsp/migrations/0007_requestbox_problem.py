# Generated by Django 5.0.1 on 2024-02-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lsp', '0006_alter_requestbox_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbox',
            name='problem',
            field=models.TextField(blank=True),
        ),
    ]
