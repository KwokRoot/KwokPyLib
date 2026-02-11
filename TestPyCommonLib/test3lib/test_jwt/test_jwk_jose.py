# pip install python-jose[cryptography]
from jose import jwt
from jose.exceptions import JWTError

jwks = {
    "keys":
        [
            {
                "kty": "RSA",
                "e": "AQAB",
                "kid": "4e5fe8e2-621d-4e05-9ae1-19003e7f32a7",
                "n": "rB1RrVXHNzv2ezUpi2h8WtXjLUhZu4X8xRS1NYgCqKa03TqQtA6q2g0oofesFi4u6AiAWD-NkHsrB3_2X08T9IoA9dIYd10XO1sdJervL1Hj1yrX78x91xv5TTfxU8EHmEd2bSjdbMwrPhEbKwHb2lD7bdPRmD_12cH7uORLPaGjcGJIjMfJ9LzxaUJkpypRf4gjr2R9BBC7E5giYqaZgHZZhkwYkJHIlSRCJPtyEt_sezF0WJKUAt7yF5eDo8Ox7OZQI__wYRAHq2q-cVuw4vS1CQd_PEL523SvOA1Fn0CXrwvE4UhdHVvS1ovoySbcSGpbOX91BRBEDKwBZuW4sw"
            }
        ]
}

token = "eyJraWQiOiI0ZTVmZThlMi02MjFkLTRlMDUtOWFlMS0xOTAwM2U3ZjMyYTciLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImF1ZCI6ImRlbW8tY2xpZW50IiwiYXpwIjoiZGVtby1jbGllbnQiLCJhdXRoX3RpbWUiOjE3NzA2MTQ0MjcsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTAwMCIsImV4cCI6MTc3MDYxNzY4OSwiaWF0IjoxNzcwNjE1ODg5LCJqdGkiOiI1NDA1ZGYzMy03YTBjLTRmY2YtYmM5OS04ODk0YjA3MTE4NzgiLCJzaWQiOiJDR0c4M0RUdWZVSmxsRG04TnNuX2pqWVhJRWl1VDFvQktJOHdUdnRZNHNNIn0.K0S9X3bn0JsS4MkqcsPVIeEOZ7IFzh01Y_rDjzCiyI2zVJ6s0QS-NYIa8EoHPH3dZTRHqEPDoxszM3x8OXlCPXfTn5Xgi2_ODiZEAz3dcKstemmwEmHspon805snAsOBwkBE6EAsOnTT3sJMegUlIborNFg6xQi9NzsT0CjHFvToYwnyy-h8CIU8kMF4MNE0_Xo-ohU8Q_FlC9106cIlBOCtzhlf4uIIDEZrxg77Y2O_0kgRpy8kfAlsobITaIc4z467DZvyugt9D3TbthLbHgr-Vb9BlBTDxr-qcjFoRqykoFerKF0P4uGaVlw_sHP7rMiKms6JYy2JVncf6Kuo9A"

try:
    decoded = jwt.decode(
        token,
        jwks,
        algorithms=['RS256'],
        audience="demo-client",
        issuer="http://localhost:9000"
    )
    print("Token is valid:", decoded)
except JWTError as e:
    print("Invalid token:", e)

