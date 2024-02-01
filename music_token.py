import datetime
import jwt
import os


secret = os.environ['PRIVKEY']
keyId = os.environ['KEYID']
teamId = os.environ['TEAMID']
alg = 'ES256'

time_now = datetime.datetime.now()
time_expired = datetime.datetime.now() + datetime.timedelta(days=180)

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
	print("curl -v -H \'Authorization: Bearer %s\' \"https://api.music.apple.com/v1/catalog/us/artists/36954\" " % (token))

