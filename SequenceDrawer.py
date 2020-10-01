import matplotlib.pyplot as plt
import os
import cv2
from matplotlib.patches import Circle

class SequenceDrawer:

    def __init__(self, image_path):
        self.image = plt.imread(image_path)

    def drawSequence(self, positions, folder='tmp/'):
        fig, ax = plt.subplots(1)
        ax.set_aspect('equal')
        ax.imshow(self.image)
        h, w, c = self.image.shape
        for el in positions:
            circ = Circle((el['x'] * w, el['y'] * h), color='red')
            ax.add_patch(circ)
            plt.savefig(folder + '{t}.jpg'.format(t=el['t']))
            ax.patches = []

    def generate_video(self, video_name, positions, image_folder='tmp/'):

        self.drawSequence(positions)

        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name + '.mp4', 0, fps=15, frameSize=(width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
        for el in os.listdir(image_folder):
            os.remove(image_folder + el)