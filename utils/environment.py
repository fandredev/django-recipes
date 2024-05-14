import os


def get_env_variable(variable_name: str = "", default_value: str = ""):
    return os.environ.get(variable_name, default_value)


def parse_comma_separate_str_to_list(comma_str: str = ""):
    if not comma_str or not isinstance(comma_str, str):
        return []
    return [string.strip() for string in comma_str.split(",") if string]
