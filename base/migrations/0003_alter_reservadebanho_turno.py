# Generated by Django 4.2.4 on 2023-09-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reservadebanho_email_reservadebanho_tamanho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservadebanho',
            name='turno',
            field=models.CharField(default='Não definido', max_length=45, verbose_name='Turno'),
        ),
    ]
