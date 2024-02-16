from typing import Dict, Any, Set

def flatten_metadata_keys(dictionary: Dict[str, Any], exclude_secret: bool = True ,prefix = None) -> Set[str]:
    key_set = set()
    for key, value in dictionary.items():
        if (value['secret'] == True) and exclude_secret:
            continue
        key_set.add(key if prefix is None else f'{prefix}.{key}')
        if isinstance(value, dict) and isinstance(value.get('type', None), dict):
            for child_key in flatten_metadata_keys(value['type'], exclude_secret, key):
                key_set.add(child_key)

    return key_set

def flatten_dataset_keys(dictionary: Dict[str, Any], prefix = None) -> Set[str]:
    key_set = set()
    for key, value in dictionary.items():
        key_set.add(key if prefix is None else f'{prefix}.{key}')
        if isinstance(value, dict):
            for child_key in flatten_dataset_keys(value, key):
                key_set.add(child_key)

    return key_set