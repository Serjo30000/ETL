from flask import Flask

from ServerDataMongo.service.dbSyncService import DbSyncService

app = Flask(__name__)

db_sync_service = DbSyncService()

def run_script():
    print("Start mongo")
    db_sync_service.carSyncOnDb()
    print("Cars updates")
    db_sync_service.parkingSyncOnDb()
    print("Parkings updates")

if __name__ == '__main__':
    print("Hello world!")
    run_script()
    # app.run(debug=True)
