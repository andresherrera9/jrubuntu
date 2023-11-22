import datetime
import numpy as np
import factory
import factory.fuzzy
from . import models, municipios

factory.Faker._DEFAULT_LOCALE = 'es_ES'


class PersonasFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Personas
        django_get_or_create = ('tIdPersona','idPersona','nombrePersona')

    tIdPersona = 'CC'
    idPersona = factory.fuzzy.FuzzyInteger(50000000, 100000000, 12345)
    nombrePersona = factory.Faker('name')


class EfectivoFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Efectivo

    class Params:
        m = municipios.get_random_city()

    # PRODUCTOS = ['Cuenta corriente', 'Cuenta de ahorros']
    # BANCOS = ['BANCO1','BANCO2','BANCO3','BANCO4']

    producto = factory.fuzzy.FuzzyChoice(['Cuenta corriente', 'Cuenta de ahorros'])
    titular = factory.SubFactory(PersonasFactory)
    id2 = factory.SubFactory(PersonasFactory)

    fechaTransaccion = factory.fuzzy.FuzzyDate(datetime.date(2009, 1, 1), datetime.date(2019, 5, 31))
    valorTransaccion = factory.fuzzy.FuzzyInteger(10000000,100000000)
    tipoTransaccion = factory.Iterator(['Retiro','Depósito'])
    nombreBanco = factory.fuzzy.FuzzyChoice(['BANCO DIAMANTE','BANCO ESMERALDA','BANCO ZAFIRO','BANCO PLATA'])
    departamento = factory.LazyAttribute(lambda x: x.m[0])
    municipio = factory.LazyAttribute(lambda x: x.m[1])


class DeclaracionRentaFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.DeclaracionRenta

    anioDeclaracion = factory.Iterator(np.arange(2009,2018,1))
    declarante = factory.SubFactory(PersonasFactory)
    patrimonioBruto = factory.fuzzy.FuzzyInteger(10000000,100000000)
    patrimonioLiquido = factory.LazyAttribute(lambda x: abs(x.patrimonioBruto - np.random.randint(10000000,100000000,1)))
    ingresoBruto = factory.fuzzy.FuzzyInteger(10000000,100000000)
    ingresoLiquido = factory.LazyAttribute(lambda x: abs(x.ingresoBruto - np.random.randint(10000000,100000000,1)))
    pasivo = factory.LazyAttribute(lambda x: x.patrimonioBruto - x.ingresoLiquido)
    gastos = factory.fuzzy.FuzzyInteger(10000000,100000000)



class ConfeCamarasFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ConfeCamaras

    fechaCreacion = factory.fuzzy.FuzzyDate(datetime.date(2009, 1, 1), datetime.date(2017, 1, 31))
    fechaRenovacionMatricula = factory.fuzzy.FuzzyDate(datetime.date(2017, 1, 31), datetime.date.today())
    empresa = factory.SubFactory(PersonasFactory, tIdPersona='NIT', nombrePersona=factory.Faker('company'))
    socio = factory.SubFactory(PersonasFactory)


class ActosNotarialesFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ActosNotariales

    class Params:
        m = municipios.get_random_city()

    nombreNotaria = factory.fuzzy.FuzzyChoice(['NOTARIA PRIMERA','NOTARIA SEGUNDA','NOTARIA TERCERA','NOTARIA CUARTA'])
    noEscritura = factory.fuzzy.FuzzyInteger(100,10000)
    fechaEscritura = factory.fuzzy.FuzzyDate(datetime.date(2009, 1, 1), datetime.date(2017, 1, 31))
    valorTransaccion = factory.fuzzy.FuzzyInteger(10000000,100000000)
    personaActo = factory.SubFactory(PersonasFactory)
    claseTramite = 'Compraventa'
    calidadActo = factory.fuzzy.FuzzyChoice(['Comprador','Vendedor','Otro'])
    departamento = factory.LazyAttribute(lambda x: x.m[0])
    municipio = factory.LazyAttribute(lambda x: x.m[1])


class CambiariasFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Cambiarias

    personaTransaccion = factory.SubFactory(PersonasFactory)
    fechaTransaccion = factory.fuzzy.FuzzyDate(datetime.date(2009, 1, 1), datetime.date(2017, 1, 31))
    valorTransaccion = factory.fuzzy.FuzzyInteger(10000000,100000000)
    nombreTransaccion = factory.fuzzy.FuzzyChoice(['Anticipo por exportaciones de bienes','Anticipo por importaciones de bienes','Remesas de trabajadores'])
    tipoTransaccion = factory.fuzzy.FuzzyChoice(['Ingresos','Egresos'])
    paisTransaccion = factory.fuzzy.FuzzyChoice(['Estados Unidos','Jamaica','Perú','México','El Salvador','China','Rusia','Venezuela'])


class ProductosFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Productos

    # PRODUCTOS = ['Cuenta de ahorros', 'Cuenta corriente', 'Tarjeta de crédito']

    bancoProducto = factory.fuzzy.FuzzyChoice(['BANCO DIAMANTE', 'BANCO ESMERALDA', 'BANCO ZAFIRO', 'BANCO PLATA'])
    producto = factory.fuzzy.FuzzyChoice(['Cuenta de ahorros', 'Cuenta corriente', 'Tarjeta de crédito'])
    titularProducto = factory.SubFactory(PersonasFactory)
    titular2Producto = factory.SubFactory(PersonasFactory)
    fechaVinculacion = factory.fuzzy.FuzzyDate(datetime.date(2009, 1, 1), datetime.date(2017, 1, 31))