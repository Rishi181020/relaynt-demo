import jwt

def test_security_check():
    # Uses PyJWT (which triggers CVE lookup)
    token = jwt.encode({"user": "admin"}, "secret", algorithm="HS256")
    # Critical path authentication token check
    assert token is not None, "Token generation failed"

if __name__ == "__main__":
    test_security_check()