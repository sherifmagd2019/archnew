# Generated by Django 2.1.5 on 2019-01-25 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organiztion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('in_number', models.IntegerField()),
                ('in_date', models.DateTimeField()),
                ('out_number', models.IntegerField()),
                ('out_date', models.DateTimeField()),
                ('post_flag', models.CharField(choices=[('I', 'وارد'), ('O', 'صادر')], default='I', max_length=1)),
                ('files', models.FileField(upload_to='')),
                ('organization', models.ManyToManyField(to='auth.Group')),
                ('otherpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
