# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
#     "http://localhost:5000",
#     "http://127.0.0.1:5000",
# ]
from utils.environment import get_env_variable, parse_comma_separate_str_to_list


CORS_ALLOWED_ORIGINS = parse_comma_separate_str_to_list(
    get_env_variable("CSRF_TRUSTED_ORIGINS")
)
