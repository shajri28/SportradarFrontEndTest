from playwright.sync_api import Page, expect


class SportRadarEventsPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.filter_content = page.get_by_role("heading", name="Filter content")
        self.category = page.get_by_role("combobox", name="Category")
        self.betting_category = page.get_by_role("option", name="✔Betting & Gaming")
        self.content_type = page.get_by_role("combobox", name="Content type").locator("span")
        self.case_content_type = page.locator("#customSelect-nJhJy-panel").get_by_role("option", name="Case Study")
        self.results_div = page.locator("div")

    def click_category_combobox(self) -> None:
        self.category.click()

    def choose_betting_category(self) -> None:
        self.betting_category.click()

    def click_content_type_combobox(self) -> None:
        self.content_type.click()

    def choose_case_study_content(self) -> None:
        self.case_content_type.click()

    def check_filter_results(self, phrase: str) -> None:
        self.results_div.filter(has_text=phrase)
