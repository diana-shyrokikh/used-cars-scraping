import datetime

from django.core import serializers
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from cars_db.models import Car


def get_username(driver: WebDriver) -> str | None:
    username = driver.find_elements(
        By.CSS_SELECTOR,
        "h4.seller_info_name > a"
    )

    if username:
        return username[0].text

    else:
        username = driver.find_elements(
            By.CSS_SELECTOR,
            "div.seller_info_name.bold"
        )

        if username:
            return username[0].text

    return None


def get_image(driver: WebDriver) -> str | None:
    image_url = driver.find_elements(
        By.CSS_SELECTOR,
        "div.carousel-inner._flex > div.photo-620x465.loaded > picture > img"
    )

    if image_url:
        return image_url[0].get_attribute("src")

    for i in range(2, 10):
        picture_url = driver.find_elements(
            By.CSS_SELECTOR,
            f"div.carousel-inner._flex > div:nth-child({i}) > picture > img"
        )

        if picture_url:
            return picture_url[0].get_attribute("src")

    return None


def get_images_count(driver: WebDriver) -> int:
    images_count = driver.find_elements(
        By.CSS_SELECTOR,
        "a.show-all.link-dotted"
    )

    if images_count:
        return int(images_count[0].text.split()[-2])

    return len(driver.find_elements(
        By.CSS_SELECTOR,
        "div.preview-gallery.mhide > div > a"
    ))


def get_car_number(driver: WebDriver) -> str | None:
    car_number = driver.find_elements(
        By.CSS_SELECTOR,
        "span.state-num.ua"
    )

    if car_number:
        return car_number[0].text

    return None


def get_car_vin(driver: WebDriver) -> str | None:
    car_vin = driver.find_elements(
        By.CLASS_NAME, "label-vin"
    )

    if car_vin:
        return car_vin[0].text

    else:
        car_vin = driver.find_elements(
            By.CLASS_NAME, "vin-code"
        )

        if car_vin:
            return car_vin[0].text

    return None


def get_phone_number(driver: WebDriver) -> int:
    driver.find_element(
        By.CSS_SELECTOR,
        "#phonesBlock > div > span > a"
    ).click()

    phone_number = driver.find_element(
        By.CSS_SELECTOR,
        "div.popup-successful-call-desk.size24.bold.green.mhide.green"
    ).get_attribute(
        "data-value"
    ).replace("(", "").replace(")", "").replace(" ", "")

    return int(f"38{phone_number}")


def is_cookies_notification(driver: WebDriver) -> None:
    accept_cookies = driver.find_elements(
        By.CSS_SELECTOR,
        "label.js-close.c-notifier-btn"
    )

    if accept_cookies:
        accept_cookies[0].click()


def get_last_page(driver: WebDriver) -> int:
    last_page = driver.find_element(
        By.CSS_SELECTOR,
        "#pagination > nav > span:nth-child(8) > a"
    )

    return int(last_page.text.replace(" ", ""))


def write_used_cars_data_json() -> None:
    data = Car.objects.all()
    json_data = serializers.serialize(
        "json", data, indent=2
    )
    date = datetime.datetime.now().date()
    file_path = f"dumps/used_car_data_{date}.json"

    with open(
            file_path, "w", encoding="utf-8"
    ) as json_file:
        json_file.write(json_data)
