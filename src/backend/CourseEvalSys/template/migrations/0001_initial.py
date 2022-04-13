# Generated by Django 4.0.3 on 2022-04-13 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Course_ID', models.IntegerField(db_column='Course_ID', primary_key=True, serialize=False, verbose_name='Course_ID')),
                ('Course_Name', models.CharField(db_column='Course_Name', max_length=255, verbose_name='Course_name')),
                ('Department', models.CharField(db_column='Department', max_length=255, verbose_name='Department')),
                ('Is_Valid', models.BooleanField(db_column='Is_Valid', verbose_name='Is_Valid')),
                ('Final_Score', models.FloatField(db_column='Final_Score', null=True, verbose_name='FinalScore')),
            ],
            options={
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('User_ID', models.IntegerField(db_column='User_ID', primary_key=True, serialize=False, verbose_name='User_ID')),
                ('User_name', models.CharField(db_column='User_name', max_length=255, verbose_name='User_name')),
                ('Password', models.CharField(db_column='Password', max_length=255, verbose_name='Password')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('Comment_ID', models.IntegerField(db_column='Comment_ID', primary_key=True, serialize=False, verbose_name='Comment_ID')),
                ('Semester', models.CharField(db_column='Semester', max_length=255, verbose_name='Semeste')),
                ('Year', models.IntegerField(db_column='Year', verbose_name='Year')),
                ('Instructor', models.CharField(db_column='Instructor', max_length=255, verbose_name='Instructor')),
                ('Score', models.IntegerField(db_column='Score', verbose_name='Score')),
                ('Content', models.CharField(db_column='Content', max_length=255, verbose_name='Content')),
                ('Like_Num', models.IntegerField(db_column='Like_Num', verbose_name='Like_Num')),
                ('Dislike_Num', models.IntegerField(db_column='Dislike_Num', verbose_name='Dislike_Num')),
                ('Course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CourseID', to='template.courses')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_of_User', to='template.users')),
            ],
            options={
                'db_table': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='CommentsLikeStatus',
            fields=[
                ('CommentID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ID_of_Comment', serialize=False, to='template.comments')),
                ('Status', models.BooleanField(db_column='Status', verbose_name='Status')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserID', to='template.users')),
            ],
            options={
                'db_table': 'CommentsLikeStatus',
            },
        ),
    ]
