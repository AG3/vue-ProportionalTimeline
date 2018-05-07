import web
import json
import atexit

urls = (
    '/', 'index',
    '/events', 'events'
)


class dataManager:
    file_path = './data.json'
    database = []
    def readFile(self):
        f = open(self.file_path, 'r')
        data = json.load(f)
        return data

    def writeFile(self):
        f = open(self.file_path, 'w')
        f.write(json.dumps(self.database))

    def addData(self, e):
        self.database.append(e)


DB = dataManager()

class index:
    def GET(self):
        render = web.template.render('../VueProject/SclaedTimeline/dist')
        return render.index()


class events:
    def GET(self):
        return json.dumps(DB.database)

    def POST(self):
        data = web.data()
        DB.addData(json.loads(data.decode("utf-8")))
        return 'OKAY'


if __name__ == "__main__":
    atexit.register(DB.writeFile)
    app = web.application(urls, globals())
    app.run()
