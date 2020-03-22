import json
from binance_f.impl.utils.jsonwrapper import JsonWrapper


def parse_json_from_string(value, status_code):
    value = value.replace("False", "false")
    value = value.replace("True", "true")
    value = json.loads(value)
    value['status_code'] = status_code
    return JsonWrapper(value)
