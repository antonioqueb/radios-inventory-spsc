
from rest_framework.serializers import ModelSerializer
from servicios.models import *


class AreasSerializer(ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class AuthGroupSerializer(ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'

class AuthGroupPermissionsSerializer(ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'

class AuthPermissionSerializer(ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'

class AuthUserSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class AuthUserGroupsSerializer(ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'

class AuthUserUserPermissionsSerializer(ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'

class CatTecnicosSerializer(ModelSerializer):
    class Meta:
        model = CatTecnicos
        fields = '__all__'

class CatUsuariosSerializer(ModelSerializer):
    class Meta:
        model = CatUsuarios
        fields = '__all__'

class ControlfolSerializer(ModelSerializer):
    class Meta:
        model = Controlfol
        fields = '__all__'

class DependenciasSerializer(ModelSerializer):
    class Meta:
        model = Dependencias
        fields = '__all__'

class DjangoAdminLogSerializer(ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'

class DjangoContentTypeSerializer(ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'

class DjangoMigrationsSerializer(ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'

class DjangoSessionSerializer(ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'

class EstacionaSerializer(ModelSerializer):
    class Meta:
        model = Estaciona
        fields = '__all__'

class EstasubeSerializer(ModelSerializer):
    class Meta:
        model = Estasube
        fields = '__all__'

class MovfallasSerializer(ModelSerializer):
    class Meta:
        model = Movfallas
        fields = '__all__'

class MovpartesSerializer(ModelSerializer):
    class Meta:
        model = Movpartes
        fields = '__all__'

class MservSerializer(ModelSerializer):
    class Meta:
        model = Mserv
        fields = '__all__'

class MunicipiosSerializer(ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'

class PdserviciosSerializer(ModelSerializer):
    class Meta:
        model = Pdservicios
        fields = '__all__'

class PermisosSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = '__all__'

class ServiciosSerializer(ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

class ServiciosradSerializer(ModelSerializer):
    class Meta:
        model = Serviciosrad
        fields = '__all__'

class TfallasSerializer(ModelSerializer):
    class Meta:
        model = Tfallas
        fields = '__all__'

class TiposSerializer(ModelSerializer):
    class Meta:
        model = Tipos
        fields = '__all__'

class TpartesSerializer(ModelSerializer):
    class Meta:
        model = Tpartes
        fields = '__all__'

