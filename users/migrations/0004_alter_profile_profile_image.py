# Generated by Django 4.0.2 on 2022-02-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_social_instagram_profile_social_twitter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.jpg', null=True, upload_to='profiles/'),
        ),
    ]
