from keras.models import model_from_json
import numpy as np
import skimage.transform
from PIL import Image
import xarray as xr
from skimage.exposure import equalize_hist
import matplotlib.pyplot as plt
import pooch


class vedge_detector:
    def __init__(self,
                 model_json: dict = None,
                 model_weights: dict = None):

        if model_weights is None:
            model_weights = dict(url="doi:10.5281/zenodo.6023284/weights-VedgeDetector.hdf5",
                                 known_hash="md5:d26061f632fe0e246a80be7cc8bc7cce")
        if model_json is None:
            model_json = dict(url="doi:10.5281/zenodo.6023284/Model_VedgeDetector.json",
                              known_hash="md5:43c92ee14a14e58375064713caa031bd")

        # ---- DOWNLOAD
        self.model_json = pooch.retrieve(url=model_json['url'], known_hash=model_json['known_hash'])
        self.model_weights = pooch.retrieve(url=model_weights['url'], known_hash=model_weights['known_hash'])

        # ---- CLASSIFIER
        self.pretrained_model = self.load_pretrained()


    def load_pretrained(self):
        # load json and create model
        json_file = open(self.model_json, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(self.model_weights)
        return loaded_model


    def preprocess(self):

        image_xr = xr.DataArray(self.image , dims=['y', 'x', 'band'],
                                coords={'y': np.arange(self.image.shape[0]),
                                        'x': np.arange(self.image.shape[1]),
                                        'band': np.arange(self.image.shape[2])})

        # subset RGB bands
        channels_provider = {
            'RapidEye': ["blue", "red", "green", "extra", "NIR"],
            'Planet': ["blue", "red", "green", "NIR"],
        }

        self.image_channels = channels_provider[self.provider]
        target_bands = ["red", "green", "NIR"]

        self.image_all = image_xr.assign_coords(band_id=('band', self.image_channels))
        self.image_all = self.image_all.set_index(band="band_id")

        if len(self.image_all.band) > 3:
            image_target = self.image_all.sel(band=target_bands)
        else:
            image_target = self.image_all

        resized = skimage.transform.resize(image_target, (480, 480, 3))
        self.preprocessed = np.expand_dims(resized, axis=0)


    def postprocess(self):
        # return only the last layer
        outArray = self.pred[5]
        outArray = np.squeeze(outArray, axis=0)
        outArray = np.squeeze(outArray, axis=2)
        imOut = Image.fromarray(outArray)
        imOut = imOut.resize((len(self.image[0]), len(self.image[:, 0])))
        self.final = np.array(imOut)

        # equalize
        rgb_array = np.stack(
            [self.image_all[..., self.image_channels.index('red')], self.image_all[..., self.image_channels.index('green')],
             self.image_all[..., self.image_channels.index('blue')]])
        self.rgb_equal = equalize_hist(rgb_array.swapaxes(0, 1).swapaxes(1, 2))


    def show_output(self):

        fig, ax = plt.subplots(1, 2, figsize=(10, 30))
        axs = ax.flatten()
        axs[0].imshow(self.rgb_equal)
        axs[0].set_title('Satellite image (RGB)', size='xx-large')
        axs[1].imshow(self.final)
        axs[1].set_title('VEdge Detector Prediction', size='xx-large')
        plt.show()


    def predict(self, image: np.ndarray, provider: str = "planet") -> np.ndarray:

        self.image = image
        self.provider = provider

        self.preprocess()

        self.pred = self.pretrained_model.predict(self.preprocessed)

        self.postprocess()

        self.show_output()

        return self.final