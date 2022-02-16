import numpy as np
from vedge_detector import vedge_detector

# load model
model = vedge_detector()

# test random data
rgb_planet = np.random.randint(255, size=(900, 800, 4), dtype=np.uint8)

pred = model.predict(rgb_planet, 'Planet')
