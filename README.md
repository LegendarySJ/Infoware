# Infoware
Amazon Best Sellers Scraper Documentation

This document provides an overview of the Amazon Best Sellers Scraper script, including its functionality, setup instructions, and usage guidelines.

Functionality

The Amazon Best Sellers Scraper is a Python script that extracts data from Amazon's "Best Sellers" section using the Selenium library. The script is designed to log in using user-provided credentials and scrape product details for the top 1500 best-selling items across 10 specified categories. The script focuses on products with discounts greater than 50% and captures key details about each product. The extracted data is stored in both CSV and JSON formats.

Key Features

Authentication: Logs into Amazon using the provided credentials.

Data Collection:

Scrapes product details, including:

Product Name

Product Price

Sale Discount

Best Seller Rating

Ship From

Sold By

Rating

Product Description

Number Bought in the Past Month (if available)

All Available Images

Category Name

Extracts up to 1500 best-selling products per category.

Data Storage:

Saves scraped data in structured CSV and JSON formats.

Error Handling: Handles common exceptions such as missing elements and navigation errors.

Setup Instructions

Prerequisites

Python Installation:

Ensure Python 3.7 or later is installed on your system.

Install Selenium: pip install selenium

WebDriver:

Download the appropriate WebDriver for your browser (e.g., ChromeDriver).

Add the WebDriver executable to your system's PATH or specify its location in the script.

Amazon Account:

A valid Amazon account with credentials is required for authentication.

Setting Up the Script

Download the Script:

Save the provided script as amazon_scraper.py.

Update Credentials:

Replace AMAZON_USERNAME and AMAZON_PASSWORD in the script with your Amazon login credentials.

Specify Categories:

Update the categories list in the script with URLs of the 10 categories you wish to scrape.

Usage Guidelines

Running the Script

Open a terminal or command prompt.

Navigate to the directory containing the amazon_scraper.py file.

Run the script:

python amazon_scraper.py

Output Files

The script generates two output files:

amazon_best_sellers.csv: Contains the scraped data in CSV format.

amazon_best_sellers.json: Contains the scraped data in JSON format.

These files will be saved in the same directory as the script.

Adjusting Scraping Parameters

To modify the maximum number of products scraped, adjust the page limit in the scrape_category function.

To filter products by discount percentage, implement additional logic in the scrape_category function.

Troubleshooting

Common Issues

Login Failure:

Verify that the credentials in the script are correct.

Ensure no CAPTCHA or multi-factor authentication is required for the login.

Element Not Found:

Ensure the WebDriver matches the installed browser version.

Check if Amazon's page structure has changed, and update the script selectors accordingly.

Slow Performance:

Use a faster internet connection or increase the time.sleep() intervals to avoid server throttling.

Error Logs

Errors encountered during execution are printed to the console. Review these messages to debug issues.

Compliance and Ethical Use

Ensure that the use of this scraper complies with Amazon's terms of service. Unauthorized scraping of data may violate Amazon's policies and result in account suspension or legal action. Use this script responsibly and only for permitted purposes.

Support

For further assistance, modify the script or refer to the Selenium documentation: https://www.selenium.dev/documentation/

