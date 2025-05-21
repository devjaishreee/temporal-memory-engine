from datetime import datetime

def get_current_timestamp():
    """Returns the current UTC timestamp as an ISO 8601 string."""
    return datetime.utcnow().isoformat() + "Z"
