# Generated by Django 3.0 on 2021-05-05 17:03

from django.db import migrations, models
import django.db.models.deletion
import nextstep.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('cpf', models.CharField(max_length=14, validators=[nextstep.core.validators.cpf_validator])),
                ('phone', models.CharField(max_length=15)),
                ('company', models.CharField(max_length=32)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='PersonMediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('foto', 1), ('biometria', 2)], max_length=32)),
            ],
            options={
                'db_table': 'person_media_type',
            },
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'person_type',
            },
        ),
        migrations.CreateModel(
            name='PersonMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_media', models.TextField()),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'db_table': 'person_media',
            },
        ),
        migrations.CreateModel(
            name='PersonAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_new', models.CharField(max_length=14)),
                ('cpf_old', models.CharField(max_length=14)),
                ('last_update', models.DateTimeField()),
                ('type', models.IntegerField(choices=[('add', 1), ('update', 2)])),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'db_table': 'person_audit',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PersonType'),
        ),
    ]