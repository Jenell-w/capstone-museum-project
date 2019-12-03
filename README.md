# capstone-museum-project

**About:** My app allows families to share activities they have completed (or attempted!) when bringing their children to museums, specifically art museums. Many people think that art museums are not child friendly but I would like to change that perception and help families explore world famous art in a way that children can relate to.

---

**Installation:** Use pipenv, npm.  
Must have the following installed to run:
Python3
-Dependencies: pandas, sqlalchemy, psycopg2-binary,
Node.js
Vue.js
Flask
Postgres

---

**To run locally:**

In one terminal tab:

`cd client`

`npm install`

`npm run build`

## use web address given in the python tab (below)

In a new tab:

`cd server`

`pipenv install`

`pipenv run python main.py`

---

**Environment Vars**
Create a .env file with the following:

`DB_USER= DB_PASS= DB_URL= DB_NAME= RUN_ENVIRONMENT=`

Note: if RUN_ENVIRONMENT == 'network', the app will connect to postgres according the the env variables above. Otherwise it will coneect to a local sqlite3 file

**when db is created, it will be seeded with museum name/ city data from a short csv file.**

Features: My app can write to a database, read from that database, delete as well. I also call an external API to do a preparation activity, which involves the display of a random piece of artwork from the Harvard University Museum collection.
