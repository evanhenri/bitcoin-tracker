# Bitcoin Tracker
App that retrieves bitcoin balances and transaction history for user specified addresses.

## Running Locally
```bash
$ docker-compose up --build
$ sudo bash -c "echo -e '127.0.0.1\tbitcoin-tracker.com' >> /etc/hosts"
```

The app can now be accessed in your browser at bitcoin-tracker.com

## Architecture
* Django - backend + frontend
* Django rest framework - backend API
* Postgres - persistent data store
* Redis - API response cache
* Celery - runs a background job every minute to refresh the cache

## Future Work
* Add pagination for transactions page
* Add button to frontend that allows users to manually refresh balance and transaction information
* Re-write frontend so it only interacts with backend via API requests
    * Could scale out the number of backend containers that service the client side frontend
* Modify containers so they are more suited to a cluster environment
