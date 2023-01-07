import datetime
import jwt


secret = """-----BEGIN PRIVATE KEY-----
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123
-----END PRIVATE KEY-----"""
keyId = "0123456789"
teamId = "1234567890"
alg = 'ES256'

time_now = datetime.datetime.now()
time_expired = datetime.datetime.now() + datetime.timedelta(hours=12)

headers = {
	"alg": alg,
	"kid": keyId
}

payload = {
	"iss": teamId,
	"iat": int(time_now.timestamp()),
	"exp": int(time_expired.timestamp())
}


if __name__ == "__main__":
	"""Create an auth token"""
	token = jwt.encode(payload, secret, algorithm=alg, headers=headers)

	print("----TOKEN----")
	print(token)

	print("----CURL----")
	print("curl -v -H \"Authorization: Bearer %s\" \"https://api.music.apple.com/v1/catalog/us/artists/36954\" " % (token))

