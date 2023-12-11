# Locally Running Exchange API

This python API uses selenium to get the latest currency data from google-finance, and even better: it's completely free unlike those bs web API's that charge 20$ a month for the exact same thing.

It takes about ~5 seconds to fetch data due to selenium launching the browser, you can speed it up with a better browser probably.

Usage:
```
  import exchange
  print(exchange.get_latest("USD", "EUR")) #This will print USD/EUR, from google finance
```
