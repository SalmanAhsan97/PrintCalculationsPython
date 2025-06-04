# Currency Converter Application

This repository contains a simple Python application that converts amounts between
major currencies. It uses the [ERAPI](https://www.exchangerate-api.com/) to
retrieve the latest exchange rates.

The app is built with Tkinter, so it should run on macOS, Windows and Linux
without additional dependencies other than Python itself.

## Requirements

- Python 3.8 or newer
- `requests` package (install with `pip install requests`)

Tkinter comes bundled with the standard Python installation on macOS. If you are
using a custom Python build that does not include Tkinter, you may need to
install it separately.

## Running the application

1. Make sure you have Python and `pip` installed.
2. Install the required package:
   ```bash
   pip install requests
   ```
3. Start the converter GUI by running:
   ```bash
   python currency_converter.py
   ```

Enter the amount, choose the currencies to convert from and to, and press
**Convert** to see the result.

## Offline mode

If the application cannot reach the exchange rate API, it will fall back to a
short list of common currencies. Rates may be unavailable in this mode.
