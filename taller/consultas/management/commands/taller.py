from django.core.management.base import BaseCommand
from consultas.factories import PersonasFactory, EfectivoFactory, DeclaracionRentaFactory, ConfeCamarasFactory, ActosNotarialesFactory, CambiariasFactory, ProductosFactory
from consultas.models import Personas, Efectivo, DeclaracionRenta, ConfeCamaras, ActosNotariales, Cambiarias, Productos
import numpy as np
import datetime
import factory

factory.Faker._DEFAULT_LOCALE = 'es_ES'


class Command(BaseCommand):
    help = 'Poblar la base de datos con información del taller'

    def add_arguments(self, parser):
        parser.add_argument('--pathfile', default='None', type=str, help='Ruta en donde se encuentran los archivos para llenar las tablas de información')

    def handle(self, *args, **options):
        self.stdout.write('Alimentando la base de datos con los datos del taller.....')
        llenar_datos_taller(self,options['pathfile'])
        self.stdout.write('Proceso terminado.')


def get_personas_listado():
    personas = {
        'EPCS ':('NIT','904056213','Almacenes EPCS SAS'),
        'JCMA':('NIT','903123123','Inversiones JCMA S.A.'),
        'CCNV': ('NIT', '900123321', 'Consorcio CNV'),
        'EXFI': ('NIT', '901597012', 'EXPOFICTI SAS'),
        'CC1': ('NIT', '900123320', 'Consorciado 1'),
        'CC2': ('NIT', '900123319', 'Consorciado 2'),
        'DANTE':('CC','82761030','Dante Escobar'),
        'MELISSA':('CC','61224799','Melissa Bustos'),
        'MAURICIO':('CC','77969003','Mauricio Ramirez'),
        'QUIMERA':('CC','50048910','Quimera Barrios'),
        'NICANOR':('CC','64505797','Nicanor Suarez'),
        'PARRA':('CC','56076882','Parra Mercado'),
        'YAMIN':('CC','79746443','Yamin Bustos'),
        'MERCADO':('CC','66828069','Mercado Ascensio'),
        'CAMILO': ('CC', '80123321', 'Camilo Aragón'),
        'MILTON': ('CC', '80123322', 'Milton Pérez'),
        'FERNANDO': ('CC', '1230789456', 'Fernando Fernandéz'),
        'PEDRO': ('CC', '140795', 'Pedro Pedroza'),
        'JAIME': ('CC', '79564879', 'Jaime Sanabria'),
        'MANUEL': ('CC', '69087218', 'Manuel Salazar')
    }

    return personas


