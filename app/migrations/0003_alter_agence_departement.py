# Generated by Django 3.2.12 on 2023-06-22 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0001_initial'),
        ('app', '0002_auto_20230622_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agence',
            name='departement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agence.departement'),
        ),
    ]