# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-31 14:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_answer_importance', models.CharField(choices=[(b'Mandatory', b'Mandatory'), (b'Very Important', b'Very Important'), (b'Somewhat Important', b'Somewhat Important'), (b'Not Important', b'Not Important')], max_length=50)),
                ('their_importance', models.CharField(choices=[(b'Mandatory', b'Mandatory'), (b'Very Important', b'Very Important'), (b'Somewhat Important', b'Somewhat Important'), (b'Not Important', b'Not Important')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='questions.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('their_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_answer', to='questions.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
