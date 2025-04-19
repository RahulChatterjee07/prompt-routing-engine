import yaml

def load_prompt_template(path):
    """
    Load a YAML file and return its content as a string.
    """
    with open(path, "r") as f:
        return f.read()
