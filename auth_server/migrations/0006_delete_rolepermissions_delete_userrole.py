# Generated by Django 4.0.6 on 2022-07-27 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_server', '0005_rename_role_userrole_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RolePermissions',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]
