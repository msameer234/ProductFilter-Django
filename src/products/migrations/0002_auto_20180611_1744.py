# Generated by Django 2.0.2 on 2018-06-11 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='created_at',
            new_name='pCreated_at',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='_OS',
            new_name='pModel',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='_model',
            new_name='pOS',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='_price',
            new_name='pPrice',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='_processor',
            new_name='pProcessor',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='pTitle',
        ),
    ]
