# Currency Converter (Django)

A simple Django-based currency converter that lets users convert amounts between different currencies using the ExchangeRate-API.

---

## 🚀 Features

* Enter an amount, select **From** and **To** currencies, and get the converted result.
* Validates input to ensure it's a positive number.
* Handles errors gracefully and displays user-friendly messages.
* Supports commonly used currencies: USD, INR, EUR, GBP, AUD, CAD, JPY, CNY.

---

## 🛠️ Installation & Setup

1. **Clone the repo:**

   ```bash
   git clone https://github.com/Boradjash29/currency_converter.git
   cd currency_converter/currency_project
   ```
2. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

3. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
currency_project/
├── converter/
│   ├── templates/converter/index.html
│   ├── views.py
│   └── urls.py
├── currency_project/
│   └── settings.py, urls.py
└── manage.py
```

---

## ✍️ Code Walkthrough

### `views.py`

```python
import requests
from django.shortcuts import render

CURRENCIES = ['USD', 'INR', 'EUR', 'GBP', 'AUD', 'CAD', 'JPY', 'CNY']
```

* Imports the `requests` library to make API calls.
* `CURRENCIES` is a list used to populate currency dropdowns.

```python
def convert_currency(request):
    result = None
    error = None
```

* Initializes `result` and `error` variables to store outputs and error messages.

```python
if request.method == 'POST':
    try:
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
```

* When the form is submitted, retrieves and validates user inputs (amount must be positive).

```python
api_key = 'd11ba643ced2f5389e2acaf3'
url = (
  f'https://v6.exchangerate-api.com/v6/'
  f'{api_key}/pair/{from_currency}/{to_currency}/{amount}'
)
response = requests.get(url)
data = response.json()
```

* Builds the API URL and fetches conversion data.

```python
if data['result'] == 'success':
    result = data['conversion_result']
else:
    error = "Conversion failed. Please try again."
```

* Checks API response and extracts the result or error.

```python
except ValueError:
    error = "Please enter a valid, positive amount."
except Exception as e:
    error = f"An unexpected error occurred: {str(e)}"
```

* Handles validation errors and unexpected issues (e.g., network, DNS failures).

```python
context = {
    'currencies': CURRENCIES,
    'amount': request.POST.get('amount'),
    'from_currency': request.POST.get('from_currency'),
    'to_currency': request.POST.get('to_currency'),
    'result': result,
    'error': error,
}
return render(request, 'converter/index.html', context)
```

* Packages all data into `context` and renders the template with values or errors.

```python
return render(request, 'converter/index.html', {
    'currencies': CURRENCIES
})
```

* For GET requests, renders the form with dropdowns only.

---

### `index.html`

* Contains a form to input the amount and select currencies.
* Uses POST to submit user input and CSRF protection for security.
* Displays `result` if conversion is successful or `error` if any message is present.
* Dynamically populates currency dropdowns using `currencies` list.

---

## ✅ Usage Flow

1. Load home page → see form with two dropdowns and amount input.
2. Fill in amount and select currencies.
3. Submit → Django view sends API request and returns conversion or error.
4. View updated template with result or error message.

---

## 🔧 Improvements

* **API Resilience**: Use a fallback API or catch downtime gracefully.
* **Input Validations**: Add form validation via Django Forms.
* **Caching**: Store recent API results to reduce API calls.
* **Extended Support**: Add more currencies or display exchange rate history.

---
