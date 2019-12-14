# Generated by Django 2.2 on 2019-12-14 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_received', to='webapp.Gallery', verbose_name='Нравится фотография')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laike', to=settings.AUTH_USER_MODEL, verbose_name='Автор лайка')),
            ],
        ),
    ]
