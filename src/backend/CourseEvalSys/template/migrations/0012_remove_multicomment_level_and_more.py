# Generated by Django 4.0.3 on 2022-04-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0011_alter_courses_final_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multicomment',
            name='Level',
        ),
        migrations.RemoveField(
            model_name='multicomment',
            name='Upper_Comment_ID',
        ),
        migrations.AddField(
            model_name='multicomment',
            name='Lower_Comment_ID',
            field=models.IntegerField(db_column='Lower_Comment_ID', default=1, verbose_name='Lower_Comment_ID'),
        ),
    ]