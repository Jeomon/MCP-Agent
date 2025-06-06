# Standard JSON-RPC 2.0 error codes
PARSE_ERROR = -32700
INVALID_REQUEST = -32600
METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603

# Server error codes (reserved from -32000 to -32099)
SERVER_ERROR_START = -32000
SERVER_ERROR_END = -32099

# Error code descriptions
ERROR_MESSAGES = {
    PARSE_ERROR: "Parse error: Invalid JSON was received by the server.",
    INVALID_REQUEST: "Invalid Request: The JSON sent is not a valid Request object.",
    METHOD_NOT_FOUND: "Method not found: The method does not exist / is not available.",
    INVALID_PARAMS: "Invalid params: Invalid method parameter(s).",
    INTERNAL_ERROR: "Internal error: Internal JSON-RPC error.",
    SERVER_ERROR_START: "Server error: Something went wrong on the server.",
}

def get_error_message(code):
    """Get the description for an error code."""
    return ERROR_MESSAGES.get(code, f"Unknown error: Code {code}")