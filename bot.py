from mastodon import Mastodon
import random
import json
import os


class Settings:
    config_location = 'config.json'

    def __init__(self):
        if os.path.exists(self.config_location):
            if json.load(open(self.config_location)) == {"id": "id","secret": "secret","token": "token","url": "url"}:
                print('You have to modify the config 1st.')
                exit()
            self.__dict__ = json.load(open(self.config_location))

        else:
            print('config.json file needed to operate.')
            exit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        json.dump(self.__dict__, open(self.config_location, 'w'))


if __name__ == "__main__":
    dog = 1
    while dog == True:
        response = input("Would you like to start?\nyes/no\n")
        if response  == "yes" or response  == "y":
            with Settings() as settings:
                mastodon = Mastodon(
                    client_id=settings.id,
                    client_secret=settings.secret,
                    access_token=settings.token,
                    api_base_url=settings.url
                )
                dog = 0
        elif response == "no" or response == "n":
            print("Ok.")
            exit()
        else:
            print("Type yes or no.")

