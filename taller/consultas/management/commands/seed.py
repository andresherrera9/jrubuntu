from django.core.management.base import BaseCommand
from consultas.factories import PersonasFactory, EfectivoFactory, DeclaracionRentaFactory, ConfeCamarasFactory, ActosNotarialesFactory, CambiariasFactory, ProductosFactory
from consultas.models import Personas, Efectivo, DeclaracionRenta, ConfeCamaras, ActosNotariales, Cambiarias, Productos, RegistroROS
import numpy as np
import datetime as dt

class Command(BaseCommand):
    help = 'Poblar la base de datos con información ficticia'

    def add_arguments(self, parser):
        parser.add_argument('--mode', default='refresh', type=str, help='Mode')
        parser.add_argument('--users', default=20, type=int,
                            help='Número de personas naturales o jurídicas ficticias: Se debe utilizar números pares. Si se ingresa un número impar el código hará una aproximación')
        parser.add_argument('--include_tipologias', default=False, type=bool,
                            help='Si es True se ingresan datos referente a tipologias conocidas')

    def handle(self, *args, **options):
        self.stdout.write('Alimentando la base de datos.....')
        alimentar_base_datos(self,options['mode'],options['users'],options['include_tipologias'])
        self.stdout.write('Proceso terminado.')


def limpiar_datos():
    Personas.objects.all().delete()


def declaracionRenta(anhoInicial,anhoFinal,declarante,incremento = 0):
    if incremento > 0:
        d = DeclaracionRentaFactory(anioDeclaracion=anhoInicial, declarante=declarante)
        ind = 1 + (incremento/100)
        patrimoniob = d.patrimonioBruto
        ingresob = d.ingresoBruto
        for a in range(anhoInicial+1,anhoFinal):
            DeclaracionRentaFactory(anioDeclaracion=a, declarante=declarante,patrimonioBruto=int(patrimoniob*ind),ingresoBruto=int(ingresob*ind))
    else:
        for a in range(anhoInicial,anhoFinal):
            DeclaracionRentaFactory(anioDeclaracion=a, declarante=declarante)


def tipologia_empresas_fachada():
    name = 'Carlos Peréz'
    idPersona = np.random.randint(50000000, 100000000, 1).item()
    p = PersonasFactory.create(tIdPersona='CC',idPersona=idPersona,nombrePersona=name)
    fechaInicio = 2009
    fechaFinal = 2019
    deltaAnhos = 2
    for a in range(fechaInicio,fechaFinal,deltaAnhos):
        fi = dt.date(a,1,1)
        ff = dt.date(a+deltaAnhos,1,1)
        c = ConfeCamarasFactory.create(estadoMatricula='INACTIVA', fechaCreacion=fi, fechaRenovacionMatricula=ff, fechaCancelacionMatricula=ff, socio=p)
        declaracionRenta(a,a+deltaAnhos,c.empresa,200)

def crear_datos(users):
        ConfeCamarasFactory.create_batch(users)
        lp = Personas.objects.all()
        n = len(lp)
        rn = np.random.randint(0, n, 2)
        t = lp[rn[0].item()]
        c = lp[rn[1].item()]
        EfectivoFactory.create_batch(5, titular=t, id2=c)
        for p in lp:
            d = DeclaracionRentaFactory.create(declarante=p)
            anhoInicial = d.anioDeclaracion
            declaracionRenta(anhoInicial+1,anhoInicial+2,p)
            ActosNotarialesFactory(personaActo=p)
            CambiariasFactory(personaTransaccion=p)
            ProductosFactory(titularProducto=p, titular2Producto=p)


def alimentar_base_datos(self,mode,users,include_tipologias):
    if users < 2:
        users = 1
    else:
        users = int(users/2)

    limpiar_datos()
    if mode == 'clear':
        return

    crear_datos(users=users)
    if include_tipologias:
        tipologia_empresas_fachada()