# Generated by Django 2.0.8 on 2018-09-20 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0006_auto_20180807_2132'),
        ('adjallocation', '0003_auto_20171110_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamInstitutionConflict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Institution', verbose_name='institution')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team', verbose_name='team')),
            ],
            options={
                'verbose_name': 'team-institution conflict',
                'verbose_name_plural': 'team-institution conflicts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='teaminstitutionconflict',
            unique_together={('team', 'institution')},
        ),
    ]
