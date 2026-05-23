import sys

try:
    import jwt
except ImportError:
    print("Installing PyJWT...", file=sys.stderr)
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyJWT"])
    import jwt


def test_security_check():
    # Uses PyJWT (which triggers CVE lookup)
    token = jwt.encode({"user": "admin"}, "secret", algorithm="HS256")
    # Verify token was created successfully
    decoded = jwt.decode(token, "secret", algorithms=["HS256"])
    assert decoded["user"] == "admin", "Verification token check failed"


if __name__ == "__main__":
    test_security_check()