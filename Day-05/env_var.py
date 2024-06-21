#always import os when using env variables and only use env variable to store sensitive infomration like passwords, tokens, API keys, Certs
import os

#get env var list by running CLI command: env
#define env var by running CLI command: export PASSWORD="laxmankiran"

password = os.getenv("PASSWORD")        # we use os.getenv() to get the value of the env variable that's already defined
print("Password is: " , password)

github_token = os.getenv("GITHUB_TOKEN")
print("Github Token is:", github_token)
