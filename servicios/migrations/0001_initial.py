# Generated by Django 4.1.7 on 2023-02-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('cve_dep', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('cve_area', models.CharField(max_length=3)),
                ('nom_area', models.CharField(blank=True, max_length=40, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'areas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CatTecnicos',
            fields=[
                ('clave', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=50)),
                ('foto', models.BinaryField(blank=True, null=True)),
                ('edo_fisico', models.CharField(blank=True, max_length=10, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'cat_tecnicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CatUsuarios',
            fields=[
                ('usuario', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('pass_field', models.CharField(db_column='pass', max_length=50)),
                ('nombre', models.CharField(blank=True, max_length=70, null=True)),
                ('nivel', models.CharField(blank=True, max_length=15, null=True)),
                ('foto', models.BinaryField(blank=True, null=True)),
                ('estatus', models.CharField(blank=True, max_length=10, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'cat_usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Controlfol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folior', models.IntegerField(blank=True, null=True)),
                ('foliodep', models.IntegerField(blank=True, null=True)),
                ('folioarea', models.IntegerField(blank=True, null=True)),
                ('foliopartes', models.IntegerField(blank=True, null=True)),
                ('foliofallas', models.IntegerField(blank=True, null=True)),
                ('foliotec', models.IntegerField(blank=True, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'controlfol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dependencias',
            fields=[
                ('cve_dep', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nom_dep', models.CharField(blank=True, max_length=40, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'dependencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estaciona',
            fields=[
                ('cliente', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('importe', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('referencia', models.CharField(blank=True, max_length=30, null=True)),
                ('pensionado', models.CharField(blank=True, max_length=60, null=True)),
                ('estaciona', models.CharField(blank=True, max_length=25, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'estaciona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estasube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=5, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('importe', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('referencia', models.CharField(blank=True, max_length=30, null=True)),
                ('pensionado', models.CharField(blank=True, max_length=60, null=True)),
                ('estaciona', models.CharField(blank=True, max_length=25, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'estasube',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movfallas',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c4', models.CharField(blank=True, max_length=4, null=True)),
                ('fecha', models.DateField()),
                ('tfalla', models.CharField(max_length=3)),
                ('serie', models.CharField(max_length=25)),
                ('cve_dep', models.CharField(blank=True, max_length=3, null=True)),
                ('cve_mun', models.CharField(blank=True, max_length=2, null=True)),
                ('cve_area', models.CharField(blank=True, max_length=3, null=True)),
                ('rfsi', models.CharField(blank=True, max_length=9, null=True)),
                ('falla', models.CharField(blank=True, max_length=50, null=True)),
                ('nuevo', models.IntegerField(blank=True, null=True)),
                ('trial391', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'movfallas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movpartes',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c4', models.CharField(blank=True, max_length=4, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('serie', models.CharField(blank=True, max_length=25, null=True)),
                ('tparte', models.CharField(max_length=3)),
                ('seriem', models.CharField(blank=True, max_length=25, null=True)),
                ('serien', models.CharField(blank=True, max_length=25, null=True)),
                ('cve_mun', models.CharField(blank=True, max_length=2, null=True)),
                ('cve_dep', models.CharField(blank=True, max_length=3, null=True)),
                ('cve_area', models.CharField(blank=True, max_length=3, null=True)),
                ('rfsi', models.CharField(blank=True, max_length=9, null=True)),
                ('parte', models.CharField(blank=True, max_length=50, null=True)),
                ('nuevo', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('trial395', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'movpartes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=10)),
                ('c4', models.CharField(blank=True, max_length=4, null=True)),
                ('fecha', models.DateField()),
                ('tfalla', models.CharField(max_length=3)),
                ('serie', models.CharField(max_length=25)),
                ('tiposerv', models.CharField(blank=True, max_length=1, null=True)),
                ('cvemun', models.CharField(blank=True, max_length=2, null=True)),
                ('cve_dep', models.CharField(blank=True, max_length=3, null=True)),
                ('t_equipo', models.CharField(blank=True, max_length=1, null=True)),
                ('trial395', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'mserv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('cve_mun', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nom_mun', models.CharField(blank=True, max_length=20, null=True)),
                ('trial395', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'municipios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pdservicios',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c4', models.CharField(blank=True, max_length=4, null=True)),
                ('tparte', models.CharField(max_length=3)),
                ('seriem', models.CharField(blank=True, max_length=25, null=True)),
                ('serien', models.CharField(blank=True, max_length=25, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('serierad', models.CharField(blank=True, max_length=25, null=True)),
                ('garantia', models.IntegerField(blank=True, null=True)),
                ('cve_mun', models.CharField(blank=True, max_length=2, null=True)),
                ('cve_dep', models.CharField(blank=True, max_length=3, null=True)),
                ('t_equipo', models.CharField(blank=True, max_length=1, null=True)),
                ('trial395', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'pdservicios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('usuario', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('m01', models.IntegerField(blank=True, null=True)),
                ('m02', models.IntegerField(blank=True, null=True)),
                ('m03', models.IntegerField(blank=True, null=True)),
                ('m04', models.IntegerField(blank=True, null=True)),
                ('m05', models.IntegerField(blank=True, null=True)),
                ('m06', models.IntegerField(blank=True, null=True)),
                ('cat01', models.IntegerField(blank=True, null=True)),
                ('cat02', models.IntegerField(blank=True, null=True)),
                ('cat03', models.IntegerField(blank=True, null=True)),
                ('cat04', models.IntegerField(blank=True, null=True)),
                ('cat05', models.IntegerField(blank=True, null=True)),
                ('cat06', models.IntegerField(blank=True, null=True)),
                ('cat07', models.IntegerField(blank=True, null=True)),
                ('cat08', models.IntegerField(blank=True, null=True)),
                ('rep01', models.IntegerField(blank=True, null=True)),
                ('rep02', models.IntegerField(blank=True, null=True)),
                ('rep03', models.IntegerField(blank=True, null=True)),
                ('rep04', models.IntegerField(blank=True, null=True)),
                ('rep05', models.IntegerField(blank=True, null=True)),
                ('rep06', models.IntegerField(blank=True, null=True)),
                ('rep07', models.IntegerField(blank=True, null=True)),
                ('rep08', models.IntegerField(blank=True, null=True)),
                ('rep09', models.IntegerField(blank=True, null=True)),
                ('rep10', models.IntegerField(blank=True, null=True)),
                ('ut01', models.IntegerField(blank=True, null=True)),
                ('ut02', models.IntegerField(blank=True, null=True)),
                ('ut03', models.IntegerField(blank=True, null=True)),
                ('ut04', models.IntegerField(blank=True, null=True)),
                ('ut05', models.IntegerField(blank=True, null=True)),
                ('trial398', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'permisos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('folio_mun', models.CharField(blank=True, max_length=4, null=True)),
                ('f_recepcion', models.DateField()),
                ('nserie', models.CharField(blank=True, max_length=25, null=True)),
                ('h_inicio', models.TimeField(blank=True, null=True)),
                ('h_termino', models.TimeField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.CharField(blank=True, max_length=40, null=True)),
                ('unidad', models.CharField(blank=True, max_length=15, null=True)),
                ('asignado', models.CharField(blank=True, max_length=1, null=True)),
                ('rfsi', models.CharField(blank=True, max_length=9, null=True)),
                ('cve_area', models.CharField(blank=True, max_length=2, null=True)),
                ('cve_dep', models.CharField(blank=True, max_length=2, null=True)),
                ('cve_mun', models.CharField(blank=True, max_length=4, null=True)),
                ('t_equipo', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_aclaves', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_preven', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_correc', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_garantia', models.CharField(blank=True, max_length=1, null=True)),
                ('acciones', models.BinaryField(blank=True, null=True)),
                ('resultados', models.BinaryField(blank=True, null=True)),
                ('ftge', models.DateField(blank=True, null=True)),
                ('ftgr', models.DateField(blank=True, null=True)),
                ('ftgt', models.DateField(blank=True, null=True)),
                ('observaciones', models.BinaryField(blank=True, null=True)),
                ('cve_tecnico', models.CharField(blank=True, max_length=5, null=True)),
                ('archivero', models.CharField(blank=True, max_length=5, null=True)),
                ('cajon', models.CharField(blank=True, max_length=5, null=True)),
                ('carpeta', models.CharField(blank=True, max_length=5, null=True)),
                ('foliomun', models.IntegerField(blank=True, null=True)),
                ('alias', models.CharField(blank=True, max_length=20, null=True)),
                ('nombret', models.CharField(blank=True, max_length=50, null=True)),
                ('serieradio', models.CharField(blank=True, max_length=25, null=True)),
                ('trial398', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'servicios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serviciosrad',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c4', models.CharField(blank=True, max_length=4, null=True)),
                ('f_recepcion', models.DateField()),
                ('f_entrega', models.DateField(blank=True, null=True)),
                ('nserie', models.CharField(blank=True, max_length=25, null=True)),
                ('h_inicio', models.TimeField(blank=True, null=True)),
                ('h_termino', models.TimeField(blank=True, null=True)),
                ('nom_resg', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.CharField(blank=True, max_length=40, null=True)),
                ('rfsi', models.CharField(blank=True, max_length=9, null=True)),
                ('cve_dep', models.CharField(blank=True, max_length=3, null=True)),
                ('cve_mun', models.CharField(blank=True, max_length=2, null=True)),
                ('t_equipo', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_aclaves', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_preven', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_correc', models.CharField(blank=True, max_length=1, null=True)),
                ('ts_garantia', models.CharField(blank=True, max_length=1, null=True)),
                ('acciones', models.BinaryField(blank=True, null=True)),
                ('observaciones', models.BinaryField(blank=True, null=True)),
                ('ftge', models.DateField(blank=True, null=True)),
                ('ftgr', models.DateField(blank=True, null=True)),
                ('ftgt', models.DateField(blank=True, null=True)),
                ('cve_tecreci', models.CharField(blank=True, max_length=5, null=True)),
                ('cve_tecrepa', models.CharField(blank=True, max_length=5, null=True)),
                ('cve_tecentr', models.CharField(blank=True, max_length=5, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=35, null=True)),
                ('ent_radio', models.CharField(blank=True, max_length=50, null=True)),
                ('rec_radio', models.CharField(blank=True, max_length=50, null=True)),
                ('serie_carga', models.CharField(blank=True, max_length=25, null=True)),
                ('cve_area', models.CharField(blank=True, max_length=3, null=True)),
                ('oficio', models.CharField(blank=True, max_length=25, null=True)),
                ('estatus', models.CharField(blank=True, max_length=10, null=True)),
                ('tiporadio', models.CharField(blank=True, max_length=15, null=True)),
                ('trial398', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'serviciosrad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tfallas',
            fields=[
                ('tfalla', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('descrip', models.CharField(max_length=50)),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
                ('categoria', models.CharField(blank=True, max_length=10, null=True)),
                ('trial401', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'tfallas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('tipo', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descrip', models.CharField(max_length=50)),
                ('trial401', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tpartes',
            fields=[
                ('cve_refacc', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nom_refacc', models.CharField(max_length=50)),
                ('existencias', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_adq', models.DateField(blank=True, null=True)),
                ('ult_adq', models.IntegerField(blank=True, null=True)),
                ('trial405', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'tpartes',
                'managed': False,
            },
        ),
    ]