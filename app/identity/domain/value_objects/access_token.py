class AccessToken:

    def __init__(self, value: str):
        if not value:
            raise ValueError("Token cannot be empty")
        
        self.value = value
    
    def __str__(self, value: str):
        return self.value