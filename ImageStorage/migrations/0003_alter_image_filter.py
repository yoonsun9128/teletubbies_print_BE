# Generated by Django 4.1.3 on 2022-11-24 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
        ('ImageStorage', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.filter'),
        ),
    ]
