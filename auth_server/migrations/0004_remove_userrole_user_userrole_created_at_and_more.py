# Generated by Django 4.0.6 on 2022-07-26 22:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth_server', '0003_rename_rolex_userrole_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrole',
            name='user',
        ),
        migrations.AddField(
            model_name='userrole',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userrole',
            name='state',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userrole',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='regular', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.IntegerField(default=1)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_server.userrole')),
            ],
        ),
    ]