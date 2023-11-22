from django.test import TestCase
from .factories import PersonasFactory, EfectivoFactory, DeclaracionRentaFactory, ConfeCamarasFactory, ActosNotarialesFactory, CambiariasFactory
from .models import Personas, Efectivo, DeclaracionRenta, ConfeCamaras, ActosNotariales, Cambiarias
import numpy as np
# Create your tests here

class FactoriesTest(TestCase):
    def setUp(self):
        # for i in range(4):
        #     ConfeCamarasFactory.create(socio=t)

        ConfeCamarasFactory.create_batch(4)
        lp = Personas.objects.all()
        n = len(lp)
        rn = np.random.randint(0,n,2)
        t = lp[rn[0].item()]
        c = lp[rn[1].item()]
        EfectivoFactory.create_batch(5,titular=t, contraparte=c)
        for p in lp:
            DeclaracionRentaFactory.create(declarante=p)
            ActosNotarialesFactory(personaActo=p)
            CambiariasFactory(personaTransaccion=p)
