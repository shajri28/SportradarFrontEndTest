from playwright.sync_api import Page


class SportRadarHomePage:
    URL = 'https://sportradar.com/'
    Sport_Entertainment_URL = "https://sportradar.com/sports-entertainment/audiovisual/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.events_link = page.get_by_role("link", name="View all News & Events")
        self.accept = page.get_by_role("button", name="ACCEPT ALL")
        self.what_we_do = page.get_by_role("heading", name="WHAT WE DO")
        self.betting_and_gaming_frame = page.get_by_role("heading", name="BETTING & GAMING")
        self.platforms_link = page.get_by_role("link", name="PLATFORMS")
        self.sport_entertainment_link = page.get_by_role("link", name="Sports Entertainment", exact=True)
        self.audi_visual_page = page.get_by_text("AUDIOVISUAL", exact=True)
        self.region_button = page.get_by_role("link", name="Regions")
        self.integrity_link = page.get_by_role("link", name="Integrity", exact=True)

    def load(self) -> None:
        self.page.goto(self.URL)

    def load_more_events(self) -> None:
        self.events_link.click()

    def accept_all_cookies(self) -> None:
        self.accept.click()

    def check_betting_platforms(self) -> None:
        self.platforms_link.click()

    def load_audio_media_rights(self) -> None:
        self.page.goto(self.Sport_Entertainment_URL)
        self.sport_entertainment_link.click()

    def click_regions_button(self) -> None:
        self.region_button.click()

    def click_integrity_link(self) -> None:
        self.integrity_link.click()
