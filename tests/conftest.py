# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import asyncio
from playwright.async_api import async_playwright

import pytest

from playwright.sync_api import Playwright, APIRequestContext, Page, expect, sync_playwright

from pages.audivisualpage import SportRadarAudiovisualPage
from pages.eventspage import SportRadarEventsPage
from pages.homepage import SportRadarHomePage
from pages.integrity_page import SportRadarIntegrityPage
from pages.north_america_partners_page import SportRadarNorthAmericaPartnersPage
from pages.platformspage import SportRadarPlatformPage
from pages.regions_page import SportRadarRegionsPage


# ------------------------------------------------------------
# DuckDuckGo search fixtures
# ------------------------------------------------------------

@pytest.fixture
def home_page(page: Page) -> SportRadarHomePage:
    return SportRadarHomePage(page)


@pytest.fixture
def platform_page(page: Page) -> SportRadarPlatformPage:
    return SportRadarPlatformPage(page)


@pytest.fixture
def events_page(page: Page) -> SportRadarEventsPage:
    return SportRadarEventsPage(page)


@pytest.fixture
def audio_visual_page(page: Page) -> SportRadarAudiovisualPage:
    return SportRadarAudiovisualPage(page)


@pytest.fixture
def regions_page(page: Page) -> SportRadarRegionsPage:
    return SportRadarRegionsPage(page)


@pytest.fixture
def north_america_partners_page(page: Page) -> SportRadarNorthAmericaPartnersPage:
    return SportRadarNorthAmericaPartnersPage(page)


@pytest.fixture
def integrity_page(page: Page) -> SportRadarIntegrityPage:
    return SportRadarIntegrityPage(page)


@pytest.fixture(autouse=True)
async def run_before_and_after_tests(playwright: Playwright):
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want

    browser = playwright.chromium.launch(headless=False)

    yield  # this is where the testing happens

    browser.close()
