from JsonReader import JsonReader
from SequenceDrawer import SequenceDrawer

jr = JsonReader("test.jsonl")
positions = jr.getPositions(0)
# Well, SequenceDrawer is pretty useless as a class, it made sense when I designed it.
# TODO: remove it.
sd = SequenceDrawer("imgs/{x}.jpg".format(x=jr.getImageId(0)))
sd.generate_video(jr.getImageId(0), positions)
