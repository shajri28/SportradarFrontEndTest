from playwright.sync_api import Page, expect

from pages.eventspage import SportRadarEventsPage
from pages.homepage import SportRadarHomePage
from pages.platformspage import SportRadarPlatformPage


def test_betting_and_gaming_information(
        page: Page,
        events_page: SportRadarEventsPage,
        home_page: SportRadarHomePage,
        platform_page: SportRadarPlatformPage
) -> None:
    # Given the sportradar home page is displayed home page is displayed
    home_page.load()
    home_page.accept_all_cookies()
    # Then user sees What we do text on this page
    expect(home_page.what_we_do).to_be_visible()
    # And user sees Betting and Gaming Information
    expect(home_page.betting_and_gaming_frame).to_be_visible()
    # When user clicks on platforms link
    home_page.check_betting_platforms()
    # Then user is redirected to platforms page
    expect(platform_page.platform_page_txt).to_be_visible()
