from playwright.sync_api import Page, expect

from pages.eventspage import SportRadarEventsPage
from pages.homepage import SportRadarHomePage


def test_homepage_sportradar_in_title_and_check_events_filter_options(
        page: Page,
        events_page: SportRadarEventsPage,
        home_page: SportRadarHomePage) -> None:
    # Given the sportradar home page is displayed home page is displayed
    home_page.load()
    home_page.accept_all_cookies()
    # When the user clicks on  view all events button
    home_page.load_more_events()

    # Then filter content text is displayed in the next page
    expect(events_page.filter_content).to_be_visible()
