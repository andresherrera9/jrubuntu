from django.http import HttpResponse
from django.http import Http404
from django_tables2 import RequestConfig
from django.shortcuts import render
from django.db.models import Q
from .models import Personas, Efectivo, DeclaracionRenta, ConfeCamaras, ActosNotariales, Cambiarias, Productos, RegistroROS, SeguridadSocial
from .forms import searchForm
from .tables import EfectivoTable, ConfeCamarasTable, DeclaracionRentaTable, ActosNotarialesTable, CambiariasTable, ProductosTable, RegistroROSTable, SeguridadSocialTable
from django_tables2.export.export import TableExport
from io import BytesIO
import pandas as pd




def index(request):
    idpage = request.GET['idpage']
    idpage=int(idpage)
    #print(idpage)
    form = searchForm()
    context = {'form': form,'idpage':idpage}
    return render(request,'consultas/index.html',context)


def resultado_persona(request,idpage):
    try:
        
        if idpage == 1:
            
            idPersona = request.GET['searchTerm']
            config = RequestConfig(request)
            p = Personas.objects.get(idPersona = idPersona)
            tefectivo = EfectivoTable(Efectivo.objects.filter(Q(ros=1),Q(titular = p) | Q(id2 = p)))
            tconfecamaras = ConfeCamarasTable(ConfeCamaras.objects.filter(Q(ros=1),Q(empresa=p) | Q(socio=p)))
            tdeclaracion = DeclaracionRentaTable(DeclaracionRenta.objects.filter(Q(ros=1),declarante=p))
            tnotarias = ActosNotarialesTable(ActosNotariales.objects.filter(Q(ros=1),personaActo=p))
            tcambiarias = CambiariasTable(Cambiarias.objects.filter(Q(ros=1),personaTransaccion=p))
            productos = ProductosTable(Productos.objects.filter(Q(ros=1),Q(titularProducto=p) | Q(titular2Producto=p)))
            registroROs = RegistroROSTable(RegistroROS.objects.filter(Q(ros=1),personaPrincipal=p))
            segSocial = SeguridadSocialTable(SeguridadSocial.objects.filter(Q(ros=1),nombreBeneficiario = p))
            context = {'tefectivo': tefectivo,
                    'tdeclaracion': tdeclaracion,
                    'tconfecamaras': tconfecamaras,
                    'tnotarias': tnotarias,
                    'tcambiarias': tcambiarias,
                    'productos': productos,
                    'registroROS': registroROs,
                    'idPersona':idPersona,
                    'idpage':idpage,
                    'segSocial':segSocial
                    }
       
        elif idpage == 2:

            idPersona = request.GET['searchTerm']
            config = RequestConfig(request)
            p = Personas.objects.get(idPersona = idPersona)
            tefectivo = EfectivoTable(Efectivo.objects.filter(Q(ros=1) | Q(ros=2),Q(titular = p) | Q(id2 = p)))
            tconfecamaras = ConfeCamarasTable(ConfeCamaras.objects.filter(Q(ros=1) | Q(ros=2), Q(empresa=p) | Q(socio=p)))
            tdeclaracion = DeclaracionRentaTable(DeclaracionRenta.objects.filter(Q(ros=1) | Q(ros=2),declarante=p))
            tnotarias = ActosNotarialesTable(ActosNotariales.objects.filter(Q(ros=1) | Q(ros=2),personaActo=p))
            tcambiarias = CambiariasTable(Cambiarias.objects.filter(Q(ros=1) | Q(ros=2),personaTransaccion=p))
            productos = ProductosTable(Productos.objects.filter(Q(ros=1) | Q(ros=2),Q(titularProducto=p) | Q(titular2Producto=p)))
            registroROs = RegistroROSTable(RegistroROS.objects.filter(Q(ros=1) | Q(ros=2),personaPrincipal=p))
            segSocial = SeguridadSocialTable(SeguridadSocial.objects.filter(Q(ros=1) | Q(ros=2),nombreBeneficiario = p))
            context = {'tefectivo': tefectivo,
                    'tdeclaracion': tdeclaracion,
                    'tconfecamaras': tconfecamaras,
                    'tnotarias': tnotarias,
                    'tcambiarias': tcambiarias,
                    'productos': productos,
                    'registroROS': registroROs,
                    'idPersona':idPersona,
                    'idpage':idpage,
                    'segSocial':segSocial
                    }


        elif idpage == 3:

            idPersona = request.GET['searchTerm']
            config = RequestConfig(request)
            p = Personas.objects.get(idPersona = idPersona)
            tefectivo = EfectivoTable(Efectivo.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(titular = p) | Q(id2 = p)))
            tconfecamaras = ConfeCamarasTable(ConfeCamaras.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(empresa=p) | Q(socio=p)))
            tdeclaracion = DeclaracionRentaTable(DeclaracionRenta.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),declarante=p))
            tnotarias = ActosNotarialesTable(ActosNotariales.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),personaActo=p))
            tcambiarias = CambiariasTable(Cambiarias.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),personaTransaccion=p))
            productos = ProductosTable(Productos.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(titularProducto=p) | Q(titular2Producto=p)))
            registroROs = RegistroROSTable(RegistroROS.objects.filter(personaPrincipal=p))
            segSocial = SeguridadSocialTable(SeguridadSocial.objects.filter(nombreBeneficiario = p))
            context = {'tefectivo': tefectivo,
                    'tdeclaracion': tdeclaracion,
                    'tconfecamaras': tconfecamaras,
                    'tnotarias': tnotarias,
                    'tcambiarias': tcambiarias,
                    'productos': productos,
                    'registroROS': registroROs,
                    'idPersona':idPersona,
                    'idpage':idpage,
                    'segSocial':segSocial
                    }

        #ltables = list(context.keys())
        #print(ltables)
        #for l in ltables:
        #    config.configure(context[l])
        config.configure(tefectivo)
        config.configure(tconfecamaras)
        config.configure(tdeclaracion)
        config.configure(tdeclaracion)
        config.configure(tdeclaracion)


    except Personas.DoesNotExist:
        raise Http404("La identificación buscada no existe")

    return render(request, 'consultas/resultados_personas.html', context)




