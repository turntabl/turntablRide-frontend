import urllib.parse


class Credentials:
    def refresh(self):
        pass

    def populate_attributes(self):
        pass


body = {"grant_type": "refresh_token", "refresh_token": "ieueiejfr873943889958"}

new = urllib.parse.urlencode(body).encode("utf-8")

print(new)
