from fastapi import HTTPException

class NoCityFoundError(HTTPException):
    """Exception raised when no city is found in geocode the response."""
    def __init__(self, message="No city found with the given name."):
        self.message = message
        super().__init__(404, self.message)

class OpenWeatherMapError(HTTPException):
    """Exception raised when app could not connect to OpenWeatherMap services."""
    def __init__(self, message="Cannot connect to OpenWeatherMap"):
        self.message = message
        super().__init__(500, self.message)
