# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import os, sys
import json
from typing import Callable, Union

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'JsonAdvanced' + os.sep + 'libs' + os.sep


if cur_path not in sys.path:
    sys.path.append(cur_path)

module = GetParams("module")

def validate_json(string: str) -> Union[dict|list|str]:
    """
    Validates and parses a JSON string.

    Args:
        string (str): The JSON string to be validated and parsed.

    Returns:
        Union[dict, list, str]: The parsed JSON data.

    Raises:
        json.JSONDecodeError: If the string is not valid JSON.
    """
    try:
        return json.loads(string)
    except json.JSONDecodeError as e:
        PrintException()
        raise e
    
def open_json(path: str) -> Union[dict|list]:
    """
    Opens and reads a JSON file from the specified path.

    Args:
        path (str): The file path of the JSON file to be opened.

    Returns:
        Union[dict, list]: The parsed JSON data.

    Raises:
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        PrintException()
        raise e
    
def create_json(path: str, data: Union[dict, list]) -> bool:
    """
    Creates a JSON file at the specified path with the given data.

    Args:
        path (str): The file path where the JSON file will be created.
        data (Union[dict, list]): The data to be written to the JSON file.

    Returns:
        bool: True if the file was created successfully, False otherwise.

    Raises:
        OSError: If there is an issue with file operations.
        TypeError: If the data is not serializable to JSON.
    """
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except (OSError, TypeError) as e:
        PrintException()
        raise e

def traverse_path(data, keys, is_add=False) -> Union[dict, list, bool]:
    """
    Traverses the JSON data to the specified path.

    Args:
        data (Union[dict, list]): The JSON data.
        keys (list): The path to traverse, split into keys.
        is_add (bool): If True, create the path if it does not exist.

    Returns:
        Union[dict, list, bool]: The traversed JSON data or False if the path does not exist and is_add is False.
    """
    current = data
    for key_path in keys:
        if key_path.isdigit():
            key_path = int(key_path)
            if not isinstance(current, list) or key_path >= len(current):
                if is_add:
                    raise ValueError("Invalid path: list index out of range")
                return False
        if key_path not in current:
            if is_add:
                current[key_path] = {}
            else:
                return False
        current = current[key_path]
    return current

def add_key_value_to_json(
        path: str,
        key: str,
        value: str,
        path_json: str,
        new_json: str,
        open_json: Callable[[str], Union[dict, list]],
        validate_json: Callable[[str], Union[dict, list, str]],
        create_json: Callable[[str, Union[dict, list]], bool],
        traverse_path_add: Callable[[Union[dict, list], list], Union[dict, list]]
) -> bool:
    """
    Adds a key-value pair to a JSON file at the specified path.

    Args:
        path (str): The file path of the JSON file to be modified.
        key (str): The key to be added.
        value (str): The value to be added.
        path_json (str): The path within the JSON where the key-value pair should be added.
        new_json (str): The file path where the modified JSON will be saved.
        open_json (Callable[[str], Union[dict, list]]): Function to open and read the JSON file.
        validate_json (Callable[[str], Union[dict, list, str]]): Function to validate the JSON value.
        create_json (Callable[[str, Union[dict, list]], bool]): Function to create and save the JSON file.

    Returns:
        bool: True if the key-value pair was added successfully, False otherwise.
    """

    data = open_json(path)
    value = validate_json(value)
    keys = path_json.split('/')

    current = traverse_path_add(data, keys[:-1], is_add=True)
    if current is False:
        raise ValueError("Invalid path: path does not exist in the JSON")

    last_key = keys[-1]

    if not key.isalnum():
        raise ValueError("The key must be alphanumeric")
        
    if last_key.isdigit():
        last_key = int(last_key)
        if not isinstance(current, list) or last_key >= len(current):
            raise ValueError("Invalid path: list index out of range")
        if isinstance(current[last_key], list):
            current[last_key].append({key: value})
        elif isinstance(current[last_key], dict):
            current[last_key][key] = value
        else:
            current[last_key] = [{key: value}]
    else:
        if last_key in current:
            if isinstance(current[last_key], list):
                current[last_key].append({key: value})
            elif isinstance(current[last_key], dict):
                current[last_key][key] = value
            else:
                current[last_key] = [{key: value}]
        else:
            current[last_key] = {key: value}
    
    return create_json(new_json, data)

def delete_key_value_from_json(
        path: str,
        key: str,
        path_json: str,
        new_json: str,
        open_json : Callable[[str], Union[dict|list]],
        traverse_path: Callable[[Union[dict, list], list], Union[dict, list]]
) -> bool:
    """
    Deletes a key-value pair from a JSON file at the specified path.

    Args:
        path (str): The file path of the JSON file to be modified.
        key (str): The key to be deleted.
        path_json (str): The path within the JSON where the key-value pair should be deleted.
        new_json (str): The file path where the modified JSON will be saved.
        open_json (Callable[[str], Union[dict, list]]): Function to open and read the JSON file.
        traverse_path (Callable[[Union[dict, list], list], Union[dict, list, bool]]): Function to traverse the JSON structure.

    Returns:
        bool: True if the key-value pair was deleted successfully, False otherwise.
    """
    data = open_json(path)
    keys = path_json.split('/') if path_json else []

    current = traverse_path(data, keys[:-1])

    if current is False:
        return False

    if keys:
        last_key = keys[-1]
        if last_key.isdigit():
            last_key = int(last_key)
            if not isinstance(current, list) or last_key >= len(current):
                return False  # The path does not exist in the JSON
            del current[last_key]
        elif last_key in current:
            del current[last_key]
        else:
            return False  # The key does not exist in the JSON
    else:
        # No path provided; assume key is at the top level
        if key in current:
            del current[key]
        else:
            return False  # The key does not exist at the top level
    
    with open(new_json, 'w') as file:
        json.dump(data, file, indent=4)
    
    return True

try:

    if module == "add_to_json":

        path = GetParams("path")
        path_json = GetParams("path_json")
        result = GetParams("result")
        key = GetParams("key")
        value = GetParams("value")
        new_json = GetParams("new_path_json")

        try:
            SetVar(result, False)
            if add_key_value_to_json(path, key, value, path_json, new_json, open_json, validate_json, create_json, traverse_path):
                SetVar(result, True)
        except Exception as e:
            PrintException()
            raise e
        
    if module == "delete_from_json":
        
        path = GetParams("path")
        key = GetParams("key")
        path_json = GetParams("path_json")
        result = GetParams("result")
        new_json = GetParams("new_path_json")

        try:
            SetVar(result, False)
            if delete_key_value_from_json(path, key, path_json, new_json, open_json, traverse_path):
                SetVar(result, True)
            else:
                raise KeyError("The key does not exist in the json")
        except Exception as e:
            PrintException()
            raise e

    if module == "create_json":
        
        data = GetParams("json")
        result = GetParams("result")
        path = GetParams("new_path_json")

        try:
            SetVar(result, False)
            data = validate_json(data)
            create_json(path, data)
            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e

       
except Exception as e:
    PrintException()
    raise e