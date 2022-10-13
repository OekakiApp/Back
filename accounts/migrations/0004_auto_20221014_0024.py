# Generated by Django 3.2.15 on 2022-10-13 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_useraccount_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='accounts', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]