# Generated by Django 3.0 on 2021-09-30 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20210930_1400'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="Profile",
                    table="profiles_profile"
                )
            ]
        ),
    ]
