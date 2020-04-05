# Generated by Django 2.2.9 on 2020-04-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200403_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='picture')),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='rating',
            new_name='score',
        ),
        migrations.AddField(
            model_name='reservereview',
            name='pictures',
            field=models.ManyToManyField(to='api.ReviewsPictures'),
        ),
        migrations.AddField(
            model_name='routereview',
            name='pictures',
            field=models.ManyToManyField(to='api.ReviewsPictures'),
        ),
    ]
