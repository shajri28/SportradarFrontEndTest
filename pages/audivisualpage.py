from playwright.sync_api import Page


class SportRadarAudiovisualPage:

    def __init__(self, page: Page) -> None:
        self.page = page

        self.audi_visual_title = page.get_by_text("AUDIOVISUAL", exact=True)
