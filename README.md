markdown
# currency-conversion-and-exchange-rates MCP Server

## Overview

The `currency-conversion-and-exchange-rates` MCP server provides a simple and reliable service for obtaining current exchange rates and historical foreign exchange (forex) rates. It offers tools for currency conversion, forex data retrieval, and payment calculations, enabling you to convert currencies such as dollars to euros effortlessly.

## Features

- **Current and Historical Exchange Rates**: Access both current and historical exchange rates for a wide range of currencies.
- **Currency Conversion**: Perform currency conversions with ease, leveraging up-to-date or historical rates.
- **Forex Data Retrieval**: Retrieve forex data for various currencies, with historical data available as far back as 1999.
- **Customizable Options**: Adjust parameters such as base currency and target currencies to suit your needs.

## Tools

### Time-Series Endpoint
- **Description**: Retrieve historical rates between two specified dates, with a maximum time range of 365 days.
- **Parameters**: 
  - `start_date` (required): The starting date for the historical data retrieval.
  - `end_date` (required): The ending date for the historical data retrieval.
  - `base` (optional): Three-letter currency code of the base currency.
  - `symbols` (optional): Comma-separated list of target currency codes.

### Convert
- **Description**: Provides a dedicated endpoint for currency conversion of a specific amount.
- **Parameters**:
  - `_from` (required): Currency code of the currency to convert from.
  - `to` (required): Currency code of the currency to convert to.
  - `amount` (required): The amount to be converted.
  - `date` (optional): Specific date for using historical rates.

### Symbols
- **Description**: Retrieve a list of all currently available currency symbols.
- **Parameters**: None.

### Historical Exchange Rates
- **Description**: Retrieve historical exchange rate data available from 1999 onward.
- **Parameters**:
  - `base` (optional): Currency code of the base currency.
  - `symbols` (optional): Comma-separated list of target currency codes.

### Recent Exchange Rates
- **Description**: Retrieve the latest exchange rate data with varying refresh rates depending on your subscription level.
- **Parameters**:
  - `base` (optional): Currency code of the base currency.
  - `symbols` (optional): Comma-separated list of target currency codes.

## Additional Features

If you have suggestions for additional currencies or data, feel free to send us a message. We are eager to hear your feedback and improve our services.

This MCP server is designed to be seamlessly integrated into your applications, providing localized currency conversion and exchange rate data to meet your needs.