# JSON in Python

This repository contains small examples demonstrating how to work with JSON in Python:

- `json_and_pythonObj.py`: How to serialize (encode) Python built-in types to JSON and deserialize (decode) JSON into Python built-ins using `json.dumps`, `json.dump`, `json.loads`, and `json.load`.
- `json_and_customObj.py`: How to serialize custom Python objects by providing a `default` function or by subclassing `json.JSONEncoder`, and how to decode JSON back into custom objects using `object_hook`.
- `example_json_format.json`: A sample JSON file showing a nested object with arrays and booleans.
- `person.json`: A sample JSON file used by `json_and_pythonObj.py`.

## Concepts

1. __Serialization (Encoding)__

    - Converting Python objects to JSON format.
    - Use `json.dumps(obj)` to get a JSON string.
    - Use `json.dump(obj, file)` to write JSON directly to a file.
    - Both functions accept formatting parameters like `indent=4` for pretty printing.

2. __Deserialization (Decoding)__

    - Converting JSON strings/files back into Python objects.
    - Use `json.loads(json_string)` to parse a JSON string into Python built-ins (usually `dict`, `list`, `str`, `int`, `float`, `bool`, `None`).
    - Use `json.load(file)` to parse JSON from a file.

3. __Built-in types vs custom objects__

    - The `json` module can serialize built in Python types directly (dicts, lists, strings, numbers, booleans, None).
    - Custom classes (instances of user-defined classes) are not serializable by default. Attempting to `json.dumps()` them raises a `TypeError`.

4. __Making custom objects serializable__

    - Option A: Provide a `default` callable to `json.dumps` that returns a JSON serializable representation (eg. a dict).

    - Option B: Subclass `json.JSONEncoder` and override `default(self, obj)` to return a serializable representation.

5. __Decoding custom objects__

    - `json.loads(..., object_hook=...)` accepts a callable that transforms dicts into custom objects. If the `object_hook` returns an instance, that instance will replace the dict.

6. __Pitfall: shadowing the standard library__

    - One thing I ran into while writing these examples: if you name a script after a standard library module (for example `json.py`, `os.py`, `sys.py`, `requests.py`), Python will import your local file first and shadow the real module. That can lead to confusing errors like `AttributeError: module 'json' has no attribute 'dumps'`, `RecursionError`, or other import failures, I hit this while developing the examples, so watch out for it.

- How to fix
    - Don’t name your script `json.py` (or any other stdlib/module name). Use something like `json_example.py` instead.
    - Remove cached bytecode: delete the `__pycache__` folder and any `*.pyc` files.
    - Restart your Python interpreter or editor/IDE so the old module is not still loaded.
    - Check the current working directory for accidentally named files, Python resolves imports from there first.

## Files and How to Run

Open a terminal (PowerShell on Windows) in the repository root (`c:\JSON_in_python`).

Run examples:

```powershell
python .\json_and_pythonObj.py
python .\json_and_customObj.py
```

Expected behavior:

- `json_and_pythonObj.py` prints a pretty JSON string for `person` and writes/reads `person.json`.
- `json_and_customObj.py` prints the JSON representation of a `Person` instance and shows decoding back into a `Person` object using `object_hook`.


## License

This is my example code for learning purposes. Use freely.
