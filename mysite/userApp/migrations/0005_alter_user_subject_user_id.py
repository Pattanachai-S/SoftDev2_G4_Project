# Generated by Django 4.1.7 on 2023-03-16 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userApp', '0004_user1_alter_user_subject_user_id_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_subject',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
