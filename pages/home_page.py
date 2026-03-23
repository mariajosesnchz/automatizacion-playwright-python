from playwright.sync_api import Page
from utils.config import BASE_URL

class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def abrir(self):
        self.page.goto(BASE_URL)

    def manejar_modal(self):
        # Esperar un poco a que cargue todo
        self.page.wait_for_timeout(4000)

        modal = self.page.locator("#promoPopup")

        if modal.is_visible():
            print("Modal apareció")
            
            boton=self.page.get_by_role("link", name="Contrata hoy").first

            # Esperar explícitamente que el botón esté visible
            boton.wait_for(state="visible", timeout=10000)
            boton.scroll_into_view_if_needed()
            boton.click(force=True)
        else:
            print("Modal NO apareció")
        
    def cerrar_modal(self):
        modal = self.page.locator("#promoPopup")

        if modal.is_visible():
            print("Intentando cerrar modal")

        boton_cerrar = self.page.locator("#promoClose")

        try:
            boton_cerrar.wait_for(state="visible", timeout=5000)
            boton_cerrar.click(force=True)

            # 🔥 Validar que desapareció
            modal.wait_for(state="hidden", timeout=5000)

            print("Modal cerrado correctamente")
        except:
            print("No se pudo cerrar el modal")
        else:
            print("Modal no está visible")