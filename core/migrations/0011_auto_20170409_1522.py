# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_member_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custodian',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Person'),
        ),
        migrations.AlterField(
            model_name='enrolment',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Group'),
        ),
        migrations.AlterField(
            model_name='enrolment',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Person'),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Membership'),
        ),
        migrations.AlterField(
            model_name='member',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Person'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Person'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Person'),
        ),
    ]
