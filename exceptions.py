from fastapi import HTTPException

class NoCityFoundError(HTTPException):
    """Exception raised when no city is found in geocode the response."""
    def __init__(self, message="No city found with the given name."):
        self.message = message
        super().__init__(404, self.message)
