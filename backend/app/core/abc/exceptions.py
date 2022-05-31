class ValidationError(Exception):
    def __init__(self, msg=None, *args):
        super(ValidationError, self).__init__(msg or "Validation error", *args)
