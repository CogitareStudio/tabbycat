# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adjallocation', '0008_auto_20170706_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adjudicatoradjudicatorconflict',
            options={'verbose_name': 'adjudicator-adjudicator conflict', 'verbose_name_plural': 'adjudicator-adjudicator conflicts'},
        ),
        migrations.AlterModelOptions(
            name='adjudicatorconflict',
            options={'verbose_name': 'adjudicator-team conflict', 'verbose_name_plural': 'adjudicator-team conflicts'},
        ),
        migrations.AlterModelOptions(
            name='adjudicatorinstitutionconflict',
            options={'verbose_name': 'adjudicator-institution conflict', 'verbose_name_plural': 'adjudicator-institution conflicts'},
        ),
        migrations.AlterModelOptions(
            name='debateadjudicator',
            options={'verbose_name': 'debate adjudicator', 'verbose_name_plural': 'debate adjudicators'},
        ),
        migrations.AlterField(
            model_name='adjudicatoradjudicatorconflict',
            name='adjudicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjudicatoradjudicatorconflict_source_set', to='participants.Adjudicator', verbose_name='adjudicator 1'),
        ),
        migrations.AlterField(
            model_name='adjudicatoradjudicatorconflict',
            name='conflict_adjudicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjudicatoradjudicatorconflict_target_set', to='participants.Adjudicator', verbose_name='adjudicator 2'),
        ),
        migrations.AlterField(
            model_name='adjudicatorconflict',
            name='adjudicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Adjudicator', verbose_name='adjudicator'),
        ),
        migrations.AlterField(
            model_name='adjudicatorconflict',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team', verbose_name='team'),
        ),
        migrations.AlterField(
            model_name='adjudicatorinstitutionconflict',
            name='adjudicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Adjudicator', verbose_name='adjudicator'),
        ),
        migrations.AlterField(
            model_name='adjudicatorinstitutionconflict',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Institution', verbose_name='institution'),
        ),
        migrations.AlterField(
            model_name='debateadjudicator',
            name='adjudicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Adjudicator', verbose_name='adjudicator'),
        ),
        migrations.AlterField(
            model_name='debateadjudicator',
            name='debate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.Debate', verbose_name='debate'),
        ),
        migrations.AlterField(
            model_name='debateadjudicator',
            name='timing_confirmed',
            field=models.NullBooleanField(verbose_name='available?'),
        ),
        migrations.AlterField(
            model_name='debateadjudicator',
            name='type',
            field=models.CharField(choices=[('C', 'chair'), ('P', 'panellist'), ('T', 'trainee')], max_length=2, verbose_name='type'),
        ),
    ]