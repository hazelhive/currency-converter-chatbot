from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():

    data = request.get_json()
    print(data)   # Debugging

    # Get source currency and amount
    unit_currency = data['queryResult']['parameters']['unit-currency'][0]

    source_currency = unit_currency['currency']
    amount = unit_currency['amount']

    # Get target currency
    target_currency = data['queryResult']['parameters']['currency-name']

    # Fetch conversion factor
    cf = fetch_conversion_factor(source_currency, target_currency)

    # Calculate final amount
    final_amount = round(amount * cf, 2)

    response = {
        "fulfillmentText": f"{amount} {source_currency} = {final_amount} {target_currency}"
    }

    return jsonify(response)


def fetch_conversion_factor(source, target):

    url = f"https://api.frankfurter.app/latest?from={source}&to={target}"

    response = requests.get(url)
    data = response.json()

    return data["rates"][target]


if __name__ == "__main__":
    app.run(debug=True)