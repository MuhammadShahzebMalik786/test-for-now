print("importing libraries")

import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup

import time
import tkinter as tk

import csv

print("libraries imported")


print("seting options")
# WebDriver setup using undetected-chromedriver
options = Options()
# options.add_argument("--headless")  # Optional: Run in headless mode
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (optional)
options.add_argument("--no-sandbox")  # Avoid sandboxing issues

print("creating server")
# Create a Service object
service = Service(r'E:\OneDrive\Desktop\Car data scraper\chromedriver.exe')  # Correct path to your ChromeDriver
print("seting options")
# Use undetected_chromedriver
driver = uc.Chrome(service=service, options=options)





# ////////////////////////////////////////////////////////////////////////////
# use this function only for debuging
def get_input(a="anything"):
    def on_submit():
        user_input = input_entry.get()
        print(f"User input: {user_input}")  # Display in terminal
        root.quit()  # Close the window after getting the input
        root.destroy()

    root = tk.Tk()
    root.title("Enter Something")

    tk.Label(root, text=a).pack(pady=5)
    input_entry = tk.Entry(root)
    input_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()


# /////////////////////////////////////////////////////////////////////////////////////////////////////
# this function will accept concent 


def accept_consent_cookie(driver, timeout=15) -> bool:
    """
    Accepts the Mobile.de consent modal if present.
    
    Parameters:
        driver: The undetected Chrome WebDriver (already on the page).
        timeout: Maximum seconds to wait for the button to appear (default 15).
    
    Returns:
        True if the consent button was found and clicked; False otherwise.
    """
    wait = WebDriverWait(driver, timeout)
    # First, try in the root document
    try:
        btn = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mde-consent-accept-btn"))
        )
        btn.click()

        return True
    except Exception:
        # If not found, iterate through iframes
        i=0
        for frame in driver.find_elements(By.CSS_SELECTOR, "iframe"):
            i+=1
            print(i)
            driver.switch_to.frame(frame)
            try:
                # btn = WebDriverWait(driver, 5).until(
                #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mde-consent-accept-btn"))
                # )
                # btn.click()
                driver.switch_to.default_content()
                return True
            except Exception:
                driver.switch_to.default_content()
                pass
    return False

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def accept_concent():
    print("checking for accept concent")
    if accept_consent_cookie(driver):
        print("Cookie consent accepted.")
    else:
        print("Consent button not found; it may already be accepted or the selector changed.")













# ///////////////////////////////////////////////////////////////////////////////
# code to check if menue selection is needed, or want to directly go to link
json=True # put function to check what is present in api
if json:
    pass



# /////////////////////////////////////////////////////////////////////////////////////

# Open the website for menue selection
print("geting driver")
driver.get("https://www.mobile.de/?lang=en")
time.sleep(5)  # Wait for elements to load
print("geting after wait")


driver.get("https://www.mobile.de/?lang=en")
driver.implicitly_wait(10)



accept_concent()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# code for selecting options in menue



# Select Make from the "Top makes" dropdown
make_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'qs-select-make'))
)

# make_dropdown.click()

# Select the Mercedes-Benz option
mercedes_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//option[@value='17200']"))
)
mercedes_option.click()

# get_input("line 59")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to get all makes for the selected make
def get_makes():
    # Wait for the make dropdown to be updated (or visible)
    make_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'qs-select-make'))
    )

    # Extract all make options
    make_options = make_dropdown.find_elements(By.TAG_NAME, 'option')
    
    makes = []
    for option in make_options:
        make_name = option.text
        make_value = option.get_attribute('value')
        if make_name != "Any" and make_value:  # Skip "Any" and empty values
            makes.append((make_name, make_value))

    return makes



# Example usage: Select Audi and then get all makes
# select_make('1900')  # Audi's value from the dropdown
makes = get_makes()

# Print the makes
for make in makes:
    print(f"Make: {make[0]}, Value: {make[1]}")
# print(f"Make: {makes}, Value: {makes}")



# /////////////////////////////////////////////////////////////////////////////////////////////////////




# /////////////////////////////////////////////////////////////////////////////////////////////////////
# Select Model from the "Top models" dropdown
model_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'qs-select-model'))
)
# model_dropdown.click()

