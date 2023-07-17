from playwright.sync_api import Page


class SportRadarPlatformPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.platform_page_txt = page.get_by_text("PLATFORMS", exact=True)