def get_transacciones_efectivo():
    txefectivo = {
        '903123123' : (
            ('Cuenta Corriente', '904056213', datetime.datetime.strptime('05/25/2017', '%m/%d/%Y').date(), 75000000,
             'Depósito', 'BANCO PLATA', 'Norte de Santander', 'Ocaña'),
            ('Cuenta Corriente', '904056213', datetime.datetime.strptime('05/29/2017', '%m/%d/%Y').date(), 55000000,
             'Depósito', 'BANCO PLATA', 'Norte de Santander', 'Tibu'),
            ('Cuenta Corriente', '904056213', datetime.datetime.strptime('06/01/2017', '%m/%d/%Y').date(), 120000000,
             'Depósito', 'BANCO PLATA', 'Norte de Santander', 'Cúcuta'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('06/29/2017', '%m/%d/%Y').date(), 270000000,
             'Retiro', 'BANCO ZAFIRO', 'Bogotá', 'Bogotá'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/29/2017', '%m/%d/%Y').date(), 54894990, 'Retiro',
            'BANCO ZAFIRO', 'Valle', 'Cali'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/02/2017', '%m/%d/%Y').date(), 50000000, 'Retiro',
            'BANCO ZAFIRO', 'Caquetá', 'Florencia'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/08/2017', '%m/%d/%Y').date(), 13273548, 'Retiro',
            'BANCO ZAFIRO', 'Caquetá', 'Florencia'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('06/13/2017', '%m/%d/%Y').date(), 9940000, 'Retiro',
             'BANCO ZAFIRO', 'Caquetá', 'Florencia'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('06/13/2017', '%m/%d/%Y').date(), 9960000, 'Retiro',
             'BANCO ZAFIRO', 'Caquetá', 'Florencia'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('06/13/2017', '%m/%d/%Y').date(), 9950000, 'Retiro',
             'BANCO ZAFIRO', 'Caquetá', 'Florencia'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/05/2017', '%m/%d/%Y').date(), 61200000, 'Retiro',
            'BANCO ZAFIRO', 'Nariño', 'Ipiales'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('06/07/2017', '%m/%d/%Y').date(), 106746460,
             'Retiro', 'BANCO ZAFIRO', 'Nariño', 'Ipiales'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/07/2017', '%m/%d/%Y').date(), 30680000, 'Retiro',
            'BANCO ZAFIRO', 'Putumayo', 'Mocoa'),
            ('Cuenta Corriente', '69087218', datetime.datetime.strptime('06/08/2017', '%m/%d/%Y').date(), 182280000,
             'Retiro', 'BANCO ZAFIRO', 'Putumayo', 'Mocoa'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('06/09/2017', '%m/%d/%Y').date(), 3000000, 'Retiro',
             'BANCO ZAFIRO', 'Putumayo', 'Mocoa'),
            (
            'Cuenta Corriente', '69087218', datetime.datetime.strptime('06/28/2017', '%m/%d/%Y').date(), 80000000, 'Retiro',
            'BANCO ZAFIRO', 'Putumayo', 'Mocoa'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/08/2017', '%m/%d/%Y').date(), 50000000, 'Retiro',
            'BANCO ZAFIRO', 'Nariño', 'Pasto'),
            (
            'Cuenta Corriente', 'None', datetime.datetime.strptime('06/20/2017', '%m/%d/%Y').date(), 68339490, 'Retiro',
            'BANCO ZAFIRO', 'Nariño', 'Pasto')
        ),
        '901597012': (
            ('Cuenta Corriente', '1230789456', datetime.datetime.strptime('05/15/2016', '%m/%d/%Y').date(), 1250000000, 'Retiro', 'BANCO DIAMANTE', 'Santander', 'Bucaramanga'),
            ('Cuenta Corriente', 'None', datetime.datetime.strptime('05/15/2016', '%m/%d/%Y').date(), 550286000,
             'Retiro', 'BANCO DIAMANTE', 'Santander', 'Bucaramanga')
        )
    }

    return txefectivo


def get_actos_notariales():
    actosNotariales = {
        '82761030': (
            ('NOTARIA SEGUNDA', 9583, datetime.datetime.strptime('12/26/2015', '%m/%d/%Y').date(), 300000000, 'Compraventa', 'COMPRADOR', 'Meta', 'Villavicencio'),
            ('NOTARIA PRIMERA', 6723, datetime.datetime.strptime('05/15/2017', '%m/%d/%Y').date(), 500000000, 'Compraventa', 'VENDEDOR', 'Meta', 'Villavicencio')
        ),
        '77969003' : (
            ('NOTARIA PRIMERA', 6723, datetime.datetime.strptime('05/15/2017', '%m/%d/%Y').date(), 500000000, 'Compraventa', 'COMPRADOR', 'Meta', 'Villavicencio')
        ),
        '61224799' : (
            ('NOTARIA SEGUNDA', 9583, datetime.datetime.strptime('12/26/2015', '%m/%d/%Y').date(), 300000000, 'Compraventa', 'VENDEDOR', 'Meta', 'Villavicencio')
        )
    }
    return actosNotariales


