# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 21:18


from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import djangoplus.admin.models
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    replaces = [('admin', '0001_initial'), ('admin', '0002_log_logindex'), ('admin', '0003_auto_20160914_1821'), ('admin', '0004_auto_20161001_1750'), ('admin', '0005_auto_20161005_1536'), ('admin', '0006_organization_organizationrole'), ('admin', '0007_auto_20161124_1811'), ('admin', '0008_auto_20161124_1825'), ('admin', '0009_auto_20170420_1238'), ('admin', '0010_auto_20170428_1545'), ('admin', '0011_user_permission_mapping'), ('admin', '0012_auto_20170619_1648'), ('admin', '0013_auto_20170910_1543'), ('admin', '0014_auto_20180106_1921'), ('admin', '0015_settings_company')]

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'admin_user_groups',
                'verbose_name': 'Fun\xe7\xe3o',
                'verbose_name_plural': 'Fun\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', djangoplus.db.models.fields.CharField(blank=True, max_length=30, verbose_name='Nome')),
                ('username', djangoplus.db.models.fields.CharField(max_length=30, unique=True, verbose_name='Login')),
                ('email', djangoplus.db.models.fields.CharField(blank=True, default='', max_length=75, verbose_name='E-mail')),
                ('active', djangoplus.db.models.fields.BooleanField(default=True, verbose_name='Ativo?')),
                ('photo', djangoplus.db.models.fields.ImageField(blank=True, default='user.png', null=True, upload_to='profiles', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            managers=[
                ('objects', djangoplus.admin.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', djangoplus.db.models.fields.CharField(default='Django+', max_length=255, verbose_name='Nome')),
                ('name', djangoplus.db.models.fields.CharField(default='Django Plus', max_length=255, verbose_name='Descri\xe7\xe3o')),
                ('logo', djangoplus.db.models.fields.ImageField(blank=True, default='', null=True, upload_to='config', verbose_name='Logotipo')),
                ('logo_pdf', djangoplus.db.models.fields.ImageField(blank=True, default='', help_text='Imagem sem fundo transparente', null=True, upload_to='config', verbose_name='Logotipo para PDF')),
                ('icon', djangoplus.db.models.fields.ImageField(blank=True, default='blank.png', null=True, upload_to='config', verbose_name='\xcdcone')),
                ('background', djangoplus.db.models.fields.ImageField(blank=True, default='', upload_to='config', verbose_name='Background')),
                ('twitter', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('facebook', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('google', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Google')),
                ('pinterest', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='pinterest')),
                ('linkedin', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Linkedin')),
                ('rss', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='RSS')),
                ('address', djangoplus.db.models.fields.TextField(blank=True, null=True, verbose_name='Endere\xe7o')),
                ('phone_1', djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone Principal')),
                ('phone_2', djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone Secund\xe1rio')),
                ('email', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='E-mail')),
                ('version', djangoplus.db.models.fields.CharField(max_length=255, null=True, verbose_name='Vers\xe3o do Sistema')),
                ('server_address', djangoplus.db.models.fields.CharField(default='http://localhost:8000', max_length=255, verbose_name='Endere\xe7o de Acesso')),
                ('system_email_address', djangoplus.db.models.fields.CharField(default='no-reply@djangoplus.net', max_length=255, verbose_name='E-mail de Notifica\xe7\xe3o')),
                ('company', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Configura\xe7\xe3o',
                'verbose_name_plural': 'Configura\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ascii', djangoplus.db.models.fields.SearchField(blank=True, default='', editable=False)),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='UnitRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.Role', verbose_name='Fun\xe7\xe3o')),
                ('unit', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.Unit', verbose_name='Unidade')),
            ],
            options={
                'verbose_name': 'Fun\xe7\xe3o na Unidade',
                'verbose_name_plural': 'Fun\xe7\xf5es na Unidade',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'verbose_name': 'Grupo',
                'proxy': True,
                'verbose_name_plural': 'Grupos',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', djangoplus.db.models.fields.IntegerField(choices=[[1, 'Cadastro'], [2, 'Edi\xe7\xe3o'], [3, 'Exclus\xe3o']], verbose_name='Opera\xe7\xe3o')),
                ('date', djangoplus.db.models.fields.DateTimeField(auto_now=True, verbose_name='Data/Hora')),
                ('object_id', djangoplus.db.models.fields.IntegerField(verbose_name='Identificador')),
                ('object_description', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Descri\xe7\xe3o do Objeto')),
                ('content', djangoplus.db.models.fields.TextField(null=True, verbose_name='Conte\xfado')),
                ('content_type', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Objeto')),
                ('user', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.CreateModel(
            name='LogIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', djangoplus.db.models.fields.IntegerField(verbose_name='Identificador')),
                ('content_type', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Dado')),
                ('log', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.Log', verbose_name='Log')),
            ],
            options={
                'verbose_name': 'Index',
                'verbose_name_plural': 'Indexes',
            },
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('contenttypes.contenttype',),
            managers=[
                ('objects', djangoplus.admin.models.ContentTypeManager()),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='content_type',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.ContentType', verbose_name='Objeto'),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ascii', djangoplus.db.models.fields.SearchField(blank=True, default='', editable=False)),
            ],
            options={
                'verbose_name': 'Organiza\xe7\xe3o',
                'verbose_name_plural': 'Organiza\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='OrganizationRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.Organization', verbose_name='Organiza\xe7\xe3o')),
                ('role', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.Role', verbose_name='Fun\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Papel na Organiza\xe7\xe3o',
                'verbose_name_plural': 'Papeis na Organiza\xe7\xe3o',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=djangoplus.db.models.fields.BooleanField(default=True, verbose_name='Superusu\xe1rio?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=djangoplus.db.models.fields.CharField(max_length=128, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
            ],
            options={
                'verbose_name': 'Permiss\xe3o',
                'proxy': True,
                'verbose_name_plural': 'Permiss\xf5es',
                'indexes': [],
            },
            bases=('auth.permission',),
        ),
        migrations.AddField(
            model_name='user',
            name='permission_mapping',
            field=djangoplus.db.models.fields.JsonField(null=True, verbose_name='Mapeamento de Permiss\xe3o'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=djangoplus.db.models.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.Organization', verbose_name='Organiza\xe7\xe3o'),
        ),
        migrations.AddField(
            model_name='user',
            name='unit',
            field=djangoplus.db.models.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.Unit', verbose_name='Unidade'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ascii',
            field=djangoplus.db.models.fields.SearchField(blank=True, default='', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='ascii',
            field=djangoplus.db.models.fields.SearchField(blank=True, default='', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ascii',
            field=djangoplus.db.models.fields.SearchField(blank=True, default='', editable=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='ascii',
            field=djangoplus.db.models.fields.SearchField(blank=True, default='', editable=False),
        ),
    ]
