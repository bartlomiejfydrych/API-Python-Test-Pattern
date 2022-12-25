def payload_cutter(payload):

    # W celu uniknięcia errora 'DictionaryHasChanged' tworzę kopię payloadu
    payload_copy = payload.copy()

    for payload_key in list(payload_copy):
        if payload_copy[payload_key] is None:
            del payload[payload_key]
        if type(payload_copy[payload_key]) is dict:
            payload_cutter(payload[payload_key])
    return payload


"""
Różnice pomiędzy list(dict), a dict.keys()
Źródło:
https://stackoverflow.com/questions/31837161/difference-between-listdict-and-dict-keys

Inne rozwiązania ze StackOverflow:
Źródło:
https://stackoverflow.com/questions/3405715/elegant-way-to-remove-fields-from-nested-dictionaries

# ------------------------------------------------
# PIERWSZE:
# Wersja, która modyfikuje payload w miejscu
# ------------------------------------------------
from collections import MutableMapping
from contextlib import suppress

def delete_keys_from_dict(dictionary, keys):
    for key in keys:
        with suppress(KeyError):
            del dictionary[key]
    for value in dictionary.values():
        if isinstance(value, MutableMapping):
            delete_keys_from_dict(value, keys)


# ------------------------------------------------
# DRUGIE:
# Wersja, która zwraca nowy obiekt
# ------------------------------------------------
from collections import MutableMapping

def delete_keys_from_dict(dictionary, keys):
    keys_set = set(keys)  # Just an optimization for the "if key in keys" lookup.

    modified_dict = {}
    for key, value in dictionary.items():
        if key not in keys_set:
            if isinstance(value, MutableMapping):
                modified_dict[key] = delete_keys_from_dict(value, keys_set)
            else:
                modified_dict[key] = value  # or copy.deepcopy(value) if a copy is desired for non-dicts.
    return modified_dict
"""