# Generated by Django 2.2 on 2019-04-14 13:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('student', 'STUDENT'), ('employer', 'EMPLOYER'), ('freelancer', 'FREELANCER')], default='student', max_length=10)),
                ('mother_name', models.CharField(blank=True, max_length=60, null=True)),
                ('fathers_name', models.CharField(blank=True, max_length=60, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('country', models.CharField(choices=[('australia', 'AUSTRALIA'), ('india', 'INDIA'), ('united states of america', 'UNITED STATES OF AMERICA'), ('united kingdoms', 'UNITED KINGDOMS')], default='india', max_length=50)),
                ('state', models.CharField(default='any', max_length=50)),
                ('city', models.CharField(default='any', max_length=50)),
                ('area', models.CharField(default='any', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Other_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_1', models.FileField(null=True, upload_to='media/', verbose_name='Document 1')),
                ('document_2', models.FileField(null=True, upload_to='media/', verbose_name='Document 2')),
                ('document_3', models.FileField(null=True, upload_to='media/', verbose_name='Document 3')),
                ('document_4', models.FileField(null=True, upload_to='media/', verbose_name='Document 4')),
                ('document_5', models.FileField(null=True, upload_to='media/', verbose_name='Document 5')),
                ('signature', models.ImageField(null=True, upload_to='media/', verbose_name='Signature Photo')),
                ('signed_photo', models.ImageField(null=True, upload_to='media/', verbose_name='Singed Photo')),
                ('thumb_impression_photo', models.ImageField(null=True, upload_to='media/', verbose_name='Thumb Impression Photo')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('10', '10'), ('12', '12'), ('diploma', 'DIPLOMA'), ('under graduation', 'UNDER GRADUATION'), ('post graduation', 'POST GRADUATION')], default='10', max_length=20)),
                ('branch', models.CharField(blank=True, default='in any', max_length=10, null=True)),
                ('roll_number', models.CharField(max_length=15)),
                ('university', models.CharField(max_length=50)),
                ('duration', models.CharField(default='in years', max_length=4)),
                ('year_of_passing', models.CharField(max_length=4)),
                ('pencentile', models.CharField(default='in numbers', max_length=4)),
                ('upload_marksheet', models.ImageField(upload_to='users/%y/%m/%d')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('institute_name', models.CharField(max_length=50)),
                ('duration', models.CharField(default='in months', max_length=2)),
                ('validity_of_certification', models.CharField(default='in years', max_length=2)),
                ('upload_certificate', models.ImageField(upload_to='users/%y/%m/%d')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Courses', to='account.Profile')),
            ],
        ),
    ]