def get_confecamaras():
    confecamaras = {
        '904056213' : (
            (datetime.datetime.strptime('12/15/2015', '%m/%d/%Y').date(), '50048910', 'Representante Legal'),
            (datetime.datetime.strptime('12/15/2015', '%m/%d/%Y').date(), '69087218', 'Socio')
        ),
        '903123123' : (
            (datetime.datetime.strptime('01/31/2017', '%m/%d/%Y').date(), '69087218', 'Representante Legal'),
            (datetime.datetime.strptime('01/31/2017', '%m/%d/%Y').date(), '64505797', 'Socio'),
            (datetime.datetime.strptime('01/31/2017', '%m/%d/%Y').date(), '56076882', 'Socio'),
            (datetime.datetime.strptime('01/31/2017', '%m/%d/%Y').date(), '82761030', 'Socio'),
            (datetime.datetime.strptime('01/31/2017', '%m/%d/%Y').date(), '79746443', 'Socio'),
            (datetime.datetime.strptime('01/31/2017', '%m/%d/%Y').date(), '66828069', 'Socio')
        ),
        '900123321' : (
            (datetime.datetime.strptime('01/15/2015', '%m/%d/%Y').date(), '80123322', 'Representante Legal'),
            (datetime.datetime.strptime('01/15/2015', '%m/%d/%Y').date(), '900123320', 'Socio'),
            (datetime.datetime.strptime('01/15/2015', '%m/%d/%Y').date(), '900123319', 'Socio')
        ),
        '900123320' : (
            (datetime.datetime.strptime('02/02/2014', '%m/%d/%Y').date(), '80123321', 'Representante Legal')
        ),
        '900123319': (
            (datetime.datetime.strptime('02/02/2014', '%m/%d/%Y').date(), '80123322', 'Representante Legal')
        ),
        '901597012' : (
            (datetime.datetime.strptime('12/21/2015', '%m/%d/%Y').date(), '140795', 'Representante Legal')
        ),
    }
    return confecamaras


def get_declaracion_renta():
    renta = {
        '904056213' : (
            (2015, 10000000, 0, 0, 0),
            (2016, 10000000, 0, 0, 0)
        ),
        '82761030' : (
            (2014, 0, 0, 0, 0),
            (2015, 0, 0, 0, 0),
            (2016, 50000000, 30000000, 0, 25000000)
        )
    }
    return renta


