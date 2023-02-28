
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areas(models.Model):
    cve_dep = models.CharField(primary_key=True, max_length=3)
    cve_area = models.CharField(max_length=3)
    nom_area = models.CharField(max_length=40, blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'
        unique_together = (('cve_dep', 'cve_area'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CatTecnicos(models.Model):
    clave = models.CharField(primary_key=True, max_length=5)
    usuario = models.CharField(max_length=50)
    foto = models.BinaryField(blank=True, null=True)
    edo_fisico = models.CharField(max_length=10, blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_tecnicos'


class CatUsuarios(models.Model):
    usuario = models.CharField(primary_key=True, max_length=25)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.
    nombre = models.CharField(max_length=70, blank=True, null=True)
    nivel = models.CharField(max_length=15, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_usuarios'


class Controlfol(models.Model):
    folior = models.IntegerField(blank=True, null=True)
    foliodep = models.IntegerField(blank=True, null=True)
    folioarea = models.IntegerField(blank=True, null=True)
    foliopartes = models.IntegerField(blank=True, null=True)
    foliofallas = models.IntegerField(blank=True, null=True)
    foliotec = models.IntegerField(blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlfol'


class Dependencias(models.Model):
    cve_dep = models.CharField(primary_key=True, max_length=3)
    nom_dep = models.CharField(max_length=40, blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependencias'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estaciona(models.Model):
    cliente = models.CharField(primary_key=True, max_length=5)
    fecha = models.DateField()
    importe = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    referencia = models.CharField(max_length=30, blank=True, null=True)
    pensionado = models.CharField(max_length=60, blank=True, null=True)
    estaciona = models.CharField(max_length=25, blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estaciona'
        unique_together = (('cliente', 'fecha'),)


class Estasube(models.Model):
    cliente = models.CharField(max_length=5, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    importe = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    referencia = models.CharField(max_length=30, blank=True, null=True)
    pensionado = models.CharField(max_length=60, blank=True, null=True)
    estaciona = models.CharField(max_length=25, blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estasube'


class Movfallas(models.Model):
    folio = models.CharField(primary_key=True, max_length=10)
    c4 = models.CharField(max_length=4, blank=True, null=True)
    fecha = models.DateField()
    tfalla = models.CharField(max_length=3)
    serie = models.CharField(max_length=25)
    cve_dep = models.CharField(max_length=3, blank=True, null=True)
    cve_mun = models.CharField(max_length=2, blank=True, null=True)
    cve_area = models.CharField(max_length=3, blank=True, null=True)
    rfsi = models.CharField(max_length=9, blank=True, null=True)
    falla = models.CharField(max_length=50, blank=True, null=True)
    nuevo = models.IntegerField(blank=True, null=True)
    trial391 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movfallas'
        unique_together = (('folio', 'tfalla'),)


class Movpartes(models.Model):
    folio = models.CharField(primary_key=True, max_length=10)
    c4 = models.CharField(max_length=4, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    serie = models.CharField(max_length=25, blank=True, null=True)
    tparte = models.CharField(max_length=3)
    seriem = models.CharField(max_length=25, blank=True, null=True)
    serien = models.CharField(max_length=25, blank=True, null=True)
    cve_mun = models.CharField(max_length=2, blank=True, null=True)
    cve_dep = models.CharField(max_length=3, blank=True, null=True)
    cve_area = models.CharField(max_length=3, blank=True, null=True)
    rfsi = models.CharField(max_length=9, blank=True, null=True)
    parte = models.CharField(max_length=50, blank=True, null=True)
    nuevo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    trial395 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movpartes'
        unique_together = (('folio', 'tparte'),)


class Mserv(models.Model):
    folio = models.CharField(max_length=10)
    c4 = models.CharField(max_length=4, blank=True, null=True)
    fecha = models.DateField()
    tfalla = models.CharField(max_length=3)
    serie = models.CharField(max_length=25)
    tiposerv = models.CharField(max_length=1, blank=True, null=True)
    cvemun = models.CharField(max_length=2, blank=True, null=True)
    cve_dep = models.CharField(max_length=3, blank=True, null=True)
    t_equipo = models.CharField(max_length=1, blank=True, null=True)
    trial395 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mserv'


class Municipios(models.Model):
    cve_mun = models.CharField(primary_key=True, max_length=2)
    nom_mun = models.CharField(max_length=20, blank=True, null=True)
    trial395 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'


class Pdservicios(models.Model):
    folio = models.CharField(primary_key=True, max_length=10)
    c4 = models.CharField(max_length=4, blank=True, null=True)
    tparte = models.CharField(max_length=3)
    seriem = models.CharField(max_length=25, blank=True, null=True)
    serien = models.CharField(max_length=25, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    serierad = models.CharField(max_length=25, blank=True, null=True)
    garantia = models.IntegerField(blank=True, null=True)
    cve_mun = models.CharField(max_length=2, blank=True, null=True)
    cve_dep = models.CharField(max_length=3, blank=True, null=True)
    t_equipo = models.CharField(max_length=1, blank=True, null=True)
    trial395 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdservicios'
        unique_together = (('folio', 'tparte'),)


class Permisos(models.Model):
    usuario = models.CharField(primary_key=True, max_length=25)
    m01 = models.IntegerField(blank=True, null=True)
    m02 = models.IntegerField(blank=True, null=True)
    m03 = models.IntegerField(blank=True, null=True)
    m04 = models.IntegerField(blank=True, null=True)
    m05 = models.IntegerField(blank=True, null=True)
    m06 = models.IntegerField(blank=True, null=True)
    cat01 = models.IntegerField(blank=True, null=True)
    cat02 = models.IntegerField(blank=True, null=True)
    cat03 = models.IntegerField(blank=True, null=True)
    cat04 = models.IntegerField(blank=True, null=True)
    cat05 = models.IntegerField(blank=True, null=True)
    cat06 = models.IntegerField(blank=True, null=True)
    cat07 = models.IntegerField(blank=True, null=True)
    cat08 = models.IntegerField(blank=True, null=True)
    rep01 = models.IntegerField(blank=True, null=True)
    rep02 = models.IntegerField(blank=True, null=True)
    rep03 = models.IntegerField(blank=True, null=True)
    rep04 = models.IntegerField(blank=True, null=True)
    rep05 = models.IntegerField(blank=True, null=True)
    rep06 = models.IntegerField(blank=True, null=True)
    rep07 = models.IntegerField(blank=True, null=True)
    rep08 = models.IntegerField(blank=True, null=True)
    rep09 = models.IntegerField(blank=True, null=True)
    rep10 = models.IntegerField(blank=True, null=True)
    ut01 = models.IntegerField(blank=True, null=True)
    ut02 = models.IntegerField(blank=True, null=True)
    ut03 = models.IntegerField(blank=True, null=True)
    ut04 = models.IntegerField(blank=True, null=True)
    ut05 = models.IntegerField(blank=True, null=True)
    trial398 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos'


class Servicios(models.Model):
    folio = models.CharField(primary_key=True, max_length=10)
    folio_mun = models.CharField(max_length=4, blank=True, null=True)
    f_recepcion = models.DateField()
    nserie = models.CharField(max_length=25, blank=True, null=True)
    h_inicio = models.TimeField(blank=True, null=True)
    h_termino = models.TimeField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    unidad = models.CharField(max_length=15, blank=True, null=True)
    asignado = models.CharField(max_length=1, blank=True, null=True)
    rfsi = models.CharField(max_length=9, blank=True, null=True)
    cve_area = models.CharField(max_length=2, blank=True, null=True)
    cve_dep = models.CharField(max_length=2, blank=True, null=True)
    cve_mun = models.CharField(max_length=4, blank=True, null=True)
    t_equipo = models.CharField(max_length=1, blank=True, null=True)
    ts_aclaves = models.CharField(max_length=1, blank=True, null=True)
    ts_preven = models.CharField(max_length=1, blank=True, null=True)
    ts_correc = models.CharField(max_length=1, blank=True, null=True)
    ts_garantia = models.CharField(max_length=1, blank=True, null=True)
    acciones = models.BinaryField(blank=True, null=True)
    resultados = models.BinaryField(blank=True, null=True)
    ftge = models.DateField(blank=True, null=True)
    ftgr = models.DateField(blank=True, null=True)
    ftgt = models.DateField(blank=True, null=True)
    observaciones = models.BinaryField(blank=True, null=True)
    cve_tecnico = models.CharField(max_length=5, blank=True, null=True)
    archivero = models.CharField(max_length=5, blank=True, null=True)
    cajon = models.CharField(max_length=5, blank=True, null=True)
    carpeta = models.CharField(max_length=5, blank=True, null=True)
    foliomun = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=20, blank=True, null=True)
    nombret = models.CharField(max_length=50, blank=True, null=True)
    serieradio = models.CharField(max_length=25, blank=True, null=True)
    trial398 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'


class Serviciosrad(models.Model):
    folio = models.CharField(primary_key=True, max_length=10)
    c4 = models.CharField(max_length=4, blank=True, null=True)
    f_recepcion = models.DateField()
    f_entrega = models.DateField(blank=True, null=True)
    nserie = models.CharField(max_length=25, blank=True, null=True)
    h_inicio = models.TimeField(blank=True, null=True)
    h_termino = models.TimeField(blank=True, null=True)
    nom_resg = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=40, blank=True, null=True)
    rfsi = models.CharField(max_length=9, blank=True, null=True)
    cve_dep = models.CharField(max_length=3, blank=True, null=True)
    cve_mun = models.CharField(max_length=2, blank=True, null=True)
    t_equipo = models.CharField(max_length=1, blank=True, null=True)
    ts_aclaves = models.CharField(max_length=1, blank=True, null=True)
    ts_preven = models.CharField(max_length=1, blank=True, null=True)
    ts_correc = models.CharField(max_length=1, blank=True, null=True)
    ts_garantia = models.CharField(max_length=1, blank=True, null=True)
    acciones = models.BinaryField(blank=True, null=True)
    observaciones = models.BinaryField(blank=True, null=True)
    ftge = models.DateField(blank=True, null=True)
    ftgr = models.DateField(blank=True, null=True)
    ftgt = models.DateField(blank=True, null=True)
    cve_tecreci = models.CharField(max_length=5, blank=True, null=True)
    cve_tecrepa = models.CharField(max_length=5, blank=True, null=True)
    cve_tecentr = models.CharField(max_length=5, blank=True, null=True)
    ubicacion = models.CharField(max_length=35, blank=True, null=True)
    ent_radio = models.CharField(max_length=50, blank=True, null=True)
    rec_radio = models.CharField(max_length=50, blank=True, null=True)
    serie_carga = models.CharField(max_length=25, blank=True, null=True)
    cve_area = models.CharField(max_length=3, blank=True, null=True)
    oficio = models.CharField(max_length=25, blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True)
    tiporadio = models.CharField(max_length=15, blank=True, null=True)
    trial398 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serviciosrad'


class Tfallas(models.Model):
    tfalla = models.CharField(primary_key=True, max_length=3)
    descrip = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    trial401 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tfallas'


class Tipos(models.Model):
    tipo = models.CharField(primary_key=True, max_length=1)
    descrip = models.CharField(max_length=50)
    trial401 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos'


class Tpartes(models.Model):
    cve_refacc = models.CharField(primary_key=True, max_length=3)
    nom_refacc = models.CharField(max_length=50)
    existencias = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    fecha_adq = models.DateField(blank=True, null=True)
    ult_adq = models.IntegerField(blank=True, null=True)
    trial405 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpartes'