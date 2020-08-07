import os
from pprint import pprint
import json
import subprocess
from datetime import datetime
from src.main.manifest import Manifest


class Builder(Manifest):

    def __init__(self, location='.'):
        self.cmd = ['docker', 'buildx', 'build']
        self.builder_release = self.get_builder_version()
        self.location = os.path.join(location)

    def get_builder_version(self):
        with open('version.txt', 'r') as version_file:
            release = float(version_file.read())
        return release

    def get_files(self):
        projects = []
        for path in os.listdir(self.location):
            tmp_ = os.path.join(self.location, path)
            if os.path.isdir(tmp_):
                if os.path.isfile(os.path.join(tmp_, 'manifest.yml')):
                    projects.append(path)
        return projects

    def load_projects(self, projects):
        locate = lambda p: os.path.join(os.path.join(self.location, p), 'manifest.yml')
        load = lambda p: self.load_file(locate(p))
        return [(p, load(p)) for p in projects]

    def upload_status(self, json_status):
        with open('status.json', 'w') as outfile:
            json.dump(json_status, outfile)

    def update_status(self, pool):
        json_status = {}
        for _, item in pool:
            item['release'] = self.builder_release
            item['datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            name = item.pop('name')
            json_status[name] = item
        return json_status

    def build(self):
        projects = self.get_files()
        pool = self.load_projects(projects)
        for name, scheme in pool:
            path = os.path.join(name, scheme.pop('path'))
            path = os.path.join('examples', path)
            path = [os.path.abspath(path)]
            try:
                print(f'Building {path}')
                pprint(scheme)
                subprocess.check_call(self.cmd + path)
                status = True
                message = ""
            except Exception as e:
                status = False
                message = e
            scheme['status']= status
            scheme['message'] = message

        updated_status = self.update_status(pool)
        self.upload_status(updated_status)
