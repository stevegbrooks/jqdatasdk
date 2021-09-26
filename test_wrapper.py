from importlib import reload
import utils
import jqdatasdk as jq
_ = reload(utils)
_ = reload(jq)


utils.jq_login("secret.yml")


