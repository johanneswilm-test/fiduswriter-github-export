# Generated by Django 2.2.10 on 2020-04-02 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0007_bookstyle_bookstylefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_repo_id', models.IntegerField()),
                ('github_repo_full_name', models.CharField(max_length=256)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]
