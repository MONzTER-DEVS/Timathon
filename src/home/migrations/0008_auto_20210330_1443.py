# Generated by Django 3.1.7 on 2021-03-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210329_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfile',
            old_name='user_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='userfile',
            name='file_name',
        ),
        migrations.AddField(
            model_name='userfile',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
