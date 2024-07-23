# Create your connection to the DB in this file #
# Ensure that 'db' is a variable that can be accessed #
import pg8000.native
from pg8000.native import Connection

database = 'theme_parks'
user = 'sam'
# password = YOUR_PASSWORD_HERE

db = Connection(
    database=database,
    user=user
    # password=password
)

