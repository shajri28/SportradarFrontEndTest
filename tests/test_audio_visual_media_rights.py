from playwright.sync_api import Page, expect

from pages.audivisualpage import SportRadarAudiovisualPage

from pages.homepage import SportRadarHomePage


def test_using_home_page_menu_get_audio_visual_media_rights_information(
        page: Page,
        home_page: SportRadarHomePage,
        audio_visual_page: SportRadarAudiovisualPage

) -> None:
    # Given the sportradar home page is displayed home page is displayed
    home_page.load()
    home_page.accept_all_cookies()
    # When user clicks on audio visual media rights link
    home_page.load_audio_media_rights()
    # Then user is redirected to audio visual page
    expect(audio_visual_page.audi_visual_title).to_be_visible()