# Select the Model option
mercedes_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//option[@value='126']"))
)
mercedes_option.click()
# Select the model (e.g., Audi)



# get_input("line 76")










# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to get all models for the selected model
def get_models():
    # Wait for the model dropdown to be updated (or visible)
    model_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'qs-select-model'))
    )

    # Extract all model options
    model_options = model_dropdown.find_elements(By.TAG_NAME, 'option')
    
    models = []
    for option in model_options:
        model_name = option.text
        model_value = option.get_attribute('value')
        if model_name != "Any" and model_value:  # Skip "Any" and empty values
            models.append((model_name, model_value))

    return models



# Example usage: Select Audi and then get all models
# select_model('1900')  # Audi's value from the dropdown
models = get_models()

# Print the models
for model in models:
    print(f"Model: {model[0]}, Value: {model[1]}")
# print(f"Model: {models}, Value: {models}")




# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Select qs-select-1st-registration-from-select from the "Top models" dropdown
model_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'qs-select-1st-registration-from'))
)
model_dropdown.click()

# Select the qs-select-1st-registration-from-select option
# mercedes_option = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//option[@value='2023']"))
# )
# mercedes_option.click()


# get_input("line 93")


# ////////////////////////////////////////////////////////////////////////////////////////







# Select milage from the "Top models" dropdown
model_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'qs-select-mileage-up-to'))
)
model_dropdown.click()

# Select the milage option
mercedes_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//option[@value='50000']"))
)
mercedes_option.click()


# get_input("click milage to any")



# /////////////////////////////////////////////////////////////////////////////////////////////





# Wait for the "Leasing" button to be clickable
leasing_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@value='purchase']"))
)

# Click on the "Leasing" button
leasing_button.click()


# get_input("line 122")

# /////////////////////////////////////////////////////////////////////////////////
# # Wait for the dropdown to be clickable
# price_dropdown = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'NeA3T'))
# )

# # Click the dropdown to reveal the options
# price_dropdown.click()

# # Wait for the "1000" option to be visible
# option_1000 = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//option[@value='1000']"))
# )

# # Use ActionChains to click on the "1000" option
# action = ActionChains(driver)
# action.move_to_element(option_1000).click().perform()

# # Optional: Wait for a few seconds to ensure the selection is reflected
# time.sleep(2)





# get_input("line 147")



# ///////////////////////////////////////////////////////////////////////////////////
print("clicking on geolocation")
# Select geolocation-autosuggest from the "Top makes" dropdown
make_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'geolocation-autosuggest'))
)
make_dropdown.click()
print("clicked on geolocation")
#//////////////////////////////////////////////////////////////////////////////////////////////////






# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# submit 
print("clicking submit button")
submit_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="qs-submit-button"]'))
)
print("submit button got")
print("sleeping")
time.sleep(5)
print("sleep done")
# wait for button
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="qs-submit-button"]'))
)

# get text
text = button.text
print(text)  # → "1,105 Offers"

# extract number only
total_searches = int(text.split()[0].replace(",", ""))
print("Total searches:", total_searches)



submit_button.click()
print("submit button pressed")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def click_continue_if_enabled(driver, timeout=10, logger=print):
    """
    Clicks the pagination Continue/Weiter button if enabled.
    If disabled, logs 'Continue is disabled' and returns False.
    Returns True if clicked, False otherwise.
    """

    # Works for both English + German labels:
    # data-testid is stable; aria-label can be Continue / Weiter
    locator = (By.CSS_SELECTOR, 'button[data-testid="pagination:next"]')

    try:
        btn = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        logger("Continue button not found.")
        return False

    try:
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)

        # Robust enabled check
        disabled_attr = btn.get_attribute("disabled")
        aria_disabled = (btn.get_attribute("aria-disabled") or "").lower()
        enabled = btn.is_enabled() and (disabled_attr is None) and (aria_disabled != "true")

        if not enabled:
            logger("Continue is disabled.")
            return False

        try:
            btn.click()
        except Exception:
            driver.execute_script("arguments[0].click();", btn)

        logger("Continue clicked.")
        return True

    except (StaleElementReferenceException, Exception) as e:
        logger(f"Could not click Continue: {e}")
        return False
    

