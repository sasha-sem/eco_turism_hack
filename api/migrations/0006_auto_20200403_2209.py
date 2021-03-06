# Generated by Django 2.2.9 on 2020-04-03 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200403_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='complexity',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='sights',
            name='rating',
        ),
        migrations.AddField(
            model_name='reservereview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReserveReviewUser', to='api.userProfile', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='routereview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RouteReviewUser', to='api.userProfile', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='routes',
            name='сomplexity',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', verbose_name='Сложность'),
        ),
    ]
