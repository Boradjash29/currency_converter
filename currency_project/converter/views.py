import requests
from django.shortcuts import render

CURRENCIES = ['USD', 'INR', 'EUR', 'GBP', 'AUD', 'CAD', 'JPY', 'CNY']

def convert_currency(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            amount = float(request.POST['amount'])
            from_currency = request.POST['from_currency']
            to_currency = request.POST['to_currency']

    
            if amount <= 0:
                raise ValueError("Amount must be greater than 0.")

            
            api_key = 'd11ba643ced2f5389e2acaf3'
            url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}'

            
            response = requests.get(url)
            data = response.json()

            if data['result'] == 'success':
                result = data['conversion_result']
            else:
                error = "Conversion failed. Please try again."

        except ValueError:
            error = "Please enter a valid, positive amount."
        except Exception as e:
            error = f"An unexpected error occurred: {str(e)}"

        
        context = {
            'currencies': CURRENCIES,
            'amount': request.POST.get('amount'),
            'from_currency': request.POST.get('from_currency'),
            'to_currency': request.POST.get('to_currency'),
            'result': result,
            'error': error,
        }
        return render(request, 'converter/index.html', context)

    
    return render(request, 'converter/index.html', {
        'currencies': CURRENCIES
    })
