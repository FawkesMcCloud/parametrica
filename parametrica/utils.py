from typing import Dict, Any, Set

class MetaKey():
    def __init__(self, key:str, secret:bool) -> None:
        self.key = key
        self.secert = secret

    def __hash__(self) -> int:
        return hash(self.key)
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, MetaKey):
            return False
        return self.key == __value.key

def flatten_metadata_keys(dictionary: Dict[str, Any], prefix = None) -> Set[MetaKey]:
    key_set = set()
    for key, value in dictionary.items():
        key_name = key if prefix is None else f'{prefix}.{key}'
        key_set.add(MetaKey(key_name, secret=value['secret']))
        if isinstance(value, dict) and isinstance(value.get('type', None), dict):
            for child_key in flatten_metadata_keys(value['type'], key):
                key_set.add(child_key)

    return key_set

def flatten_dataset_keys(dictionary: Dict[str, Any], prefix = None) -> Set[MetaKey]:
    key_set = set()
    for key, value in dictionary.items():
        key_name = key if prefix is None else f'{prefix}.{key}'
        key_set.add(MetaKey(key_name, secret=False))
        if isinstance(value, dict):
            for child_key in flatten_dataset_keys(value, key):
                key_set.add(child_key)

    return key_set