# print(click_continue_if_enabled(driver))
# print('check continue')
# ///////////////////////////////////////////////////////////////////////////////////////////////


def get_total_pages(driver, timeout=10, logger=print):
    """
    Returns total number of pages from the pagination UI.

    Handles patterns like:
      - <span class="XUy1p">1/50</span>  -> returns 50
      - <button aria-label="Seite 50">  -> returns 50
      - <button aria-label="Page 6">    -> returns 6

    Returns:
      int (total pages) or None if not found.
    """

    wait = WebDriverWait(driver, timeout)

    # 1) Best: read "current/total" like 1/50 from span.XUy1p
    try:
        ratio_el = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="srp-pagination"] span.XUy1p'))
        )
        txt = (ratio_el.text or "").strip()  # e.g., "1/50" or "6/6"
        m = re.search(r'(\d+)\s*/\s*(\d+)', txt)
        if m:
            total = int(m.group(2))
            logger(f"Total pages: {total} (from '{txt}')")
            return total
    except TimeoutException:
        pass
    except Exception as e:
        logger(f"Could not read XUy1p ratio: {e}")

    # 2) Fallback: find the max page number from aria-labels (Page/Seite)
    try:
        # This collects all page buttons (not previous/next)
        page_btns = driver.find_elements(By.CSS_SELECTOR, '[data-testid="srp-pagination"] button[aria-label]')
        nums = []
        for b in page_btns:
            al = (b.get_attribute("aria-label") or "").strip()
            # match "Page 6" or "Seite 50"
            m = re.search(r'(?:Page|Seite)\s*(\d+)', al, flags=re.IGNORECASE)
            if m:
                nums.append(int(m.group(1)))
        if nums:
            total = max(nums)
            logger(f"Total pages: {total} (from aria-label max)")
            return total
    except Exception as e:
        logger(f"Could not read total pages from page buttons: {e}")

    logger("Total pages not found.")
    return None

# print("total pages")
# print(get_total_pages(driver))

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# here a function that will do pagination and get links from all articals on current page

import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
print("geting time")
time1=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(time1)
# ✅ Create CSV once (header)
with open(f'article_links_{time1}.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Link'])

