# Generated by Django 3.0.3 on 2020-05-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_merge_p_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merge',
            name='p_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]