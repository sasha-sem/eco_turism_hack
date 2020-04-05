# Generated by Django 2.2.9 on 2020-04-05 00:05

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200404_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='achievements',
            field=models.ManyToManyField(blank=True, to='api.Achievements'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='known_routes',
            field=models.ManyToManyField(blank=True, to='api.Routes'),
        ),
        migrations.CreateModel(
            name='GeoCash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('descr', models.TextField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=512, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('reserve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GeoCashReserve', to='api.Reserves', verbose_name='Заповедник')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
    ]
