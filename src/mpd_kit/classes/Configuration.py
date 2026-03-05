from mpd_kit.classes.exceptions.SecondNonRecurringValue import SecondNonRecurringValue
from mpd_kit.classes.exceptions.UnknownValue import UnknownValue
from mpd_kit.classes.exceptions.SkippedRequiredValue import SkippedRequiredValue
from mpd_kit.classes.ValueSignature import ValueSignature

ARG_KEY = 0
ARG_VALUE = 1

class Configuration:
    # values = []

    value_signatures = [
        ValueSignature('DNAME', 'Display Name', False, True),
        ValueSignature('VERSION', 'Version', False, True),
        ValueSignature('BRIEF', 'Description', False, True),
        ValueSignature('ENTRY', 'Entry File', True, True),
        ValueSignature('BASEFLAGS', 'Base Compiler Flags', False, False),
    ]

    def __init__(self):
        self.values = []

    def getValueSignature(self, key: str):
        for item in self.value_signatures:
            if item.key == key:
                return item

        return None

    def getValue(self, key: str):
        for value in self.values:
            if value[ARG_KEY] == key:
                return value[ARG_VALUE]

        return None

    def getRecurringValues(self, key):
        result = []

        for item in self.values:
            if item[ARG_KEY] == key:
                result.append(item[ARG_VALUE])

        return result

    def setValue(self, key: str, value: str):
        signature = self.getValueSignature(key)

        if not signature:
            raise UnknownValue(key)

        if not signature.recurring:
            current_value = self.getValue(key)
            if current_value:
                raise SecondNonRecurringValue(f'{key} is now {current_value}, tried {value}')

        self.values.append([key, value])

    def validateRequired(self):
        for signature in self.value_signatures:
            if signature.required and not self.getValue(signature.key):
                raise SkippedRequiredValue(signature.key)
