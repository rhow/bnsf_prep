
from typing import TypedDict


class LogRecord(TypedDict):
    id: int
    type: str
    timestamp: str

    # def __init__(self, **)

class Record(object):
    _error: bool = False
    _msg: str
    _int: int
    _type: str
    _timestamp: str

    def __init__(self, **kwargs):
        try:
            self._id = int(kwargs['id'])
            self._type = kwargs['type']
            self._timestamp = kwargs['timestamp']

        except Exception as e:
            self._error = True
            self._msg = f'Error with {e}'
        
    @property
    def error(self):
        return self._error
    
    @property
    def msg(self):
        return self._msg
        

def validate_records(records: dict) -> bool:
    valid = True
    for r_kw in records:
        record = Record(**r_kw)

        if valid and record.error:
            valid = False

    return valid

def validate_log_records(records: dict) -> bool:
    valid = True

    for r in records:
        try:
            record: LogRecord = {
                'id': int(r['id']),
                'type': r['type'],
                'timestamp': r['timestamp']
            }

        except KeyError as e:
            valid = False
        except ValueError as e:
            valid = False

    return valid

records_input = [
    {"id": 1, "type": "LOGIN", "timestamp": "2024-11-01T12:00"},
    {"id": 2, "type": "LOGOUT", "timestamp": "2024-11-01T12:30"},
]

result = validate_log_records(records=records_input)
print(result)
