import streamlit as st
import requests

# Function to fetch exchange rates from the API
def fetch_exchange_rates(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        st.error("Failed to fetch exchange rates. Please check the API URL.")

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    try:
        from_rate = exchange_rates[from_currency]
        to_rate = exchange_rates[to_currency]
        converted_amount = amount * (to_rate / from_rate)
        return converted_amount
    except KeyError:
        st.error("Invalid currency code. Please enter valid currency codes.")

# Function to display help menu with currency codes and symbols
def display_help_menu():
    # Define the currency data with currency codes, names, and symbols
    currency_data = {
        "EUR": ("The European Union", "Euro", "€"),
        "USD": ("The United States of America", "US Dollar", "$"),
        "JPY": ("Japan", "Japanese Yen", "¥"),
        "BGN": ("The Republic of Bulgaria", "Bulgarian Lev", "лв"),
        "CZK": ("The Czech Republic", "Czech Koruna", "Kč"),
        "DKK": ("The Kingdom of Denmark", "Danish Krone", "kr"),
        "GBP": ("The United Kingdom of Great Britain and Northern Ireland", "British Pound Sterling", "£"),
        "HUF": ("Hungary", "Hungarian Forint", "Ft"),
        "PLN": ("The Republic of Poland", "Polish Zloty", "zł"),
        "RON": ("The Republic of Romania", "Romanian Leu", "lei"),
        "SEK": ("The Kingdom of Sweden", "Swedish Krona", "kr"),
        "CHF": ("Swiss Confederation (Switzerland)", "Swiss Franc", "Fr"),
        "ISK": ("Iceland", "Icelandic Króna", "kr"),
        "NOK": ("The Kingdom of Norway", "Norwegian Krone", "kr"),
        "HRK": ("The Republic of Croatia", "Croatian Kuna", "kn"),
        "RUB": ("The Russian Federation (Russia)", "Russian Ruble", "₽"),
        "TRY": ("The Republic of Turkey", "Turkish Lira", "₺"),
        "AUD": ("The Commonwealth of Australia (Australia)", "Australian Dollar", "$"),
        "BRL": ("Federative Republic of Brazil", "Brazilian Real", "R$"),
        "CAD": ("Dominion of Canada", "Canadian Dollar", "$"),
        "CNY": ("The People's Republic of China", "Chinese Yuan", "¥"),
        "HKD": ("Hong Kong Special Administrative Region of the People's Republic of China (Hong Kong)", "Hong Kong Dollar", "HK$"),
        "IDR": ("The Republic of Indonesia", "Indonesian Rupiah", "Rp"),
        "ILS": ("The State of Israel", "Israeli New Sheqel", "₪"),
        "INR": ("The Republic of India", "Indian Rupee", "₹"),
        "KRW": ("Republic of Korea (South Korea)", "South Korean Won", "₩"),
        "MXN": ("United Mexican States", "Mexican Peso", "Mex$"),
        "MYR": ("Malaysia", "Malaysian Ringgit", "RM"),
        "NZD": ("New Zealand", "New Zealand Dollar", "$"),
        "PHP": ("The Republic of the Philippines", "Philippine Peso", "₱"),
        "SGD": ("The Republic of Singapore", "Singapore Dollar", "S$"),
        "THB": ("The Kingdom of Thailand", "Thai Baht", "฿"),
    }

    st.subheader("Help Menu")
    st.write("Use this menu to input correct currency codes:")
    st.write("Currency Code \t\t\t Currency Name \t\t\t Country Name \t\t\t Currency Symbol")
    for currency_code, (country, currency_name, currency_symbol) in currency_data.items():
        st.write(f"{currency_code} \t\t\t {currency_name} ({country}) \t\t\t {currency_symbol}")


def homepage():
    st.title("Homepage")
    st.markdown('<style>h1 { font-family: "Times New Roman", Times, serif; }</style>', unsafe_allow_html=True)
    st.write("Welcome to the **Currency Converter Application**!")
    st.write("This application allows you to convert currencies using real-time exchange rates.")

def applications():
    st.title("Applications")
    st.write("This page demonstrates the currency conversion functionality using real-time exchange rates.")
    st.write("You can enter an amount and select source and target currencies to convert.")

    API_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_qrgPe54us4B2fNOzvU4VO3qYflJcm4g73ZCJsgpe"
    exchange_rates = fetch_exchange_rates(API_URL)

    amount = st.number_input("Enter amount:", min_value=0.01, step=0.01)

    from_currency = st.selectbox("Select source currency:", list(exchange_rates.keys()))
    from_currency_symbol = st.empty()
    from_currency_symbol.write(f"Source currency symbol: {exchange_rates[from_currency]} {from_currency}")

    to_currency = st.selectbox("Select target currency:", list(exchange_rates.keys()))
    st.write(f"Target currency symbol: {exchange_rates[to_currency]} {to_currency}")

    if st.button("Convert"):
        result = convert_currency(amount, from_currency, to_currency, exchange_rates)
        st.write(f"Converted amount: {result:.2f} {exchange_rates[to_currency]} {to_currency}")

    if st.button("Help"):
        display_help_menu()

def contact_information():
    st.title("Contact Information")
    st.write("Feel free to reach out to us for any questions, feedback, or support! We are always happy to help. 😊")
    st.subheader("Contact Information:")
    st.markdown("- **Email:** dijaskhan467@gmail.com")
    st.markdown("- **Phone:** +92 3190372796")
    st.markdown("- **Address:** Bano Qabil Korangi Campus, Sector 36E, Landhi Town, Karachi, Pakistan")
    st.subheader("Our Team:")
    st.markdown("LEADER: Sajid Khan")
    st.markdown("1st MEMBER: Abdullah Javed")
    st.markdown("2nd MEMBER: Syed Muhammad Anas")

# Add navigation between pages
PAGES = {
    "Homepage": homepage,
    "Applications": applications,
    "Contact Information": contact_information
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
