# Generated by Django 2.0.7 on 2018-08-01 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_requestfreinds'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestFreind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
                ('datetime_request', models.DateTimeField(default=django.utils.timezone.now)),
                ('datetime_accept', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('accept', 'Принят'), ('deny', 'Отказ'), ('none', 'Запрос')], default='none', max_length=6)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_freinds_send', to='users.User')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_freinds_recv', to='users.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='requestfreinds',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='requestfreinds',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='RequestFreinds',
        ),
    ]
