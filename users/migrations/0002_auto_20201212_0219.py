# Generated by Django 3.1.3 on 2020-12-12 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionmodel',
            old_name='montat',
            new_name='montant',
        ),
    ]
