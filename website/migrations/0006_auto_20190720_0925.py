# Generated by Django 2.2.3 on 2019-07-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_delete_vision1'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('History', models.TextField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='goals',
        ),
    ]