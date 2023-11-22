from django.db import models

# Create your models here.


class Personas(models.Model):
    tIdPersona = models.CharField(max_length=3)
    idPersona = models.CharField(max_length=20)
    nombrePersona = models.CharField(max_length=200)
    personaTaller = models.CharField(max_length=2, default='NO')

    # def __str__(self):
    #     return 'Id:{0}, Nombre:{1}'.format(self.idPersona, self.nombrePersona)
    def __str__(self):
        return self.nombrePersona

    class Meta:
        unique_together = ('tIdPersona','idPersona','nombrePersona')


class Efectivo(models.Model):
    producto = models.CharField(max_length=200)
    titular = models.ForeignKey(Personas, related_name='titular', on_delete=models.CASCADE)
    id2 = models.ForeignKey(Personas, related_name='id2', on_delete=models.CASCADE, blank=True, null=True)
    fechaTransaccion = models.DateField()
    valorTransaccion = models.BigIntegerField()
    Valor_Transaccion = models.CharField(max_length=200,default=0)
    tipoTransaccion = models.CharField(max_length=50)
    nombreBanco = models.CharField(max_length=200)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    ros = models.IntegerField(default=0)
    
    def __str__(self):
        return 'Titular: {0}, Id2: {1}, Fecha: {2}, Valor: {3}, Tipo Transaccion: {4}'.format(self.titular, self.id2, self.fechaTransaccion, self.valorTransaccion, self.tipoTransaccion)

    

class DeclaracionRenta(models.Model):
    anioDeclaracion = models.IntegerField()
    declarante = models.ForeignKey(Personas, related_name='declarante', on_delete=models.CASCADE)
    patrimonioBruto = models.BigIntegerField()
    patrimonio_Bruto = models.CharField(max_length=200,default=0)
    patrimonioLiquido = models.BigIntegerField()
    patrimonio_Liquido = models.CharField(max_length=200,default=0)
    ingresoBruto = models.BigIntegerField()
    ingreso_Bruto = models.CharField(max_length=200,default=0)
    ingresoLiquido = models.BigIntegerField()
    ingreso_Liquido = models.CharField(max_length=200,default=0)
    pasivo = models.BigIntegerField()
    pasivos = models.CharField(max_length=200,default=0)
    gastos = models.BigIntegerField()
    gasto = models.CharField(max_length=200,default=0)
    ros = models.IntegerField(default=0)

    def __str__(self):
        return 'Anho: {0}, Declarante: {1}, Patrimonio Bruto: {2}, Ingreso Bruto: {3}, Pasivo: {4}, Gastos: {5}'.format(self.anioDeclaracion, self.declarante, self.patrimonioBruto, self.ingresoBruto, self.pasivo, self.gastos)

    class Meta:
        unique_together = ('anioDeclaracion','declarante')


class ConfeCamaras(models.Model):
    estadoMatricula = models.CharField(max_length=10, default='ACTIVA') 
    fechaCreacion = models.DateField()
    fechaRenovacionMatricula = models.DateField()
    fechaCancelacionMatricula = models.DateField(blank=True, null=True, default=None)
    empresa = models.ForeignKey(Personas, related_name='empresa', on_delete=models.CASCADE)
    socio = models.ForeignKey(Personas, related_name='socio', on_delete=models.CASCADE)
    composicion = models.CharField(max_length=50, default='Representante Legal')
    ros = models.IntegerField(default=0)

    def __str__(self):
        return 'Fecha creacion: {0}, Fecha renovacion: {1}, Nombre empresa: {2}'.format(self.fechaCreacion, self.fechaRenovacionMatricula, self.empresa)

    class Meta:
        unique_together = ('fechaCreacion','empresa','socio')


class ActosNotariales(models.Model):
    escribanos = models.CharField(max_length=200)
    noEscritura = models.IntegerField()
    fechaEscritura = models.DateField()
    valorTransaccion = models.IntegerField()
    Valor_Transaccion = models.CharField(max_length=100, default=0) 
    personaActo = models.ForeignKey(Personas, related_name='personaActo', on_delete=models.CASCADE)
    claseTramite = models.CharField(max_length=100)
    calidadActo = models.CharField(max_length=200)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    ros = models.IntegerField(default=0)

    def __str__(self):
        return 'Número escritura: {0}, Persona: {1}, Clase Tramite: {2}, Calidad Acto: {3}'.format(self.noEscritura,self.personaActo,self.claseTramite,self.calidadActo)


