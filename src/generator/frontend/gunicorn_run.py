import multiprocessing
import os

from gunicorn.app.base import BaseApplication

class GunicornApplication(BaseApplication):

    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    # Assuming `proj.wsgi:application` is the path to your WSGI application
    from skkuppt.wsgi import application

    # Define any configuration options for Gunicorn here
    FRONTEND_PORT=os.environ.get("FRONTEND_PORT", "8080")
    options = {
        'bind': f'0.0.0.0:{FRONTEND_PORT}',
        'workers': multiprocessing.cpu_count() * 2,
    }

    GunicornApplication(application, options).run()
