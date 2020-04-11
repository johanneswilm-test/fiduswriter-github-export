# Generated by Django 2.2.10 on 2020-04-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_export', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrepository',
            name='export_epub',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookrepository',
            name='export_html',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookrepository',
            name='export_latex',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookrepository',
            name='export_unpacked_epub',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
