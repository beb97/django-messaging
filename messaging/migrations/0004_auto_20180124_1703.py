# Generated by Django 2.0.1 on 2018-01-24 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20180124_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='messaging.Message'),
        ),
    ]
