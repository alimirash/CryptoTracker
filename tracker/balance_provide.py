from pathlib import Path
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = "https://www.coincarp.com/currencies/ethereum/richlist/"

base_dir = Path("tracker/data")

csv_files = list(base_dir.glob("*.csv"))

if not csv_files:
    print("No CSV files found in the directory.")
else:
    print(f"Found {len(csv_files)} files: {csv_files}")

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.odd, tr.even"))
    )
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    rows = soup.find_all("tr", class_=["odd", "even"])
    personal_wallets = []
    exchange_wallets = []

    for order_number, row in enumerate(rows):
        try:
            wallet_element = row.find("td", class_="td2")
            wallet = (
                wallet_element.find("span", class_="mr-2").text.strip()
                if wallet_element
                else "Unknown"
            )
            quantity_element = row.find("td", class_="td3")
            quantity = quantity_element.text.strip() if quantity_element else "0"
            owner_element = row.find("span", class_="adds-notes")
            owner = owner_element.text.strip() if owner_element else "personal"
            changes_element = row.find("td", class_="td5")
            changes = changes_element.text.strip() if changes_element else "0"
            for file_path in csv_files:
                print(f"Processing file: {file_path}")
                try:
                    df = pd.read_csv(file_path)
                    print(df.head())

                    df.columns = [col.strip() for col in df.columns]

                    if wallet in df["Address"].values:
                        name_tag = df.loc[df["Address"] == wallet, "Name Tag"].values[0]
                        if pd.notna(name_tag):
                            owner = name_tag
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

            if owner == "personal":
                personal_wallets.append(
                    {
                        "order_number": order_number,
                        "wallet": wallet,
                        "quantity": quantity,
                        "owner": owner,
                        "changes": changes,
                    }
                )
            else:
                exchange_wallets.append(
                    {
                        "order_number": order_number,
                        "wallet": wallet,
                        "quantity": quantity,
                        "owner": owner,
                        "changes": changes,
                    }
                )
        except AttributeError as e:
            print(f"Error processing row: {e}")

    print("Personal Wallets:")
    for entry in personal_wallets:
        print(entry)

    print("Exchange Wallets:")
    for entry in exchange_wallets:
        print(entry)

finally:
    driver.quit()
