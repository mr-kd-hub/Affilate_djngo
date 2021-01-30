# Generated by Django 3.0.8 on 2020-09-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_Name', models.CharField(max_length=70)),
                ('Member_Position', models.CharField(max_length=100)),
                ('Member_Profile', models.ImageField(upload_to='img/')),
                ('Member_FaceBook_Account', models.CharField(blank=True, max_length=255)),
                ('Member_Twitter_Account', models.CharField(blank=True, max_length=255)),
                ('Member_Instagram_Account', models.CharField(blank=True, max_length=255)),
                ('Member_Linkdin_Account', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]