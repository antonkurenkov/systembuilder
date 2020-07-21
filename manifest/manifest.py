import yaml
import os


class Manifest:

    @staticmethod
    def check_existent(path):
        return os.path.exists(path)

    def load_file(self, path):
        if self.check_existent(path):
            with open(path) as f:
                return yaml.safe_load(f)
        else:
            return None