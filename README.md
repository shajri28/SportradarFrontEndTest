## What is Playwright?

Playwright is a fairly new test automation framework from Microsoft.
It is open source, and it has bindings in TypeScript/JavaScript, Python, .NET, and Java.
Some of the nice features Playwright offers include:

* concise, readable calls
* easy out-of-the-box setup
* very fast execution times (compared to other browser automation tools)
* cross-browser and mobile emulation support
* automatic waiting
* screenshots and video capture
* built-in API calls

https://playwright.dev/

Microsoft is actively developing Playwright,
so new features are coming all the time!

## Test Maintenance

In this project Page oriented Model is used.
Selectors are created in pages package
Add your new pages classes to conftest.py file

Example:
@pytest.fixture
def north_america_partners_page(page: Page) -> SportRadarNorthAmericaPartnersPage:
return SportRadarNorthAmericaPartnersPage(page)

## Installation

To ensure all dependencies are resolved in a CI environment, in one go, add them to a requirements.txt file.

Then run the following command : pip install -r requirements.txt