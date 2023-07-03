# Generated by Django 4.2.1 on 2023-07-02 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprimaria', '0004_tema_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continente', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='continente/%Y/%m/%d')),
            ],
        ),
        migrations.RemoveField(
            model_name='tema',
            name='nivel',
        ),
        migrations.DeleteModel(
            name='Nivel',
        ),
        migrations.AddField(
            model_name='tema',
            name='continente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vistaprimaria.continente'),
        ),
    ]
