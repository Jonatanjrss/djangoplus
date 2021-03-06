# Generated by Django 2.1.7 on 2019-03-07 16:56

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0009_auto_20190212_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Grupos'},
        ),
        migrations.AlterModelOptions(
            name='logindex',
            options={'verbose_name': 'Índices', 'verbose_name_plural': 'Índices'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Organização', 'verbose_name_plural': 'Organizações'},
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name': 'Permissão', 'verbose_name_plural': 'Permissões'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Função', 'verbose_name_plural': 'Funções'},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Escopo', 'verbose_name_plural': 'Escopos'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Configurações', 'verbose_name_plural': 'Configurações'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Unidade', 'verbose_name_plural': 'Unidades'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Login', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='log',
            name='content',
            field=djangoplus.db.models.fields.TextField(null=True, verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='log',
            name='content_type',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.ContentType', verbose_name='Objeto'),
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=djangoplus.db.models.fields.DateTimeField(auto_now=True, verbose_name='Data/Hora'),
        ),
        migrations.AlterField(
            model_name='log',
            name='object_description',
            field=djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Descrição do Objeto'),
        ),
        migrations.AlterField(
            model_name='log',
            name='object_id',
            field=djangoplus.db.models.fields.IntegerField(verbose_name='Identificação'),
        ),
        migrations.AlterField(
            model_name='log',
            name='operation',
            field=djangoplus.db.models.fields.IntegerField(choices=[[1, 'Cadastrar'], [2, 'Editar'], [3, 'Excluir']], verbose_name='Operação'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Login'),
        ),
        migrations.AlterField(
            model_name='logindex',
            name='content_type',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Objeto'),
        ),
        migrations.AlterField(
            model_name='logindex',
            name='object_id',
            field=djangoplus.db.models.fields.IntegerField(verbose_name='Identificação'),
        ),
        migrations.AlterField(
            model_name='role',
            name='active',
            field=djangoplus.db.models.fields.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='role',
            name='group',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.Group', verbose_name='Perfil'),
        ),
        migrations.AlterField(
            model_name='role',
            name='scope',
            field=djangoplus.db.models.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.Scope', verbose_name='Escopo'),
        ),
        migrations.AlterField(
            model_name='role',
            name='user',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Login'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='address',
            field=djangoplus.db.models.fields.TextField(blank=True, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='company',
            field=djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Nome da Empresa'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='icon',
            field=djangoplus.db.models.fields.ImageField(blank=True, default='blank.png', null=True, upload_to='config', verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='initials',
            field=djangoplus.db.models.fields.CharField(default='Django+', max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=djangoplus.db.models.fields.ImageField(blank=True, default='', null=True, upload_to='config', verbose_name='Logotipo'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo_pdf',
            field=djangoplus.db.models.fields.ImageField(blank=True, default='', help_text='Imagem sem plano de fundo', null=True, upload_to='config', verbose_name='Logotipo para PDF'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='name',
            field=djangoplus.db.models.fields.CharField(default='Django Plus', max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone_1',
            field=djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone Principal'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone_2',
            field=djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone Secundário'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='server_address',
            field=djangoplus.db.models.fields.CharField(default='http://localhost:8000', max_length=255, verbose_name='URL do Servidor'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='system_email_address',
            field=djangoplus.db.models.fields.CharField(default='no-reply@djangoplus.net', max_length=255, verbose_name='E-amil de Notificação'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='version',
            field=djangoplus.db.models.fields.CharField(max_length=255, null=True, verbose_name='Versão do Sistema'),
        ),
        migrations.AlterField(
            model_name='user',
            name='active',
            field=djangoplus.db.models.fields.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=djangoplus.db.models.fields.CharField(blank=True, max_length=30, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='permission_mapping',
            field=djangoplus.db.models.fields.JsonField(null=True, verbose_name='Mapeamento de Permissões'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=djangoplus.db.models.fields.ImageField(blank=True, default='user.png', null=True, upload_to='profiles', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=djangoplus.db.models.fields.CharField(max_length=30, unique=True, verbose_name='Login'),
        ),
    ]
