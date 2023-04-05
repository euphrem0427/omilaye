# Generated by Django 4.1.2 on 2023-03-09 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0001_initial'),
        ('app', '0002_abonne_date_ajout'),
    ]

    operations = [
        migrations.AddField(
            model_name='agence',
            name='commune',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agence.commune'),
        ),
        migrations.AddField(
            model_name='agence',
            name='departement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agence.departement'),
        ),
        migrations.AddField(
            model_name='site',
            name='commune',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agence.commune'),
        ),
        migrations.AddField(
            model_name='site',
            name='departement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agence.departement'),
        ),
    ]