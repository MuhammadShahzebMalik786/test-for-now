# Mobile.de Scraper - Linux Headless Version

This is a headless web scraper for mobile.de (German car marketplace) optimized for Linux servers and headless environments.

## Features

- **Headless Operation**: Runs without GUI, perfect for servers
- **Linux Optimized**: Configured for Linux environments with proper Chrome options
- **Robust Error Handling**: Handles network issues and page loading problems
- **CSV Output**: Saves data in structured CSV format
- **Resume Capability**: Skips already scraped listings
- **Configurable**: Easy to customize search parameters

## Key Changes from Windows Version

1. **Removed GUI Dependencies**: No tkinter input dialogs
2. **Added Linux Chrome Options**: `--no-sandbox`, `--disable-dev-shm-usage`
3. **Headless Mode**: Always runs in headless mode
4. **System Chrome**: Uses system-installed Chrome instead of bundled driver
5. **Better Error Handling**: More robust error handling for headless environment

## Installation

### Automatic Setup (Recommended)
```bash
chmod +x setup_linux.sh
./setup_linux.sh
```

### Manual Setup
```bash
# Install Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable

# Install Python dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_linux.txt
```

## Usage

1. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run the scraper:**
   ```bash
   python3 mobile_scraper_linux_headless.py
   ```

3. **Check output files:**
   - `article_links_YYYY-MM-DD_HH-MM-SS.csv` - Collected article links
   - `car_details_output.csv` - Scraped car details

## Configuration

Edit `config.py` to customize:
- Car make and model
- Search parameters
- Delays and timeouts
- Chrome options

## Common Issues & Solutions

### Chrome/ChromeDriver Issues
```bash
# Check Chrome version
google-chrome --version

# Install missing dependencies
sudo apt install -y libnss3 libgconf-2-4 libxss1 libappindicator1 libindicator7
```

### Permission Issues
```bash
# Make sure script is executable
chmod +x mobile_scraper_linux_headless.py

# Run with proper permissions
sudo python3 mobile_scraper_linux_headless.py
```

### Memory Issues (for low-memory systems)
Add these Chrome options in config.py:
```python
"--memory-pressure-off",
"--max_old_space_size=4096"
```

## Output Format

The scraper generates CSV files with the following data:
- Basic info: Title, Price, Location
- Technical specs: Mileage, Power, Fuel Type
- Seller info: Dealer, Phone, Rating
- Images: URLs to all car photos
- Features: Equipment and options list

## Performance Tips

1. **Run during off-peak hours** to avoid rate limiting
2. **Use delays** between requests to be respectful
3. **Monitor memory usage** on low-spec systems
4. **Resume interrupted runs** - the scraper skips already processed listings

## Legal Notice

This scraper is for educational purposes. Please:
- Respect mobile.de's terms of service
- Don't overload their servers
- Use reasonable delays between requests
- Consider their robots.txt file

## Troubleshooting

### Script won't start
- Check Python version: `python3 --version`
- Verify Chrome installation: `google-chrome --version`
- Check virtual environment: `which python`

### No data scraped
- Check internet connection
- Verify mobile.de is accessible
- Look for consent/cookie dialogs
- Check Chrome logs in terminal

### Memory errors
- Reduce batch size
- Add memory limits to Chrome options
- Close other applications

## Support

For issues specific to this Linux version, check:
1. Chrome installation and version
2. Python dependencies
3. System permissions
4. Network connectivity

Original Windows version functionality has been preserved while optimizing for headless Linux operation.
