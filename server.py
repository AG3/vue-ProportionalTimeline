import web
import json

urls = (
    '/', 'index',
    '/events', 'events'
)


class index:
    def GET(self):
        render =web.template.render('../VueProject/SclaedTimeline/dist')
        return render.index()


class events:
    def __init__(self):
        self.data = {'time': 1, 'title': 'hello', 'content': 'xixixi'}

    def GET(self):
        return json.dumps(self.data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
