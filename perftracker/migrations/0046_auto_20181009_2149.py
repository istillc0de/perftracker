# Generated by Django 2.0.3 on 2018-10-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0045_hwfarmnodemodel_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwfarmnodemodel',
            name='purpose',
            field=models.CharField(blank=True, default=None, help_text='a test server', max_length=256, null=True),
        ),
    ]
