# 💱 Currency Converter Chatbot

A simple chatbot that converts one currency to another using real-time exchange rates. The project is built with Python and Flask, and uses Dialogflow to understand user queries. Exchange rates are fetched from the Frankfurter API.

## Features

- Convert currencies using live exchange rates
- Supports multiple international currencies
- Integrated with Dialogflow for natural language input
- Flask backend to handle webhook requests
- Returns quick and accurate conversion results

## Tech Stack

- Python
- Flask
- Dialogflow
- Frankfurter Exchange Rate API
- JSON

## Project Structure

```
currency-converter-chatbot/
│── app.py
│── requirements.txt
│── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hazelhive/currency-converter-chatbot.git
cd currency-converter-chatbot
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

The Flask server will start and wait for requests from Dialogflow.

## Example

**User:**

```
Convert 100 USD to INR
```

**Bot:**

```
100 USD is approximately 8650 INR.
```

*(The output will vary depending on the current exchange rate.)*

## How It Works

1. The user enters a currency conversion request in Dialogflow.
2. Dialogflow extracts the required parameters.
3. The request is sent to the Flask webhook.
4. Flask retrieves the latest exchange rate from the Frankfurter API.
5. The converted amount is calculated and returned to the user.

## Future Improvements

- Add support for historical exchange rates
- Build a web interface for direct user interaction
- Store conversion history
- Improve error handling for invalid currency codes
- Add support for voice input

## Author

**Subhashree Baisakh**

Integrated M.Sc. Physics, NIT Rourkela

GitHub: https://github.com/hazelhive