seen = set()
i=0
total_pages=get_total_pages(driver)
l=0
# ✅ RUN UNTIL "Continue" IS NOT PRESENT / DISABLED
while True:
    
    print(f"total pages {total_pages}")

    i+=1
    # 1) Wait for all article elements to load on CURRENT page
    print("waiting for articles to locate")
    articles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article a[href]"))
    )
    print("all article visible")
    WebDriverWait(driver, 30).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # 2) Extract href from each article (avoid duplicates)
    href_links = []
    for article in articles:
        link = article.get_attribute("href")
        # if link and link not in seen:
        if link:
            seen.add(link)
            href_links.append(link)
        else:
            print("links not present or already in seen")

    # 3) Print links
    for link in href_links:
        pass
        # print(link)
    print(f"uncoment to see all {len(href_links)} links")
    # 4) Append current page links into CSV
    
    if href_links:
        j=0
        with open(f'article_links_{time1}.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for link in href_links:
                writer.writerow([link])
                l+=1
                j+=1
            print(f"that number of total links found {l},  current page links {j}, actual total searches {total_searches}")
    # (Optional) Debug pause
    # get_input("line 223")

    # 5) Remember a stable element to detect page change
    first_article = articles[0]
    old_url = driver.current_url
    # 6) Try to click Continue (your function handles enabled/disabled/not-found)
    clicked = click_continue_if_enabled(driver)
    print(f"clicked on continue {i} out of {total_pages}")

    # 7) Stop when Continue is not present OR disabled
    if i==total_pages:
        print("Stop: Continue button not present or disabled.")
        break

    # 8) Wait until the next page loads
    

    # if clicked:
    #     WebDriverWait(driver, 15).until(lambda d: d.current_url != old_url)
    # else:
    #     print("Continue not present or disabled.")


print(f"Links saved to 'article_links_{time1}.csv'")








# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# code for scraping details of single artical



# Function to scrape the car details from the provided link
# function being used
def scrape_car_details(soup):
    """
    Extract the key features section from the listing page.  This
    function iterates over all elements whose ``data-testid`` begins with
    ``vip-key-features-list-item`` and maps the suffix to a more
    descriptive dictionary key.  It supports keys like mileage, power,
    fuel, transmission, first registration, and number of previous
    owners.  Unknown suffixes fall back to their original name.

    Parameters:
        soup: BeautifulSoup object representing the listing page.

    Returns:
        A dictionary where each key corresponds to a car attribute and
        each value is the extracted text.
    """
    car_details: dict[str, str] = {}
    try:
        # Mapping from the data-testid suffix to our preferred keys.  Keys not
        # present in this map will be converted from camelCase or PascalCase
        # to snake_case automatically.  This helps capture future fields
        # without manual updates.
        key_map = {
            'mileage': 'mileage',
            'power': 'power',
            'fuel': 'fuel_type',
            'transmission': 'transmission',
            'firstRegistration': 'first_registration',
            'numberOfPreviousOwners': 'previous_owners',
            'bodyType': 'body_type',
            'seats': 'number_of_seats',
            'doorCount': 'door_count',
            'cubicCapacity': 'cubic_capacity',
            'driveType': 'drive_type',
            # Add more explicit mappings here as needed
        }

        # Helper to convert camelCase/PascalCase strings to snake_case
        def camel_to_snake(name: str) -> str:
            import re
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

        # Loop through all key feature items
        for item in soup.select('[data-testid^="vip-key-features-list-item"]'):
            dtid = item.get('data-testid', '')
            suffix = dtid.split('vip-key-features-list-item-')[-1]
            # Map known suffixes to friendly key names; otherwise convert camelCase
            key = key_map.get(suffix, camel_to_snake(suffix))
            # The value is contained in a nested div with class geJSa or spans inside
            val_div = item.find('div', class_='geJSa')
            # In some layouts, the value might be within a span instead of a div
            if not val_div:
                val_div = item.find('span')
            if val_div:
                value = val_div.get_text(strip=True)
                car_details[key] = value
        return car_details
    except Exception as e:
        print(f"Error while scraping key features: {e}")
        return {}




# its being used
def scrape_technical_data_from_element(soup):
    car_details = {}
    try:
        # Mapping of normalized DT labels to our desired keys.  A label is
        # normalized by stripping whitespace, colons and converting to
        # lowercase.  For multilingual support we include common German
        # equivalents where known.  Unknown labels will be stored using
        # the normalized text as the key.
        label_map = {
            'vehiclecondition': 'vehicle_condition',
            'fahrzeugzustand': 'vehicle_condition',
            'category': 'category',
            'fahrzeugtyp': 'category',
            'fahrzeugart': 'category',
            'bodytype': 'category',
            'modelrange': 'model_range',
            'modellreihe': 'model_range',
            'trimline': 'trim_line',
            'ausstattungslinie': 'trim_line',
            'line': 'trim_line',
            'vehiclenumber': 'vehicle_number',
            'fahrzeugnummer': 'vehicle_number',
            'availability': 'availability',
            'verfügbarkeit': 'availability',
            'origin': 'origin',
            'countryversion': 'origin',
            'herkunft': 'origin',
            'mileage': 'mileage',
            'kilometer': 'mileage',
            'kilometerstand': 'mileage',
            'cubiccapacity': 'cubic_capacity',
            'hubraum': 'cubic_capacity',
            'power': 'power',
            'leistung': 'power',
            'drivetype': 'drive_type',
            'antriebsart': 'drive_type',
            'fuel': 'fuel_type',
            'kraftstoff': 'fuel_type',
            'energyconsumption(comb.)': 'energy_consumption',
            'energieverbrauch(komb.)': 'energy_consumption',
            'co₂emissions(comb.)': 'co2_emissions',
            'co2emissions(comb.)': 'co2_emissions',
            'co₂-emissionen(komb.)': 'co2_emissions',
            'co₂class': 'co2_class',
            'co2class': 'co2_class',
            'schadstoffklasse': 'co2_class',
            'fuelconsumption(comb.)': 'fuel_consumption',
            'kraftstoffverbrauch(komb.)': 'fuel_consumption',
            'verbrauch(kombiniert)': 'fuel_consumption',
            # German-specific labels mapping to our canonical keys
            'kategorie': 'category',
            'baureihe': 'model_range',
            'kraftstoffart': 'fuel_type',
            'anzahlsitzpltze': 'number_of_seats',
            'anzahldertren': 'door_count',
            'getriebe': 'transmission',
            'erstzulassung': 'first_registration',
            'anzahlderfahrzeughalter': 'previous_owners',
        }

        # Helper to normalize dt text to match our keys
        def normalize_label(label: str) -> str:
            import re
            return re.sub(r'[^a-z0-9]', '', label.lower())

        # Parse all definition terms and their definitions
        dts = soup.find_all('dt')
        for dt_tag in dts:
            dd_tag = dt_tag.find_next('dd')
            if dd_tag:
                raw_key = dt_tag.get_text(strip=True)
                norm_key = normalize_label(raw_key)
                key = label_map.get(norm_key, norm_key)
                value = dd_tag.get_text(strip=True)
                car_details[key] = value

        # Fuel consumption details appear as multiple values under a single dt
        # with data-testid envkv.consumptionDetails.fuel-item.  If present,
        # capture all nested values as a list and assign to our
        # fuel_consumption key.
        fc_dt = soup.find('dt', {'data-testid': 'envkv.consumptionDetails.fuel-item'})
        if fc_dt:
            fc_values = [item.get_text(strip=True) for item in fc_dt.find_all('div', class_='Js08r')]
            # Use our standardized key
            car_details['fuel_consumption'] = fc_values

        # Feature list entries (equipment) are <li> elements with class
        # FtSYW.  Collect all features into a list.
        features = []
        for feature_li in soup.find_all('li', class_='FtSYW'):
            feature_name = feature_li.get_text(strip=True)
            features.append(feature_name)
        # Only include features if we found any
        if features:
            car_details['features'] = features

    except Exception as e:
        print(f"Error extracting technical data: {e}")
        return {}
    return car_details



# being used
def scrape_car_details_from_element(soup):
    """
    Extract high‑level listing details from the HTML soup.  This function
    collects the title, additional info, price, seller/dealer info,
    location, phone, monthly financing details, rating, negotiability
    and seller type.  Where possible, it uses stable CSS selectors or
    `data-testid` hooks.  Missing values are reported as 'Not found'.
    """
    car_details: dict[str, str] = {}
    try:
        # Title (e.g., "Mercedes‑Benz 190")
        title = soup.find('h2', {'class': 'dNpqi'})
        car_details['title'] = title.get_text(strip=True) if title else 'Not found'

        # Additional description/variant (often empty string when none)
        additional_info = soup.find('div', {'class': 'GOIOV fqe3L EevEz'})
        car_details['additional_info'] = additional_info.get_text(strip=True) if additional_info else 'Not found'

        # Price (value inside VIP price label)
        price = soup.find(attrs={'data-testid': 'vip-price-label'})
        if price:
            car_details['price'] = price.get_text(strip=True)
        else:
            # fallback class
            price_div = soup.find('div', {'class': 'HBWcC'})
            car_details['price'] = price_div.get_text(strip=True) if price_div else 'Not found'

        # Dealer rating (stars or textual rating) – fallback to existing class
        dealer_rating = soup.find('span', {'class': 'qHfAA'})
        car_details['dealer_rating'] = dealer_rating.get_text(strip=True) if dealer_rating else 'Not found'

        # Dealer/seller company name if available
        dealer = soup.find('a', {'class': 'FWtU1 rqVIk lZcLh'})
        car_details['dealer'] = dealer.get_text(strip=True) if dealer else 'Not found'

        # Rating (like "No rating" or stars) from the price evaluation component
        vip_rating = soup.find('div', {'class': '_u77E'})
        car_details['rating'] = vip_rating.get_text(strip=True) if vip_rating else 'Not found'

        # Negotiability (e.g., "Negotiable")
        negotiable_div = soup.find('div', {'class': 'HaBLt ZD2EM'})
        car_details['negotiable'] = negotiable_div.get_text(strip=True) if negotiable_div else 'Not found'

        # Monthly financing rate and link
        monthly_rate_block = soup.find(attrs={'data-testid': 'vip-financing-monthly-rate'})
        if monthly_rate_block:
            rate_link = monthly_rate_block.find('a', href=True)
            if rate_link:
                car_details['monthly_rate'] = rate_link.get_text(strip=True)
                car_details['monthly_rate_href'] = rate_link['href']
            else:
                car_details['monthly_rate'] = monthly_rate_block.get_text(strip=True)
                car_details['monthly_rate_href'] = 'Not found'
        else:
            # fallback: anchor with class cCGm3 (legacy)
            monthly_rate = soup.find('a', {'class': 'cCGm3'})
            car_details['monthly_rate'] = monthly_rate.get_text(strip=True) if monthly_rate else 'Not found'
            car_details['monthly_rate_href'] = monthly_rate['href'] if monthly_rate and monthly_rate.has_attr('href') else 'Not found'

        # Seller block: type, location, phone.  `data-testid="seller-title-address"` wraps these.
        seller_block = soup.find(attrs={'data-testid': 'seller-title-address'})
        if seller_block:
            # Seller type (e.g., "Private Seller" or dealer name)
            seller_type_div = seller_block.find('div', {'class': 'QTTRi'})
            car_details['seller_type'] = seller_type_div.get_text(strip=True) if seller_type_div else 'Not found'

            # Location (e.g., "DE-26831 Bunde")
            loc_div = seller_block.find('div', {'class': 'olCKS'})
            car_details['location'] = loc_div.get_text(strip=True) if loc_div else 'Not found'

            # Phone (masked phone number)
            phone_span = seller_block.find('span', attrs={'aria-live': 'polite'})
            car_details['phone'] = phone_span.get_text(strip=True) if phone_span else 'Not found'
        else:
            # Fallback: original location and phone extraction
            loc_div = soup.find('div', {'class': 'olCKS HaBLt'})
            car_details['location'] = loc_div.get_text(strip=True) if loc_div else car_details.get('location', 'Not found')
            phone_h4 = soup.find('h4', {'class': 'DaDwz fpviJ DyuPj'})
            car_details['phone'] = phone_h4.get_text(strip=True) if phone_h4 else car_details.get('phone', 'Not found')

        # If monthly_rate_href was captured, populate the generic financing_link for backwards compatibility
        if 'monthly_rate_href' in car_details and not car_details.get('financing_link'):
            car_details['financing_link'] = car_details['monthly_rate_href']
        return car_details
    except Exception as e:
        print(f"Error extracting car details: {e}")
        return {}


# /////////////////////////////////////////////////////////////////////////////////////////////////////


import csv
import os

def write_car_details_to_csv(car_details, output_file):
    """Write or append car details to CSV."""
    try:
        # Check if the file exists before opening
        file_exists = os.path.isfile(output_file)
        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # If the file does not exist or is empty, write headers
            if not file_exists or os.stat(output_file).st_size == 0:
                # Write CSV header with additional fields for seller type, rating and negotiability
                writer.writerow([
                    "URL", "Title", "Additional Info", "Price", "Dealer Rating", "Dealer",
                    "Seller Type", "Location", "Phone", "Rating", "Negotiable",
                    "Monthly Rate", "Monthly Rate Link", "Financing Link",
                    "Mileage", "Power", "Fuel Type", "Transmission", "First Registration",
                    "Vehicle Condition", "Category", "Model Range", "Trim Line", "Vehicle Number", "Origin",
                    "Cubic Capacity", "Drive Type", "Energy Consumption", "CO2 Emissions",
                    "CO2 Class", "Fuel Consumption", "Features","Image URLS"
                ])
            # Write the row of car details
            writer.writerow([
                car_details.get('url', ''),
                car_details.get('title', ''),
                car_details.get('additional_info', ''),
                car_details.get('price', ''),
                car_details.get('dealer_rating', ''),
                car_details.get('dealer', ''),
                car_details.get('seller_type', ''),
                car_details.get('location', ''),
                car_details.get('phone', ''),
                car_details.get('rating', ''),
                car_details.get('negotiable', ''),
                car_details.get('monthly_rate', ''),
                car_details.get('monthly_rate_href', ''),
                car_details.get('financing_link', ''),
                car_details.get('mileage', ''),
                car_details.get('power', ''),
                car_details.get('fuel_type', ''),
                car_details.get('transmission', ''),
                car_details.get('first_registration', ''),
                car_details.get('vehicle_condition', ''),
                car_details.get('category', ''),
                car_details.get('model_range', ''),
                car_details.get('trim_line', ''),
                car_details.get('vehicle_number', ''),
                car_details.get('origin', ''),
                car_details.get('cubic_capacity', ''),
                car_details.get('drive_type', ''),
                car_details.get('energy_consumption', ''),
                car_details.get('co2_emissions', ''),
                car_details.get('co2_class', ''),
                car_details.get('fuel_consumption', ''),
                ", ".join(car_details.get('features', [])),
                ", ".join(car_details.get('img_urls', []))
            ])
    except Exception as e:
        print(f"Error writing to CSV: {e}")

# //////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////
# Helper to reveal the full phone number on a listing page.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def reveal_full_phone(driver, timeout: int = 10) -> str | None:
    """
    Clicks the 'Show' phone button and returns the full phone number once revealed.
    Returns None if not found or failed within the timeout.
    """
    try:
        wait = WebDriverWait(driver, timeout)

        # Find and click the "show phone" button via JavaScript to bypass overlays
        show_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="seller-phone-button"]')
            )
        )
        driver.execute_script("arguments[0].click();", show_btn)

        # Wait until the <span aria-live="polite"> contains a full number (no ellipsis)
        def full_number_loaded(drv):
            span = drv.find_element(
                By.CSS_SELECTOR,
                "[data-testid='phone-reveal-details'] span[aria-live='polite']"
            )
            return span if "..." not in span.text and "…" not in span.text else False

        phone_span = wait.until(full_number_loaded)

        # Return the cleaned phone text
        return phone_span.text.strip()

    except Exception:
        return None






