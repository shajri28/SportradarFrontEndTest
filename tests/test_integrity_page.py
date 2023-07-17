from playwright.sync_api import Page, expect

from pages.homepage import SportRadarHomePage
from pages.integrity_page import SportRadarIntegrityPage


def test_user_clicks_on_integrity_from_menu_and_redirected_to_integrity_page(
        page: Page,
        home_page: SportRadarHomePage, integrity_page: SportRadarIntegrityPage
) -> None:
    # Given the sportradar home page is displayed home page is displayed
    home_page.load()
    home_page.accept_all_cookies()
    # When user clicks on integrity link
    home_page.click_integrity_link()
    # Then integrity text is displayed
    expect(integrity_page.integrity_text).to_be_visible()