class Cambiarias(models.Model):
    personaTransaccion = models.ForeignKey(Personas, related_name='personaTransaccion', on_delete=models.CASCADE)
    fechaTransaccion = models.DateField()
    valorTransaccion = models.IntegerField()
    TransaccionValor= models.CharField(max_length=200,default=0)
    nombreTransaccion = models.CharField(max_length=200)
    tipoTransaccion = models.CharField(max_length=100)
    paisTransaccion = models.CharField(max_length=100)
    paisDestino = models.CharField(max_length=100)
    remitente = models.CharField(max_length=200, blank=True, null=True, default=None)
    ros = models.IntegerField(default=0)

    def __str__(self):
        return 'Tipo transaccion: {0}, Valor transaccion: {1}, Fecha transaccion: {2}, Persona: {3}, Pais: {4}, Remitente: {5}'.format(self.tipoTransaccion,self.valorTransaccion,self.fechaTransaccion,self.personaTransaccion,self.paisTransaccion, self.remitente)


class Productos(models.Model):
    bancoProducto = models.CharField(max_length=200)
    producto = models.CharField(max_length=100)
    titularProducto = models.ForeignKey(Personas, related_name='titularProducto', on_delete=models.CASCADE)
    titular2Producto = models.ForeignKey(Personas, related_name='titular2Producto', on_delete=models.CASCADE, blank=True, null=True)
    fechaVinculacion = models.DateField()
    ros = models.IntegerField(default=0)
    noProducto = models.CharField(max_length=100, default=0)

    def __str__(self):
        return 'Banco: {0}, Producto: {1}, Titular: {2}, Titular2: {3}, Fecha Vinculación: {4}'.format(self.bancoProducto,self.producto,self.titularProducto,self.titular2Producto,self.fechaVinculacion)


class RegistroROS(models.Model):
    codigoROS = models.CharField(max_length=50,blank=True)
    fechaReporte = models.DateField()
    bancoReportante = models.CharField(max_length=200,blank=True)
    personaPrincipal = models.ForeignKey(Personas, related_name='personaPrincipal', on_delete=models.CASCADE)
    valorOperacion = models.IntegerField()
    Valor_Operacion = models.CharField(max_length=200,default=0)
    #fechaInicialOperacion = models.DateField(blank=True)
    #fechaFinalOperacion = models.DateField(blank=True, null=True, default=None)
    descripcionOperacion = models.TextField(max_length=6000)
    ros = models.IntegerField(default=0)

    def __str__(self):
        return 'Código ROS: {0}, Fecha Reporte: {1}, Banco Reportante: {2}, Persona Principal: {3}, Valor Operación: {4}, Descripción: {5}'.format(self.codigoROS, self.fechaReporte, self.bancoReportante, self.personaPrincipal, self.valorOperacion,self.descripcionOperacion)


class SeguridadSocial(models.Model):
    tipoid =  models.CharField(max_length=20)
    idBeneficiario =  models.IntegerField(default=0) 
    nombreBeneficiario = models.ForeignKey(Personas, related_name='nombreBeneficiario', on_delete=models.CASCADE)
    edadBeneficiario = models.IntegerField(default=0)
    calidadBeneficiario = models.CharField(max_length=20)
    tipoIdTitular = models.CharField(max_length=20)
    idTitular = models.IntegerField(default=0) 
    nombreTitular = models.CharField(max_length=20)
    edadTitular = models.IntegerField(default=0)
    ros = models.IntegerField(default=0)

    def __str__(self):
        return 'Tipo ID beneficiario: {0}, ID beneficiario: {1}, Nombre beneficiario: {2}, Edad beneficiario: {3}, Calidad beneficiario: {4}, Tipo ID titular: {5}, ID titular: {6}, Nombre titular: {7}, Edad titular: {8}'.format(self.tipoid, self.idBeneficiario, self.nombreBeneficiario, self.edadBeneficiario, self.calidadBeneficiario,self.tipoIdTitular,self.idTitular,self.nombreTitular,self.edadTitular)

