# class Bank:
#     def __init__(self, location, bank_name):
#         self.name = bank_name
#         self.loc = location
#     def bank_loc(self):
#         print(self.loc)
# class Account(Bank):
#     def __init__(self, account_holder, age, location, bank_name):
#         super().__init__(location, bank_name)
#         self.acc_hold_nome = account_holder
#         self.age = age
#     def bank_loc(self):
#         print(self.name)
#
# b = Bank('hyd', 'hdfc')
# a = Account('satish', 25, 'hyd', 'icici')
# a.bank_loc()
# b.bank_loc()

# def greetings(func):
#     def wrapper(*args, **kwargs):
#         print(f"Hello {args[0]}")
#         func(*args, **kwargs)
#     return wrapper
#
# @greetings
# def func(*args, **kwargs):
#     pass
#
# func("Satish")

# country_name = 'China'
# import requests
# url =  f"https://jsonmock.hackerrank.com/api/countries?name={country_name}"
# resp = requests.get(url)
# if resp.status_code==200:
#     print('done')
# data = resp.json()
# print(data['data'][0])
# capital = data['data'][0].get('capital', 'No capital found')
# print(capital)
#
# from fastapi import FastAPI, HTTPException
# import requests
#
# app = FastAPI()

# from fastapi import FastAPI, HTTPException
# import requests
#
# app = FastAPI()
# @app.get("/get-capital/")
# async def get_capital(country_name: str):
#     """
#     Fetch the capital of a country using the mock API.
#
#     :param country_name: The name of the country.
#     :return: The capital city or an appropriate message.
#     """
#     url = f"https://jsonmock.hackerrank.com/api/countries?name={country_name}"
#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             raise HTTPException(status_code=500, detail="Failed to fetch country data")
#
#         data = response.json()
#         # Ensure we handle cases where the country isn't found
#         if not data.get('data'):
#             raise HTTPException(status_code=404, detail=f"Country '{country_name}' not found")
#
#         country_data = data['data'][0]
#         capital = country_data.get('capital', 'No capital found')
#         return {"country": country_name, "capital": capital}
#
#     except requests.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")




