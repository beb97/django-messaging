# Generated by Django 2.0.1 on 2018-01-24 16:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20180124_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messaging.Message')),
            ],
            bases=('messaging.message',),
        ),
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='messaging.Message'),
        ),
    ]