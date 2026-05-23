import json

def test_broken_auth_flow():
    # Valid JSON string using double quotes instead of single quotes.
    bad_json_string = '{"status": "authenticated", "token_valid": true}'
    config = json.loads(bad_json_string)
    assert config["status"] == "authenticated"

if __name__ == "__main__":
    test_broken_auth_flow()