from keras.models import model_from_json
import numpy as np
import requests
import tempfile
import os
import skimage.transform

class vedge_detector:
    def __init__(self, model_json: str="https://raw.githubusercontent.com/MartinSJRogers/VEdge_Detector/main/model/Model_VedgeDetector.json",
                 model_weights: str="https://github.com/MartinSJRogers/VEdge_Detector/raw/main/model/weights_VedgeDetector.hdf5",
                 tmp_dir: str = "./_tmp"):

        self.temp_dir = tmp_dir
        os.makedirs(self.temp_dir, exist_ok=True)

        #self.temp_dir = tempfile.TemporaryDirectory()
        #self.download_file(model_json, path2save=os.path.join(self.temp_dir.name,'model.json'))
        #self.download_file(model_weights, path2save=os.path.join(self.temp_dir.name,'model.hdf5'))
        self.download_file(model_json, path2save=os.path.join(self.temp_dir,'model.json'))
        self.download_file(model_weights, path2save=os.path.join(self.temp_dir,'model.hdf5'))
        self.pretrained_model = self.load_pretrained()
        #self.temp_dir.cleanup()

    def download_file(self, url, path2save):

        os.makedirs(os.path.dirname(path2save), exist_ok=True)

        r = requests.get(url, stream=True)
        with open(path2save, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()

    def load_pretrained(self):
        # load json and create model
        json_file = open(os.path.join(self.temp_dir.name,'model.json'), 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(os.path.join(self.temp_dir.name,'model.hdf5'))
        return loaded_model

    def predict(self, image: np.ndarray) -> np.ndarray:

        resized = skimage.transform.resize(image, (480, 480, 3))
        image = np.expand_dims(resized, axis=0)

        y = self.pretrained_model.predict(image)

        return y