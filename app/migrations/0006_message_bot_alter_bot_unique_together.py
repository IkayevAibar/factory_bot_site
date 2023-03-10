# Generated by Django 4.1.5 on 2023-01-17 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('app', '0005_bot'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='bot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.bot', verbose_name='Получатель[Bot] сообщения'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='bot',
            unique_together={('token', 'chat_id')},
        ),
    ]
