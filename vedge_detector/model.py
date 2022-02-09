from keras.models import model_from_json
import numpy as np
import requests
import tempfile
import os
import skimage.transform
from PIL import Image
import xarray as xr

class vedge_detector:
    def __init__(self, model_json: str="https://zenodo.org/record/6023284/files/Model_VedgeDetector.json?download=1",
                 model_weights: str="https://zenodo.org/record/6023284/files/weights-VedgeDetector.hdf5?download=1"):

        self.temp_dir = tempfile.TemporaryDirectory()
        self.download_file(model_json, path2save=os.path.join(self.temp_dir.name,'model.json'))
        self.download_file(model_weights, path2save=os.path.join(self.temp_dir.name,'model.hdf5'))
        self.pretrained_model = self.load_pretrained()
        self.temp_dir.cleanup()

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

    def predict(self, image: np.ndarray, provider: str = "planet") -> np.ndarray:

        image_xr = xr.DataArray(image, dims=['y', 'x', 'band'],
                                      coords={'y': np.arange(image.shape[0]),
                                              'x': np.arange(image.shape[1]),
                                              'band': np.arange(image.shape[2])})

        # subset RGB bands
        channels_provider = {
            'sentinel': ["cirrus", "blue", "red", "green", "NIR"],
            'planet': ["blue", "red", "green", "NIR"],
            'rgb': ["blue", "red", "green"]
        }

        image_channels = channels_provider[provider]
        target_bands = ["red", "green", "NIR"]

        image_all = image_xr.assign_coords(band_id=('band', image_channels))
        image_all = image_all.set_index(band="band_id")

        if len(image_all.band) > 3:
            image_target = image_all.sel(band=target_bands)
        else:
            image_target = image_all

        resized = skimage.transform.resize(image_target, (480, 480, 3))
        resized = np.expand_dims(resized, axis=0)

        pred = self.pretrained_model.predict(resized)

        # return only the last layer
        outArray = pred[5]
        outArray = np.squeeze(outArray, axis=0)
        outArray = np.squeeze(outArray, axis=2)
        imOut = Image.fromarray(outArray)
        imOut = imOut.resize((len(image[0]), len(image[:, 0])))
        final = np.array(imOut)

        return final