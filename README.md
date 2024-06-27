# sixs_json
The 6S code but with JSON output for easier parsing.

# Packaging reminder
Build the package with the following command:

```bash
python -m build
```

Check it's content in the archive and then upload it to PyPi with the following command:

```bash
twine upload -r pypi dist/*
```