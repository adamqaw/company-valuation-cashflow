import requests
import pandas as pd
import os




class Finance:
  API_KEY = '896123476cd9c8becbc6e08ba9eb5108'

  companies_response = requests.get(f'https://fmpcloud.io/api/v3/stock-screener?sector=technology&marketCapMoreThan=100000000000&limit=100&apikey={API_KEY}')
  companies = companies_response.json()
  
  def get_cash_flow_annual(company):
    cf_annual_endpoint = f'https://fmpcloud.io/api/v3/cash-flow-statement/{company}?limit=120&apikey={API_KEY}'
    cf_annual_response = requests.get(cf_annual_endpoint)


cash_flow_response = ''
    
tech_companies = []

for item in companies:
  tech_companies.append(item['symbol'])

