import django_tables2 as tables
from .models import Personas, Efectivo, ConfeCamaras, DeclaracionRenta, ActosNotariales, Cambiarias, Productos, RegistroROS, SeguridadSocial


class EfectivoTable(tables.Table):
    class Meta:
        model = Efectivo
        fields = ('producto','titular','id2','fechaTransaccion','Valor_Transaccion','tipoTransaccion','nombreBanco','departamento','municipio')
        template_name = 'django_tables2/bootstrap4.html'


class ConfeCamarasTable(tables.Table):
    class Meta:
        model = ConfeCamaras
        fields = ('estadoMatricula', 'fechaCreacion', 'fechaRenovacionMatricula', 'fechaCancelacionMatricula', 'empresa', 'socio', 'composicion')
        template_name = 'django_tables2/bootstrap4.html'


class DeclaracionRentaTable(tables.Table):
    class Meta:
        model = DeclaracionRenta
        fields = ('anioDeclaracion', 'declarante', 'patrimonio_Bruto', 'patrimonio_Liquido', 'ingreso_Bruto', 'ingreso_Liquido', 'pasivos', 'gasto')
        template_name = 'django_tables2/bootstrap4.html'


class ActosNotarialesTable(tables.Table):
    class Meta:
        model = ActosNotariales
        fields = ('escribanos', 'noEscritura', 'fechaEscritura', 'Valor_Transaccion', 'personaActo', 'claseTramite','calidadActo','departamento','municipio')
        template_name = 'django_tables2/bootstrap4.html'


class CambiariasTable(tables.Table):
    class Meta:
        model = Cambiarias
        fields = ('personaTransaccion','tipoTransaccion','fechaTransaccion','TransaccionValor','nombreTransaccion','paisTransaccion','paisDestino','remitente')
        #fields = ('personaTransaccion','fechaTransaccion','valorTransaccion','nombreTransaccion', 'tipoTransaccion','paisTransaccion','remitente')
        template_name = 'django_tables2/bootstrap4.html'


class ProductosTable(tables.Table):
    class Meta:
        model = Productos
        fields = ('bancoProducto', 'producto','titularProducto','titular2Producto','fechaVinculacion')
        template_name = 'django_tables2/bootstrap4.html'


class RegistroROSTable(tables.Table):
    class Meta:
        model = RegistroROS
        fields = ('codigoROS','fechaReporte','personaPrincipal','Valor_Operacion','descripcionOperacion')
        template_name = 'django_tables2/bootstrap4.html'

class SeguridadSocialTable(tables.Table):
    class Meta:
        model = SeguridadSocial
        fields = ('tipoid','idBeneficiario','nombreBeneficiario','edadBeneficiario','calidadBeneficiario','tipoIdTitular','idTitular','nombreTitular','edadTitular')
        template_name = 'django_tables2/bootstrap4.html'