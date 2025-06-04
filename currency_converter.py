import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "https://open.er-api.com/v6/latest/{}"  # base currency placeholder

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("350x200")
        self.resizable(False, False)

        # Currency options
        self.currencies = self.fetch_currencies()
        # Default values
        self.base_currency = tk.StringVar(value="USD")
        self.target_currency = tk.StringVar(value="EUR")
        self.amount_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def fetch_currencies(self):
        """Retrieve available currency codes from the API."""
        try:
            resp = requests.get(API_URL.format("USD"), timeout=10)
            data = resp.json()
            if data.get("result") == "success":
                return sorted(data["rates"].keys())
        except Exception as e:
            print(f"Could not fetch currency list: {e}")
        # Fallback to common currencies if API fails
        return ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY"]

    def create_widgets(self):
        padding = {"padx": 10, "pady": 5}

        ttk.Label(self, text="Amount").grid(column=0, row=0, **padding)
        amount_entry = ttk.Entry(self, textvariable=self.amount_var)
        amount_entry.grid(column=1, row=0, **padding)

        ttk.Label(self, text="From").grid(column=0, row=1, **padding)
        from_combo = ttk.Combobox(self, values=self.currencies, textvariable=self.base_currency, state="readonly")
        from_combo.grid(column=1, row=1, **padding)

        ttk.Label(self, text="To").grid(column=0, row=2, **padding)
        to_combo = ttk.Combobox(self, values=self.currencies, textvariable=self.target_currency, state="readonly")
        to_combo.grid(column=1, row=2, **padding)

        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        convert_button.grid(column=0, row=3, columnspan=2, **padding)

        ttk.Label(self, text="Result").grid(column=0, row=4, **padding)
        result_entry = ttk.Entry(self, textvariable=self.result_var, state="readonly")
        result_entry.grid(column=1, row=4, **padding)

    def convert(self):
        amount_str = self.amount_var.get()
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for the amount.")
            return

        base = self.base_currency.get()
        target = self.target_currency.get()

        try:
            resp = requests.get(API_URL.format(base), timeout=10)
            data = resp.json()
            if data.get("result") != "success":
                raise ValueError("API error")
            rate = data["rates"].get(target)
            if rate is None:
                raise ValueError("Currency not found")
            converted = amount * rate
            self.result_var.set(f"{converted:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve rates: {e}")


def main():
    app = CurrencyConverter()
    app.mainloop()


if __name__ == "__main__":
    main()
