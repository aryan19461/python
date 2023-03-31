# a to z --> small case
# 0 to 9 digit required
# . and _ can be used once only
# @ can be used only once

import re
email_conndition = "^[a-z] + [A-Z] + [0-9] + [\._]? [a-z 0-9 ] +[@]\w + [.]\w" # ^ means start of string and \w means irt will search that specific [] in the enitire string
user_Email = input("Enter your email: \n")


if re.search(email_conndition, user_Email):
    print("Valid Email")
else:
    print("Invalid Email")