# ///////////////////////////////////////////////////////////////////////////////
from bs4 import BeautifulSoup

def extract_image_urls(html: str) -> list[str]:
    """
    Given the inner HTML of the mRJ5K div, return all unique
    image URLs (from src and srcset attributes).
    """
    soup = BeautifulSoup(html, "html.parser")
    urls = set()
    for img in soup.find_all("img"):
        # Get the 'src' URL
        src = img.get("src")
        if src:
            urls.add(src)
        # Extract URLs from the 'srcset' attribute
        srcset = img.get("srcset")
        if srcset:
            # Each entry in srcset is "URL size", split by comma
            for part in srcset.split(","):
                url = part.strip().split()[0]
                urls.add(url)
    return list(urls)

# Example usage with the innerHTML of the mRJ5K container:
from selenium.webdriver.common.by import By

# Suppose 'driver' is your Selenium WebDriver and you are on the listing page.


# ///////////////////////////////////////////////////////////////////////////////////////////////////////

import os
import csv
from urllib.parse import urlsplit, parse_qs
from urllib.parse import urlsplit, parse_qs, urlunsplit, urlencode
#if normalize url needed
def normalize_mobile_url(url: str) -> str:
    """
    Keep only:
    https://suchen.mobile.de/fahrzeuge/details.html?id=<ID>
    """
    if not url:
        return ""

    url = url.strip()

    try:
        parts = urlsplit(url)
        qs = parse_qs(parts.query)

        listing_id = (qs.get("id") or [""])[0].strip()
        if not listing_id:
            return ""

        clean_query = urlencode({"id": listing_id})
        return urlunsplit((parts.scheme, parts.netloc, parts.path, clean_query, ""))

    except Exception:
        return ""

