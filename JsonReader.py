import jsonlines


class JsonReader:

    def __init__(self, filename):
        self.lines = []
        with jsonlines.open(filename) as f:
            for line in f.iter():
                self.lines.append(line)

    def getPositions(self, index=0):
        positions = []
        for x in self.lines[index]["traces"]:
            for el in x:
                positions.append(el)
        return positions

    def getImageId(self, index):
        return self.lines[index]["image_id"]

