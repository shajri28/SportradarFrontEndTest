from playwright.sync_api import Page


class SportRadarRegionsPage:

    def __init__(self, page: Page) -> None:
        self.page = page

        self.north_america = page.get_by_role("link", name="North America")

        self.partners_button = page.get_by_role("link", name="Our Partners & Clients")

    def click_north_america_button(self) -> None:
        self.north_america.click()

    def click_partners_button(self) -> None:
        self.partners_button.click()
