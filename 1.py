import time
from seleniumwire import webdriver

driver = webdriver.Chrome()


# Define a request interceptor function
def my_request_interceptor(request):
    # Do something with the intercepted request
    print(f"Intercepted request: {request.url}")


# Set the request interceptor
driver.request_interceptor = my_request_interceptor

# Make requests
driver.get('https://qa.digift.ru/')

time.sleep(4)
driver.quit()
