from playwright.sync_api import Page


class SportRadarNorthAmericaPartnersPage:

    def __init__(self, page: Page) -> None:
        self.page = page

        self.ufa_logo = page.get_by_role("img", name="UEFA logo")
        self.nba_logo = page.get_by_role("img", name="NBA logo")
        self.ita_logo = page.get_by_role("img", name="ITF logo")
        self.mlb_logo = page.get_by_role("img", name="MLB logo")
        self.nhl_logo = page.get_by_role("img", name="NHL logo")
        self.fta_logo = page.get_by_role("img", name="FIA logo")
        self.afc_logo = page.get_by_role("img", name="AFC logo")
