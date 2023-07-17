from playwright.sync_api import Page


class SportRadarIntegrityPage:

    def __init__(self, page: Page) -> None:
        self.page = page

        self.integrity_text = page.get_by_text("INTEGRITY", exact=True)
