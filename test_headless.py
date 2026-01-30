#!/usr/bin/env python3


import requests

def get_public_ip():
    """Fetch the public IP address of the router."""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def get_ip_location(ip):
    """Fetch geolocation details for the given IP address."""
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "success":
            return {
                "IP": ip,
                "Country": data.get("country"),
                "Region": data.get("regionName"),
                "City": data.get("city"),
                "ZIP": data.get("zip"),
                "Latitude": data.get("lat"),
                "Longitude": data.get("lon"),
                "ISP": data.get("isp")
            }
        else:
            print(f"Error from API: {data.get('message')}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching location: {e}")
        return None

if __name__ == "__main__":
    ip = get_public_ip()
    if ip:
        location = get_ip_location(ip)
        if location:
            print("\nRouter Location Details:")
            for key, value in location.items():
                print(f"{key}: {value}")


print("Testing basic headless Chrome functionality...")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_headless_chrome():
    """Test basic headless Chrome functionality"""
    print("Setting up headless Chrome...")
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    try:
        driver = webdriver.Chrome(options=options)
        print("✅ Chrome driver initialized successfully")
        
        # Test basic navigation
        print("Testing navigation to Mobile.de...")
        driver.get("https://www.mobile.de/?lang=en")
        time.sleep(3)
        
        # Get page title
        title = driver.title
        print(f"✅ Page loaded successfully. Title: {title}")
        
        # Check if we can find basic elements
        page_source = driver.page_source
        if "mobile.de" in page_source.lower():
            print("✅ Page content loaded correctly")
        else:
            print("❌ Page content may not have loaded properly")
        
        # Test basic element finding
        try:
            body = driver.find_element("tag name", "body")
            print("✅ Can find page elements")
        except Exception as e:
            print(f"❌ Cannot find page elements: {e}")
        
        driver.quit()
        print("✅ Test completed successfully - Linux headless scraper is working!")
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        return False

if __name__ == "__main__":
    success = test_headless_chrome()
    if success:
        print("\n🎉 The Linux headless scraper setup is working correctly!")
        print("You can now run the full scraper: python3 mobile_scraper_linux_headless.py")
    else:
        print("\n❌ There are issues with the setup that need to be resolved.")


