import cherrypy
import cherrypy_cors
import os
import json
from system import System

class Api:
        def __init__(self):
                cherrypy.response.headers['Content-Type'] = 'application/json'
                self.system = System()
                cherrypy_cors.install()

        @cherrypy.expose
        @cherrypy.tools.json_out()
        def index(self, text):
                return self.system.generate_span_to_n_days(50)
        #         return '''
        #     <html>
        #     <body>top</body>
        # '''

        # @cherrypy.expose
        # @cherrypy.tools.json_out()
        # def get(self,code=None,name=None,parsed_name=None,bbn=None):
        #         result = self.service.get(code,name,parsed_name,bbn)
        #         return result

configs = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')
if __name__ == '__main__':
        #breakpoint()
        configs = {
            '/': {
                'cors.expose.on': True,
            },
        }
        cherrypy.quickstart(Api(), config=configs)

Api()