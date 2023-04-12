# Generated by Django 4.1.7 on 2023-04-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customUser", "0012_alter_user_profilepic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profilePic",
            field=models.ImageField(
                blank=True,
                default=None,
                max_length=1000,
                null=True,
                upload_to="media/profilePics",
            ),
        ),
    ]
