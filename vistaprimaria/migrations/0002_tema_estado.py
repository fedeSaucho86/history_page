# Generated by Django 4.2.1 on 2023-06-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprimaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='estado',
            field=models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado'), ('Retirado', 'Retirado')], default='Borrador', max_length=10),
        ),
    ]
