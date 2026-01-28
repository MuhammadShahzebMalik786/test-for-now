#!/bin/bash

echo "Setting up Mobile.de Scraper for Linux (Headless)"
echo "=================================================="

# Update system packages
echo "Updating system packages..."
sudo apt update

# Install Chrome dependencies
echo "Installing Chrome dependencies..."
sudo apt install -y wget gnupg software-properties-common apt-transport-https ca-certificates

# Install Google Chrome
echo "Installing Google Chrome..."
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable

# Install Python dependencies
echo "Installing Python dependencies..."
sudo apt install -y python3 python3-pip python3-venv

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python packages
echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements_linux.txt

echo ""
echo "Setup complete!"
echo ""
echo "To run the scraper:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run the scraper: python3 mobile_scraper_linux_headless.py"
echo ""
echo "Note: Make sure you have sufficient permissions and network access."
