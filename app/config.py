from environs import Env

env = Env()
env.read_env()

LMTP_SERVER = env("LMTP_SERVER")
LMTP_PORT = env.int("LMTP_PORT")
TO_EMAILS = env.list("EMAILS")
# TO_EMAILS = ["toanbs@ghtklab.com"]  # must be a list
THREADS = env.int("THREADS")

