import uuid

class UUIDVO:
    @staticmethod
    def generate():
        return str(uuid.uuid4())