def vistas(request):
    idPersona= request.GET["idPersona"]
    idpage= request.GET["idpage"]
    #print(idpage)
    #print(idPersona)
    output = BytesIO()
    p = Personas.objects.get(idPersona = idPersona)

    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    
    if idpage == '1':
       pd.DataFrame(Efectivo.objects.filter(Q(ros=1),Q(titular = p) | Q(id2 = p)).values('producto','titular__nombrePersona','id2__nombrePersona',
                                                                            'fechaTransaccion','valorTransaccion','tipoTransaccion',
                                                                            'nombreBanco','departamento','municipio')).to_excel(writer, sheet_name='Efectivo',index=False)
        
        
       pd.DataFrame(Cambiarias.objects.filter(Q(ros=1),Q(personaTransaccion = p)).values('personaTransaccion__nombrePersona','fechaTransaccion','valorTransaccion',
                                                                                'nombreTransaccion','tipoTransaccion','paisTransaccion','remitente')).to_excel(writer, sheet_name='Cambiarias',index=False)
        
        
       pd.DataFrame(DeclaracionRenta.objects.filter(Q(ros=1),Q(declarante = p)).values('anioDeclaracion','declarante__nombrePersona','patrimonioBruto','patrimonioLiquido',
                                                                        'ingresoBruto','ingresoLiquido','pasivo','gastos')).to_excel(writer, sheet_name='Renta', index=False)
        
       pd.DataFrame(ConfeCamaras.objects.filter(Q(ros=1),Q(empresa = p) | Q(socio = p)).values('estadoMatricula','fechaCreacion','fechaRenovacionMatricula','fechaCancelacionMatricula',
                                                                                'empresa__nombrePersona','socio__nombrePersona','composicion')).to_excel(writer, sheet_name='Confecamaras',index=False)
        
       pd.DataFrame(ActosNotariales.objects.filter(Q(ros=1),Q(personaActo = p)).values('escribanos','noEscritura','fechaEscritura','valorTransaccion','personaActo__nombrePersona',
                                                                            'claseTramite','calidadActo','departamento','municipio')).to_excel(writer, sheet_name='Notarias',index=False)
        
        
       pd.DataFrame(Productos.objects.filter(Q(ros=1),Q(titularProducto = p) | Q(titular2Producto = p)).values('bancoProducto','producto','titularProducto__nombrePersona','titular2Producto__nombrePersona','fechaVinculacion')).to_excel(writer, sheet_name='Productos',index=False)
        
       pd.DataFrame(RegistroROS.objects.filter(Q(ros=1),Q(personaPrincipal = p)).values('codigoROS','fechaReporte','bancoReportante','personaPrincipal__nombrePersona','valorOperacion',
                                                                        'descripcionOperacion')).to_excel(writer, sheet_name='ROS',index=False)

    if idpage == '2':
       pd.DataFrame(Efectivo.objects.filter(Q(ros=1) | Q(ros=2),Q(titular = p) | Q(id2 = p)).values('producto','titular__nombrePersona','id2__nombrePersona',
                                                                            'fechaTransaccion','valorTransaccion','tipoTransaccion',
                                                                            'nombreBanco','departamento','municipio')).to_excel(writer, sheet_name='Efectivo',index=False)
        
        
       pd.DataFrame(Cambiarias.objects.filter(Q(ros=1) | Q(ros=2),Q(personaTransaccion = p)).values('personaTransaccion__nombrePersona','fechaTransaccion','valorTransaccion',
                                                                                'nombreTransaccion','tipoTransaccion','paisTransaccion','remitente')).to_excel(writer, sheet_name='Cambiarias',index=False)
        
        
       pd.DataFrame(DeclaracionRenta.objects.filter(Q(ros=1) | Q(ros=2),Q(declarante = p)).values('anioDeclaracion','declarante__nombrePersona','patrimonioBruto','patrimonioLiquido',
                                                                        'ingresoBruto','ingresoLiquido','pasivo','gastos')).to_excel(writer, sheet_name='Renta', index=False)
        
       pd.DataFrame(ConfeCamaras.objects.filter(Q(ros=1) | Q(ros=2),Q(empresa = p) | Q(socio = p)).values('estadoMatricula','fechaCreacion','fechaRenovacionMatricula','fechaCancelacionMatricula',
                                                                                'empresa__nombrePersona','socio__nombrePersona','composicion')).to_excel(writer, sheet_name='Confecamaras',index=False)
        
       pd.DataFrame(ActosNotariales.objects.filter(Q(ros=1) | Q(ros=2),Q(personaActo = p)).values('escribanos','noEscritura','fechaEscritura','valorTransaccion','personaActo__nombrePersona',
                                                                            'claseTramite','calidadActo','departamento','municipio')).to_excel(writer, sheet_name='Notarias',index=False)
        
        
       pd.DataFrame(Productos.objects.filter(Q(ros=1) | Q(ros=2),Q(titularProducto = p) | Q(titular2Producto = p)).values('bancoProducto','producto','titularProducto__nombrePersona','titular2Producto__nombrePersona','fechaVinculacion')).to_excel(writer, sheet_name='Productos',index=False)
        
       pd.DataFrame(RegistroROS.objects.filter(Q(ros=1) | Q(ros=2),Q(personaPrincipal = p)).values('codigoROS','fechaReporte','bancoReportante','personaPrincipal__nombrePersona','valorOperacion',
                                                                        'descripcionOperacion')).to_excel(writer, sheet_name='ROS',index=False)                                                                   
    
    if idpage == '3':
       pd.DataFrame(Efectivo.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(titular = p) | Q(id2 = p)).values('producto','titular__nombrePersona','id2__nombrePersona',
                                                                            'fechaTransaccion','valorTransaccion','tipoTransaccion',
                                                                            'nombreBanco','departamento','municipio')).to_excel(writer, sheet_name='Efectivo',index=False)
        
        
       pd.DataFrame(Cambiarias.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(personaTransaccion = p)).values('personaTransaccion__nombrePersona','fechaTransaccion','valorTransaccion',
                                                                                'nombreTransaccion','tipoTransaccion','paisTransaccion','remitente')).to_excel(writer, sheet_name='Cambiarias',index=False)
        
        
       pd.DataFrame(DeclaracionRenta.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(declarante = p)).values('anioDeclaracion','declarante__nombrePersona','patrimonioBruto','patrimonioLiquido',
                                                                        'ingresoBruto','ingresoLiquido','pasivo','gastos')).to_excel(writer, sheet_name='Renta', index=False)
        
       pd.DataFrame(ConfeCamaras.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(empresa = p) | Q(socio = p)).values('estadoMatricula','fechaCreacion','fechaRenovacionMatricula','fechaCancelacionMatricula',
                                                                                'empresa__nombrePersona','socio__nombrePersona','composicion')).to_excel(writer, sheet_name='Confecamaras',index=False)
        
       pd.DataFrame(ActosNotariales.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(personaActo = p)).values('escribanos','noEscritura','fechaEscritura','valorTransaccion','personaActo__nombrePersona',
                                                                            'claseTramite','calidadActo','departamento','municipio')).to_excel(writer, sheet_name='Notarias',index=False)
        
        
       pd.DataFrame(Productos.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(titularProducto = p) | Q(titular2Producto = p)).values('bancoProducto','producto','titularProducto__nombrePersona','titular2Producto__nombrePersona','fechaVinculacion')).to_excel(writer, sheet_name='Productos',index=False)
        
       pd.DataFrame(RegistroROS.objects.filter(Q(ros=1) | Q(ros=2) | Q(ros=3),Q(personaPrincipal = p)).values('codigoROS','fechaReporte','bancoReportante','personaPrincipal__nombrePersona','valorOperacion',
                                                                        'descripcionOperacion')).to_excel(writer, sheet_name='ROS',index=False)   

    writer.close()
    output_name='SICON'
    output.seek(0)
    
    response = HttpResponse(output,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment;filename="request.xlsx"'
    return response