def get_transacciones_cambiarias():
    cambiarias = {
        '904056213' : (
            (datetime.datetime.strptime('03/02/2015', '%m/%d/%Y').date(), 5008008, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('10/02/2015', '%m/%d/%Y').date(), 999480, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('10/08/2015', '%m/%d/%Y').date(), 1999572, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('10/31/2015', '%m/%d/%Y').date(), 5180698, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('11/07/2015', '%m/%d/%Y').date(), 2985528, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (
            datetime.datetime.strptime('02/14/2016', '%m/%d/%Y').date(), 33696557, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (
            datetime.datetime.strptime('03/08/2016', '%m/%d/%Y').date(), 46836826, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('08/09/2016', '%m/%d/%Y').date(), 6130500, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (
            datetime.datetime.strptime('08/17/2016', '%m/%d/%Y').date(), 39380000, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('08/29/2016', '%m/%d/%Y').date(), 4982779, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None'),
            (datetime.datetime.strptime('09/20/2016', '%m/%d/%Y').date(), 4999992, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Panamá', 'None')
        ),
        '901597012' : (
            (datetime.datetime.strptime('05/11/2016', '%m/%d/%Y').date(), 815375000, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Estados Unidos', 'None'),
            (datetime.datetime.strptime('05/12/2016', '%m/%d/%Y').date(), 1027250000, 'Anticipo por exportaciones de bienes', 'Ingresos', 'Estados Unidos', 'None')
        )
    }
    return cambiarias


def get_productos():
    productos = {
        '903123123': (
            ('BANCO PLATA', 'Cuenta Corriente','None',datetime.datetime.strptime('12/16/2015', '%m/%d/%Y').date()),
            ('BANCO ZAFIRO', 'Cuenta Corriente', 'None', datetime.datetime.strptime('12/16/2015', '%m/%d/%Y').date())
        ),
        '901597012': (
            ('BANCO DIAMANTE', 'Cuenta Corriente', 'None', datetime.datetime.strptime('12/22/2015', '%m/%d/%Y').date())
        )
    }
    return productos


def llenar_datos_taller(self,pathfile):
    if pathfile == 'None':
        personas = get_personas_listado()
        txe = get_transacciones_efectivo()
        anotarias = get_actos_notariales()
        confecamaras = get_confecamaras()
        renta = get_declaracion_renta()
        cambiarias = get_transacciones_cambiarias()
        productos = get_productos()

        """ Personas """
        pkeys = personas.keys()
        for p in pkeys:
            tipoId = personas[p][0]
            idPersona = personas[p][1]
            nombrePersona = personas[p][2]
            PersonasFactory(tIdPersona=tipoId, idPersona=idPersona, nombrePersona= nombrePersona)

        """ Transacciones en efectivo """
        txekeys = txe.keys()
        for t in txekeys:
            lt = txe[t]
            titular = Personas.objects.get(idPersona=t)
            if np.ndim(lt) > 1:
                for l in lt:
                    producto = l[0]
                    if l[1] == 'None':
                        id2 = None
                    else:
                        id2 = Personas.objects.get(idPersona=l[1])

                    fechaTransaccion = l[2]
                    valorTransaccion = l[3]
                    tipoTransaccion = l[4]
                    nombreBanco = l[5]
                    departamento = l[6]
                    municipio = l[7]
                    EfectivoFactory(producto=producto, titular=titular, id2=id2, fechaTransaccion=fechaTransaccion, valorTransaccion=valorTransaccion, tipoTransaccion=tipoTransaccion, nombreBanco=nombreBanco, departamento=departamento, municipio=municipio)

            else:
                l = lt
                producto = l[0]
                if l[1] == 'None':
                    contraparte = None
                else:
                    contraparte = Personas.objects.get(idPersona=l[1])

                fechaTransaccion = l[2]
                valorTransaccion = l[3]
                tipoTransaccion = l[4]
                nombreBanco = l[5]
                departamento = l[6]
                municipio = l[7]
                EfectivoFactory(producto=producto, titular=titular, id2=contraparte, fechaTransaccion=fechaTransaccion, valorTransaccion=valorTransaccion, tipoTransaccion=tipoTransaccion, nombreBanco=nombreBanco, departamento=departamento,municipio=municipio)

        """  Actos notariales """
        nkeys = anotarias.keys()
        for n in nkeys:
            lt = anotarias[n]
            personaActo = Personas.objects.get(idPersona=n)
            if np.ndim(lt) > 1:
                for l in lt:
                    nombreNotaria = l[0]
                    noEscritura = l[1]
                    fechaEscritura = l[2]
                    valorTransaccion = l[3]
                    claseTramite = l[4]
                    calidadActo = l[5]
                    departamento = l[6]
                    municipio = l[7]
                    ActosNotarialesFactory(nombreNotaria=nombreNotaria,noEscritura=noEscritura,fechaEscritura=fechaEscritura,valorTransaccion=valorTransaccion,personaActo=personaActo,claseTramite=claseTramite,calidadActo=calidadActo,departamento=departamento,municipio=municipio)

            else:
                l = lt
                nombreNotaria = l[0]
                noEscritura = l[1]
                fechaEscritura = l[2]
                valorTransaccion = l[3]
                claseTramite = l[4]
                calidadActo = l[5]
                departamento = l[6]
                municipio = l[7]
                ActosNotarialesFactory(nombreNotaria=nombreNotaria, noEscritura=noEscritura, fechaEscritura=fechaEscritura, valorTransaccion=valorTransaccion,personaActo=personaActo, claseTramite=claseTramite, calidadActo=calidadActo, departamento=departamento, municipio=municipio)

        """ Confecamaras """
        cnkeys = confecamaras.keys()
        for c in cnkeys:
            lt = confecamaras[c]
            empresa = Personas.objects.get(idPersona=c)
            if np.ndim(lt) > 1:
                for l in lt:
                    fechaCreacion = l[0]
                    socio = Personas.objects.get(idPersona=l[1])
                    composicion = l[2]
                    ConfeCamarasFactory(fechaCreacion=fechaCreacion, empresa=empresa, socio=socio, composicion=composicion)
            else:
                l = lt
                fechaCreacion = l[0]
                socio = Personas.objects.get(idPersona=l[1])
                composicion = l[2]
                ConfeCamarasFactory(fechaCreacion=fechaCreacion, empresa=empresa, socio=socio, composicion=composicion)

        """ Declaraciones de renta """
        rkeys = renta.keys()
        for r in rkeys:
            lt = renta[r]
            declarante = Personas.objects.get(idPersona=r)
            if np.ndim(lt) > 1:
                for l in lt:
                    anioDeclaracion = l[0]
                    patrimonioBruto = l[1]
                    ingresoBruto = l[2]
                    pasivo = l[3]
                    gastos = l[4]
                    DeclaracionRentaFactory(anioDeclaracion=anioDeclaracion, declarante=declarante, patrimonioBruto=patrimonioBruto, ingresoBruto=ingresoBruto, pasivo=pasivo, gastos=gastos)

            else:
                l = lt
                anioDeclaracion = l[0]
                patrimonioBruto = l[1]
                ingresoBruto = l[2]
                pasivo = l[3]
                gastos = l[4]
                DeclaracionRentaFactory(anioDeclaracion=anioDeclaracion, declarante=declarante,patrimonioBruto=patrimonioBruto, ingresoBruto=ingresoBruto, pasivo=pasivo, gastos=gastos)


        """ Transacciones cambiarias """
        ckeys = cambiarias.keys()
        for c in ckeys:
            lt = cambiarias[c]
            personaTransaccion = Personas.objects.get(idPersona=c)
            if np.ndim(lt) > 1:
                for l in lt:
                    fechaTransaccion = l[0]
                    valorTransaccion = l[1]
                    nombreTransaccion = l[2]
                    tipoTransaccion = l[3]
                    paisTransaccion = l[4]
                    if l[5] == 'None':
                        remitente = None
                    else:
                        remitente = l[5]

                    CambiariasFactory(personaTransaccion=personaTransaccion, fechaTransaccion=fechaTransaccion, valorTransaccion=valorTransaccion, nombreTransaccion=nombreTransaccion, tipoTransaccion=tipoTransaccion, paisTransaccion=paisTransaccion, remitente=remitente)

            else:
                l = lt
                fechaTransaccion = l[0]
                valorTransaccion = l[1]
                nombreTransaccion = l[2]
                tipoTransaccion = l[3]
                paisTransaccion = l[4]
                if l[5] == 'None':
                    remitente = None
                else:
                    remitente = l[5]

                CambiariasFactory(personaTransaccion=personaTransaccion, fechaTransaccion=fechaTransaccion,valorTransaccion=valorTransaccion, nombreTransaccion=nombreTransaccion, tipoTransaccion=tipoTransaccion, paisTransaccion=paisTransaccion, remitente=remitente)

        """ Productos """
        prkeys = productos.keys()
        for p in prkeys:
            lt = productos[p]
            titularProducto = Personas.objects.get(idPersona=p)
            if np.ndim(lt) > 1:
                for l in lt:
                    bancoProducto = l[0]
                    producto = l[1]
                    if l[2] == 'None':
                        titular2Producto = None
                    else:
                        titular2Producto = Personas.objects.get(idPersona=l[2])

                    fechaVinculacion = l[3]
                    ProductosFactory(bancoProducto=bancoProducto,producto=producto, titularProducto=titularProducto, titular2Producto=titular2Producto, fechaVinculacion=fechaVinculacion)

            else:
                l = lt
                bancoProducto = l[0]
                producto = l[1]
                if l[2] == 'None':
                    titular2Producto = None
                else:
                    titular2Producto = Personas.objects.get(idPersona=l[2])

                fechaVinculacion = l[3]
                ProductosFactory(bancoProducto=bancoProducto, producto=producto, titularProducto=titularProducto,titular2Producto=titular2Producto, fechaVinculacion=fechaVinculacion)
