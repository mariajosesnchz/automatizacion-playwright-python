from pages.home_page import HomePage
from pages.contact_page import ContactPage  
from utils.data_reader import cargar_datos
import pytest
import utils.fake_data as fd

def test_formulario_valido(page):
    #datos = cargar_datos()["invalido"]
    datos = fd.generar_datos_validos()
    home = HomePage(page)
    contact = ContactPage(page)
    home.abrir()
    home.manejar_modal()
    contact.llenar_formulario(datos)
    
    exito = contact.obtener_mensajes_exito()
    assert exito["gracias_por_contactarnos"], "Debe aparecer el mensaje 'Gracias por contactarnos'"
    contact.regresar_inicio()
    assert "xtrim" in page.url.lower(), "No regresó al inicio"
#@pytest.mark.skip    
def test_formulario_invalido(page):
    #datos = cargar_datos()["invalido"]
    datos= fd.generar_datos_invalidos()
    home = HomePage(page)
    contact = ContactPage(page)
    home.abrir()
    home.manejar_modal()
    contact.llenar_formulario(datos)
    page.wait_for_timeout(5000)
    
    errores = contact.obtener_mensajes_error()
    assert errores["email_invalido"], "Debe aparecer el error email invalido"
    assert errores["obligatorios_count"] == 0, "No deben aparecer errores de campos"

def test_formulario_vacio(page):
    #datos = cargar_datos()["vacio"]
    datos= fd.generar_datos_vacios()
    home = HomePage(page)
    contact = ContactPage(page)
    home.abrir()
    home.manejar_modal()
    contact.llenar_formulario(datos)

    errores = contact.obtener_mensajes_error()
    assert errores["obligatorios_count"] == 3, "Deben aparecer 3 errores obligatorios"

def test_cedula_duplicada(page):
    datos = cargar_datos()["duplicadoCI"] 
    home = HomePage(page)
    contact = ContactPage(page)
    home.abrir()
    home.manejar_modal()
    contact.llenar_formulario(datos)

    errores = contact.obtener_mensajes_error()
    assert errores["cedula_duplicada"], "No se mostró el error de cédula duplicada"
    
    
    