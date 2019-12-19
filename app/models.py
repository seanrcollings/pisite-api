from app import db
import subprocess


#pylint: disable=no-member
class Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    command = db.Column(db.String(128))
    description = db.Column(db.Text())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "command": self.command,
            "description": self.description
        }

    def execute_command(self):
        try:
            data = subprocess.check_output(self.command,
                                           shell=True).strip().decode('utf-8')
        except:
            data = "Data Fetch Failed :("
        return data
