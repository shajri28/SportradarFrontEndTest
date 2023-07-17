from playwright.sync_api import Page, expect

from pages.homepage import SportRadarHomePage
from pages.north_america_partners_page import SportRadarNorthAmericaPartnersPage

from pages.regions_page import SportRadarRegionsPage


def test_north_america_region_partners(
        page: Page,
        home_page: SportRadarHomePage, regions_page: SportRadarRegionsPage,
        north_america_partners_page: SportRadarNorthAmericaPartnersPage

) -> None:
    # Given the sportradar home page is displayed home page is displayed
    home_page.load()
    home_page.accept_all_cookies()
    # When user clicks on Region Button
    home_page.click_regions_button()
    # And user selects north america
    regions_page.click_north_america_button()

    # And user clicks on our partners button
    regions_page.click_partners_button()

    # Then north america partners logos are visible
    expect(north_america_partners_page.nba_logo).to_be_visible()
    expect(north_america_partners_page.afc_logo).to_be_visible()
    expect(north_america_partners_page.mlb_logo).to_be_visible()
    expect(north_america_partners_page.fta_logo).to_be_visible()
    expect(north_america_partners_page.ita_logo).to_be_visible()
    expect(north_america_partners_page.ufa_logo).to_be_visible()
