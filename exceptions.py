class DatabaseAppError(Exception):
    """Custom exception for display human error messages"""

    def __init__(self, msg=None):
        super().__init__()
        self.msg = msg or (
            'Something went wrong please try again or contact administrator'
        )
