class Password:
    MIN_LENGTH = 6
    
    def __init__(self, value: str):
        self._validate(value)
        self.value = value

    def _validate(self, value: str):
        if len(value) < self.MIN_LENGTH:
            raise ValueError("Password too short")
    
    def __str__(self):
        return self.value