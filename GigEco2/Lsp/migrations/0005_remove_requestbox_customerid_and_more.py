# Generated by Django 5.0.1 on 2024-02-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lsp', '0004_requestbox_customeremail_serviceprovider_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestbox',
            name='customerId',
        ),
        migrations.AlterField(
            model_name='requestbox',
            name='accepted',
            field=models.BooleanField(blank=True),
        ),
    ]