# Generated by Django 2.0.3 on 2018-10-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0046_auto_20181009_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='scores',
            field=models.CharField(help_text='Raw test scores: [12.21, 14.23, 12.94]', max_length=16384),
        ),
    ]