# -------------------- URL NORMALIZER (compare safely) --------------------
# if only id is needed
def extract_mobile_listing_id(url: str) -> str:
    """Return only the listing id from a mobile.de details URL."""
    if not url:
        return ""
    try:
        qs = parse_qs(urlsplit(url.strip()).query)
        return (qs.get("id") or [""])[0].strip()
    except Exception:
        return ""

# -------------------- CSV READER --------------------
def read_links_from_csv(file_path, col_no=0):
    links = []
    if not os.path.exists(file_path):
        return links

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # safe skip header
        for row in reader:
            if len(row) > col_no and row[col_no].strip():
                links.append(row[col_no].strip())
    return links

# -------------------- LOAD INPUT LINKS --------------------
links = read_links_from_csv(f"article_links_{time1}.csv", 0)

# -------------------- LOAD ALREADY SCRAPED LINKS --------------------
scraped_links = read_links_from_csv("car_details_output.csv", 0)

# BEST: compare by listing id (stable)
scraped_ids_set = {extract_mobile_listing_id(u) for u in scraped_links if extract_mobile_listing_id(u)}
output_file = 'car_details_output.csv'
# -------------------- PROCESS ONLY UNIQUE LINKS --------------------
for i, link in enumerate(links, start=1):
    if not link or not link.strip():
        continue

    listing_id = extract_mobile_listing_id(link)

    # if link is not a valid mobile details link (no id), skip
    if not listing_id:
        print(f"[{i}/{len(links)}] Skipping (no id found) -> {link.strip()}")
        continue

    if listing_id in scraped_ids_set:
        print(f"[{i}/{len(links)}] Already scraped -> id={listing_id}")
        continue

    print(f"[{i}/{len(links)}] Unique -> id={listing_id} | {link.strip()}")

    # ---------------- SCRAPE HERE ----------------
    # scrape(link)

    # after successful scrape, add to set so duplicates in same run are also skipped
    scraped_ids_set.add(listing_id)

    
    try:
        i+=1
        driver.get(link)  # Open the URL
        # print(f"Opening: {link}")
        print(f"\nopening link no {i} of {len(links)}\n\n\n\n")
        time.sleep(3)


        
        try:
        
            print("got driver")

            wait = WebDriverWait(driver, 20)
            print("wait is done")
            reveal_full_phone(driver)
            # Click the phone reveal button
            show_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="seller-phone-button"]'))
            )
            driver.execute_script("arguments[0].click();", show_btn)
            print("working for now")

            # Wait for the <span aria-live="polite"> to show the full number (no ellipsis)
            def full_number_loaded(drv):
                span = drv.find_element(By.CSS_SELECTOR, "[data-testid='phone-reveal-details'] span[aria-live='polite']")
                return span if '...' not in span.text else False

            phone_span = wait.until(full_number_loaded)
            phone_text = phone_span.text  # e.g., '+36 70 418 2659'
            print("Phone number:", phone_text)

        except Exception as e:
            print("An error occurred:", e)
        time.sleep(5)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////
        container = driver.find_element(By.CSS_SELECTOR, "div.mRJ5K")
        html = container.get_attribute("innerHTML")
        image_urls = extract_image_urls(html)
        # print("Found image URLs:", image_urls)
        print("uncoment to see image urls")
        # Scrape the car details using the correct page source
        page_source = driver.page_source  # Get the page content
        soup = BeautifulSoup(page_source, 'html.parser')  # Parse the page source with BeautifulSoup


# //////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Extract car details using various functions
        technical_data = scrape_technical_data_from_element(soup)
        # print("Technical Data from Element:", technical_data)

        car_details = scrape_car_details(soup)  # General car details
        # print("Car Details:", car_details)

        car_details_from_element = scrape_car_details_from_element(soup)  # Car details from another element
        # print("Car Details from Element:", car_details_from_element)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Combine all data into a single dictionary
        combined_car_details = {
    "url": link,
    'img_urls':image_urls,   
          # note lowercase key and comma after link
    **car_details_from_element,
    **car_details,
    **technical_data
    }

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


        # Print the final combined car details
        # print("\n Combined Car Details:", combined_car_details)
        print("\nuncoment to see Combined Car Details\n")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # If car details are found, write them to CSV
        if combined_car_details:
            write_car_details_to_csv(combined_car_details, output_file)
        else:
            print('Car details not found')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # get_input("line 76")  # Wait for user input to proceed to the next iteration

    except Exception as e:
        # print(f"Error opening {link}: {e}")
        print("error opening link")

print(f"\ndata extraction is done\n")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Close the browser after visiting all links
driver.quit()