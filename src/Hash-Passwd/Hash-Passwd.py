#!/usr/bin/env python3
import bcrypt
a = input('')
print(str(bcrypt.hashpw(a.encode(), bcrypt.gensalt()).decode()))
