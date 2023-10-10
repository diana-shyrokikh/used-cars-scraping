from selenium.webdriver.chrome.service import Service

import init_django_orm  # noqa: F401

from urllib.parse import urljoin

from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from tqdm import tqdm

from cars_db.models import Car
from utils import (
    get_username,
    get_images_count,
    get_car_number,
    get_car_vin,
    get_phone_number,
    is_cookies_notification,
    get_last_page,
    get_image,
)

BASE_URL = "https://auto.ria.com/uk/car/used/"


def get_webdriver() -> WebDriver:
    service = Service(executable_path="/usr/local/bin/chromedriver-linux64/chromedriver")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(service=service, options=chrome_options)


def get_page(
        path: str,
        driver: WebDriver
) -> None:
    page = urljoin(BASE_URL, path)
    driver.get(page)


def get_car_list(driver: WebDriver, page: int) -> list[str]:
    cars = driver.find_elements(
            By.CLASS_NAME,
        "m-link-ticket"
        )
    car_links = [
        car.get_attribute("href")
        for car in tqdm(
            cars,
            desc=f"Creating car list from {page} page"
        )
    ]

    return car_links


def get_car(driver: WebDriver, url: str) -> None:
    driver.get(url)
    username = get_username(driver)

    if not username:
        return None

    title = driver.find_element(
        By.TAG_NAME, "h1"
    ).get_attribute("title")

    price_usd = int(driver.find_element(
        By.CSS_SELECTOR,
        "div.price_value > strong"
    ).text.replace("$", "").replace(
        " ", ""
    ).replace("€", ""))

    one_thousand = 1_000
    odometer = int(driver.find_element(
        By.CSS_SELECTOR,
        "div.base-information.bold > span"
    ).text) * one_thousand

    image_url = get_image(driver)
    images_count = get_images_count(driver)
    car_number = get_car_number(driver)
    car_vin = get_car_vin(driver)
    phone_number = get_phone_number(driver)

    return Car.objects.create(
        url=url,
        title=title,
        price_usd=price_usd,
        odometer=odometer,
        username=username,
        phone_number=phone_number,
        image_url=image_url,
        images_count=images_count,
        car_number=car_number,
        car_vin=car_vin,
    )


def get_all_cars(pages: int = None) -> None:
    driver = get_webdriver()

    driver.get(BASE_URL)

    is_cookies_notification(driver)

    last_page = (
        get_last_page(driver)
        if not pages
        else pages
    )

    for page in range(1, last_page + 1):
        driver.get(BASE_URL)
        get_page(
            driver=driver,
            path=f"?page={page}"
        )

        cars = get_car_list(driver, page)
        for car in tqdm(
            cars,
            desc=f"Scraping cars"
        ):
            get_car(driver, car)

    driver.close()


if __name__ == "__main__":
    get_all_cars()
