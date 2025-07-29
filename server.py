import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates'

mcp = FastMCP('currency-conversion-and-exchange-rates')

@mcp.tool()
def time_series_endpoint(start_date: Annotated[str, Field(description='')],
                         end_date: Annotated[str, Field(description='')],
                         base: Annotated[Union[str, None], Field(description='Three-letter currency code of the currency would would like to convert from. This currency will be converted into the code of the currency provided in the to parameter')] = None,
                         symbols: Annotated[Union[str, None], Field(description='A comma-separated list of currency codes to convert the from parameter into.')] = None) -> dict: 
    '''Retrieve historical rates between two specified dates. `Maximum of 365 day time range`'''
    url = 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/timeseries'
    headers = {'x-rapidapi-host': 'currency-conversion-and-exchange-rates.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'start_date': start_date,
        'end_date': end_date,
        'base': base,
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def convert(_from: Annotated[str, Field(description='The three-letter currency code of the currency you would like to convert from.')],
            to: Annotated[str, Field(description='The three-letter currency code of the currency you would like to convert to.')],
            amount: Annotated[str, Field(description='The amount to be converted.')],
            date: Annotated[Union[str, None], Field(description='Optionally, provide a specific date (format YYYY-MM-DD) to use historical rates for this conversion.')] = None) -> dict: 
    '''In addition to providing converstion rates, our API provides a dedicated endpoint to easily do conversion on a specific amount of the currency.'''
    url = 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert'
    headers = {'x-rapidapi-host': 'currency-conversion-and-exchange-rates.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
        'amount': amount,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def symbols() -> dict: 
    '''Retrieve a list of all currently available currency symbols'''
    url = 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/symbols'
    headers = {'x-rapidapi-host': 'currency-conversion-and-exchange-rates.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def historical_exchange_rates(base: Annotated[Union[str, None], Field(description='Three-letter currency code of the currency would would like to convert from. This currency will be converted into the code of the currency provided in the to parameter')] = None,
                              symbols: Annotated[Union[str, None], Field(description='A comma-separated list of currency codes to convert the from parameter into.')] = None) -> dict: 
    '''Retrieve historical exchange rate data. Data is available for most currencies all the way back to the year of 1999.'''
    url = 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/2019-10-16'
    headers = {'x-rapidapi-host': 'currency-conversion-and-exchange-rates.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'base': base,
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recent_exchange_rates(base: Annotated[Union[str, None], Field(description='Three-letter currency code of the currency would would like to convert from. This currency will be converted into the code of the currency provided in the to parameter')] = None,
                          symbols: Annotated[Union[str, None], Field(description='A comma-separated list of currency codes to convert the from parameter into.')] = None) -> dict: 
    '''Retrieve the latest exchange rate data. Refresh rate will depend on your subscription: updated every 60 minutes, every 10 minutes or every 60 seconds.'''
    url = 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest'
    headers = {'x-rapidapi-host': 'currency-conversion-and-exchange-rates.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'base': base,
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
