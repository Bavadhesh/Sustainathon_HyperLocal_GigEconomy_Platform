# Generated by Django 5.0.1 on 2024-02-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lsp', '0005_remove_requestbox_customerid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestbox',
            name='accepted',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
