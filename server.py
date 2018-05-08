import web
import json
import atexit

urls = (
    '/', 'index',
    '/events', 'events',
    '/save', 'saver'
)


class dataManager:
    file_path = './data.json'
    database = []

    def __init__(self):
        self.database = self.readFile()

    def readFile(self):
        f = open(self.file_path, 'r')
        data = json.load(f)
        f.close()
        return data

    def writeFile(self):
        print("Saving to file")
        print(self.database)
        print(self.file_path)
        f = open(self.file_path, 'w')
        f.write(json.dumps(self.database))
        f.close()


    def addData(self, e):
        print("Saving event to db")
        print(e)
        self.database.append(e)
        print(self.database)
        # self.GET()


DB = dataManager()


class saver:
    def GET(self):
        DB.writeFile()
        return "SAVED"


class index:
    def GET(self):
        render = web.template.render('./')
        return render.index()


class events:
    def GET(self):
        print("Getting events")
        return json.dumps(DB.database)

    def POST(self):
        print("Uploading event")
        data = web.data()
        print("Event:" + data.decode("utf-8"))
        DB.addData(json.loads(data.decode("utf-8")))
        return 'OKAY'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
