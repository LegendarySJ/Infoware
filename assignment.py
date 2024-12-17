from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import csv
import json

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-blink-features=AutomationControlled')

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

# Amazon credentials
AMAZON_USERNAME = "your_email@example.com"
AMAZON_PASSWORD = "your_password"

# Login to Amazon
def amazon_login():
    driver.get("https://www.amazon.com")

    # Click on Sign In
    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-link-accountList")))
    sign_in_button.click()

    # Enter credentials
    email_field = wait.until(EC.presence_of_element_located((By.ID, "ap_email")))
    email_field.send_keys(AMAZON_USERNAME)
    email_field.send_keys(Keys.RETURN)

    password_field = wait.until(EC.presence_of_element_located((By.ID, "ap_password")))
    password_field.send_keys(AMAZON_PASSWORD)
    password_field.send_keys(Keys.RETURN)

# Scrape product details
def scrape_category(category_url):
    driver.get(category_url)
    scraped_data = []

    try:
        for page in range(1, 16):  # Adjust for 1500 products (100 per page approx.)
            time.sleep(2)  # Avoid overloading the server
            products = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")

            for product in products:
                try:
                    name = product.find_element(By.CSS_SELECTOR, "h2 span").text
                    price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                    discount = product.find_element(By.CSS_SELECTOR, ".s-saving-badge").text
                    rating = product.find_element(By.CSS_SELECTOR, ".a-icon-alt").text
                    best_seller_rating = product.get_attribute("data-best-seller-rank")

                    ship_from = "Not Available"
                    sold_by = "Not Available"
                    try:
                        ship_from = product.find_element(By.CSS_SELECTOR, ".ships-from .a-color-secondary").text
                        sold_by = product.find_element(By.CSS_SELECTOR, ".sold-by .a-color-secondary").text
                    except NoSuchElementException:
                        pass

                    product_description = "Not Available"
                    num_bought = "Not Available"

                    images = []
                    try:
                        img_elements = product.find_elements(By.CSS_SELECTOR, ".s-image")
                        images = [img.get_attribute("src") for img in img_elements]
                    except NoSuchElementException:
                        pass

                    scraped_data.append({
                        "Product Name": name,
                        "Product Price": price,
                        "Sale Discount": discount,
                        "Best Seller Rating": best_seller_rating,
                        "Ship From": ship_from,
                        "Sold By": sold_by,
                        "Rating": rating,
                        "Product Description": product_description,
                        "Number Bought in the Past Month": num_bought,
                        "Images": images,
                        "Category": driver.title.split("|")[0].strip()
                    })
                except NoSuchElementException:
                    continue

            # Click next page
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, "ul.a-pagination li.a-last a")
                next_page.click()
            except NoSuchElementException:
                break
    except Exception as e:
        print(f"Error while scraping category: {e}")

    return scraped_data

# Save data to CSV or JSON
def save_data(data, filename, format="csv"):
    if format == "csv":
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    elif format == "json":
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# Main execution
def main():
    amazon_login()

    categories = [
        "https://www.amazon.com/Best-Sellers/zgbs",
        # Add URLs of other 9 categories here
    ]

    all_data = []
    for category_url in categories:
        print(f"Scraping category: {category_url}")
        category_data = scrape_category(category_url)
        all_data.extend(category_data)

    save_data(all_data, "amazon_best_sellers.csv", format="csv")
    save_data(all_data, "amazon_best_sellers.json", format="json")

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()
