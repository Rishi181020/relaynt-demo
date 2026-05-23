import json

def test_broken_auth_flow():
    # Intentionally invalid JSON string using single quotes instead of double quotes.
    # This will raise: json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
    bad_json_string = "{'status': 'authenticated', 'token_valid': true}"
    config = json.loads(bad_json_string)
    assert config["status"] == "authenticated"

if __name__ == "__main__":
    test_broken_auth_flow()
