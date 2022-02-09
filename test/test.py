import numpy as np
from vedge_detector import vedge_detector
import matplotlib.pyplot as plt

# load model
model = vedge_detector()

# test random data
rgb_planet = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)


pred = model.predict(rgb_planet, 'rgb')

plt.imshow(pred)
plt.show()

## test real data
#from scivision.io import load_pretrained_model, load_dataset
#from skimage.exposure import equalize_hist

#cat = load_dataset('scivision.yml')
#
# ds = cat.sample_image(sample_image='dunwich').to_dask()
#
# channels_provider = {
#     'sentinel': ["blue", "red", "green", "coastal", "NIR"],
#     'planet': ["blue", "red", "green", "NIR"]
# }
#
# image_channels = channels_provider['planet']
# target_bands = ["red", "green", "NIR"]
#
# image_all = ds.assign_coords(channel_id=('channel', image_channels))
# image_all = image_all.set_index(channel="channel_id")
#
# if len(image_all.channel) == 4:
#     image_target = image_all.sel(channel=target_bands)
# else:
#     image_target = image_all
#
# pred = model.predict(image_target)
#
# tensor = np.stack([image_all[..., image_channels.index('red')], image_all[..., image_channels.index('green')],
#                    image_all[..., image_channels.index('blue')]])
# rgb = equalize_hist(tensor.swapaxes(0, 1).swapaxes(1, 2))
#
# fig, ax = plt.subplots(1,2, sharex=True, sharey=True)
# axs = ax.flatten()
# axs[0].imshow(rgb)
# axs[0].set_title('Satellite image (RGB)')
# axs[1].imshow(final)
# axs[1].set_title('VEdge Detector Prediction')
# plt.show()
