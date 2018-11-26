# Generated by Django 2.1.1 on 2018-11-25 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_propiedades_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='propiedades',
            name='status',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10),
        ),
        migrations.AlterField(
            model_name='propiedades',
            name='tipo',
            field=models.CharField(choices=[('venta', 'VENTA'), ('renta', 'RENTA')], default='venta', max_length=10),
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='principal.Propiedades'),
        ),
    ]
