import csv
import os


class Data:
    def __init__(self):
        self.fields = ["id", "value", "time"]
        self.path = None
        self.init_file()


    def init_file(self):
        self.path = os.path.abspath(os.path.curdir + "/database")
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.path = os.path.abspath(self.path + "/database.csv")
        if not os.path.exists(self.path):
            with open(self.path, 'w')as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()
                file.close()

    def write(self, data: list[dict]):
        with open(self.path, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerows(data)
            file.close()

    def read(self):
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file, fieldnames=self.fields)

            for line in reader:
                print(line)
