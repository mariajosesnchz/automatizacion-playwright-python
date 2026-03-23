from pages.home_page import HomePage
from utils.data_reader import cargar_datos
import pytest
import utils.fake_data as fd


def test_modal_contratar(page):
    home = HomePage(page)
    home.abrir()
    home.manejar_modal()
    assert "xtrim" in page.url.lower()

def test_cerrar_modal(page):
    home = HomePage(page)
    home.abrir()
    # Esperar que el modal aparezca
    page.wait_for_timeout(3000)
    modal = page.locator("#promoPopup")
    if modal.is_visible():
        home.cerrar_modal()
        # Validar que desapareció
        assert not modal.is_visible(), "El modal no se cerró"
    else:
        print("Modal no apareció, test no aplica")    
