import alchemy

alchemy.create_air()
try:
    alchemy.create_earth()
except Exception as e:
    print(e)
