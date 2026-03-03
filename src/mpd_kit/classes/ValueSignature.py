class ValueSignature:
    key = None
    pretty_name = None
    recurring = None
    required = False

    def __init__(self, key: str, pretty_name: str, recurring: bool, required: bool):
        self.key = key
        self.pretty_name = pretty_name
        self.recurring = recurring
        self.required = required
