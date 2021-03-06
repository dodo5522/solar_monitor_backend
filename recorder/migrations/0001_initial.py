# Generated by Django 3.1.1 on 2020-10-03 15:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('group_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('zip_code', models.CharField(blank=True, max_length=8, verbose_name='郵便番号')),
                ('country', models.CharField(blank=True, default='日本', max_length=40, verbose_name='国')),
                ('prefecture', models.CharField(blank=True, max_length=40, verbose_name='都道府県')),
                ('city', models.CharField(blank=True, max_length=40, verbose_name='市区町村番地')),
                ('building', models.CharField(blank=True, max_length=40, verbose_name='建物名')),
            ],
        ),
        migrations.CreateModel(
            name='Recorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('unit_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='KilowattHours',
            fields=[
                ('recorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recorder.recorder')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.DecimalField(decimal_places=1, max_digits=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.group')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.location')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.unit')),
            ],
            bases=('recorder.recorder',),
        ),
        migrations.CreateModel(
            name='AmpHours',
            fields=[
                ('recorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recorder.recorder')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.DecimalField(decimal_places=1, max_digits=10)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.group')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.location')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.unit')),
            ],
            bases=('recorder.recorder',),
        ),
    ]
