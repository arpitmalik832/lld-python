from abc import ABC, abstractmethod


class ApiUtils:
    @staticmethod
    def log_request(request_data):
        print(f"Request data: {request_data}")

    @staticmethod
    def apply_rate_limit(request_data):
        print(f"Rate limit applied for request: {request_data}")


# Base API interface
class Api(ABC):
    @abstractmethod
    def execute_request(self, request_data) -> str:
        pass


# Concrete API implementation
class ECommerceApi(Api):
    def execute_request(self, request_data) -> str:
        print("Processing request:", request_data)
        return "Response data"


# Task 1 - Modify the class definition to inherit from the API class.
class BaseApiDecorator(Api, ABC):
    # Task 2 - Modify the __init__ method to store the API instance.
    def __init__(self, api: Api):
        if api is not None:
            self.api = api
        else:
            self.api = None

    # Task 3 - Add the execute_request method that calls the execute_request method of the API instance.
    def execute_request(self, request_data) -> str:
        if self.api is not None:
            self.api.execute_request(request_data)
        return ECommerceApi().execute_request(request_data)


class LoggingDecorator(BaseApiDecorator):
    # Task 4 - Modify the __init__ method to pass the API instance to the parent class.
    def __init__(self, api: Api):
        super().__init__(api)

    # Task 5 - Implement the execute_request method to log the request data and response data.
    def execute_request(self, request_data) -> str:
        ApiUtils.log_request(request_data)
        return super().execute_request(request_data)


class RateLimitDecorator(BaseApiDecorator):
    # Task 4 - Modify the __init__ method to pass the API instance to the parent class.
    def __init__(self, api: Api):
        super().__init__(api)

    # Task 5 - Implement the execute_request method to log the request data and response data.
    def execute_request(self, request_data) -> str:
        ApiUtils.apply_rate_limit(request_data)
        return super().execute_request(request_data)
