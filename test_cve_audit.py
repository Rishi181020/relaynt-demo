import jwt
def test_security_check():
    # Uses PyJWT (which triggers CVE lookup)
    token = jwt.encode({"user": "admin"}, "secret", algorithm="HS256")
    # Basic failure to trigger the agent code-fix
    assert False, "Verification token check failed"
if __name__ == "__main__":
    test_security_check()
