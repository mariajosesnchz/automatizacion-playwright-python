from playwright.sync_api import Page


class ContactPage:

    def __init__(self, page: Page):
        self.page = page

        
    def llenar_formulario(self, datos):
        self.page.wait_for_timeout(3000)

        self.page.get_by_role("textbox", name="Nombres").fill(datos["nombre"])
        self.page.get_by_role("textbox", name="Cédula").fill(datos["cedula"])
        self.page.get_by_role("textbox", name="Teléfono").fill(datos["telefono"])
        self.page.get_by_role("textbox", name="Correo electrónico").fill(datos["email"])

        checkbox = self.page.get_by_role("checkbox", name="Al dar clic, autorizas el uso")

        try:
            if not checkbox.is_checked():
                checkbox.click(force=True)
        except:
        # fallback si no es un checkbox real
            checkbox.click(force=True)

        self.page.get_by_role("button", name="Enviar").click()    
            
    def obtener_mensajes_error(self) -> dict:
        errores = {}

    # Error general
        general = self.page.get_by_text("Ocurrió un error al procesar tu solicitud")
        try:
            general.wait_for(state="visible", timeout=5000)
            errores["general"] = True
        except:
            errores["general"] = False

    # Obligatorios (no necesitan wait_for)
        obligatorios = self.page.locator("text=Este campo es obligatorio.")
        errores["obligatorios_count"] = obligatorios.count()

    # Cédula duplicada
        error_cedula = self.page.get_by_text("No se puede crear otro lead con esta identificación")
        errores["cedula_duplicada"] = error_cedula.is_visible() if error_cedula.count() > 0 else False

    # Email inválido
        error_email = self.page.get_by_text("Por favor, introduce una dirección de correo electrónico válida")
        errores["email_invalido"] = error_email.is_visible() if error_email.count() > 0 else False

        return errores
    
    def obtener_mensajes_exito(self) -> dict:
        exitos = {}

        mensaje_exito = self.page.get_by_role("heading", name="¡Gracias por contactarnos!")

        mensaje_exito.wait_for(state="visible", timeout=10000)

        exitos["gracias_por_contactarnos"] = mensaje_exito.is_visible()

        return exitos
    
    def regresar_inicio(self):
        boton = self.page.get_by_role("link", name="Regresar al inicio")
        boton.click()