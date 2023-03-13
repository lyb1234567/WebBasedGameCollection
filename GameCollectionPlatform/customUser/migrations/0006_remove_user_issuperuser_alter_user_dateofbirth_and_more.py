# Generated by Django 4.1.7 on 2023-03-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customUser", "0005_alter_user_dateofbirth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="isSuperUser",
        ),
        migrations.AlterField(
            model_name="user",
            name="dateOfBirth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="profilePic",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="userType",
            field=models.CharField(
                blank=True, default="Player", max_length=20, null=True
            ),
        ),
    ]
