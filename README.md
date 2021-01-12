# VEdge_Detector
### Introduction: A tool for automatic coastal vegetation edge detection

VEdge_Detector is a python-based tool for the automated detection of coastal vegetation edges in remote sensing imagery. The tool produces a heatmap, showing the pixels predicted with the highest confidence as being the vegetation line. The images below show the outputs produced by the VEdge_Detector tool in A. Covehithe, Suffolk. United Kingdom; B. Wilk auf Föhr, Germany and C. Varela, Guinea Bissau. 

![alt text](https://github.com/MartinSJRogers/VEdge_Detector/blob/main/example_Images.png) 

### Background description

Recent advances in remote sensing imagery availability and spatial resolution is providing new opportunities for the rapid, cost-effective detection of a shoreline’s location and its change over time. VEdge_Detector has been developed by training a convolutional neural network to identify coastal vegetation edges in c.30,000 remote sensing images of coastal areas. Further details of how the model has been trained and developed is outlined in the following publication: 

The VEdge_Detector tool has been trained to differentiate between the coastal vegetation edge and other boundaries in a remote sensing image, including inland field edges and urban features. 

### Instructions for running the VEdge_Detector tool: 

To run this tool, you first need the required python packages in an environment. This tool is best run using the **Spyder** development environment within **Anaconda**- which can be downloaded [here](https://docs.anaconda.com/anaconda/install/). 



### Image specification

The VEdge_Detector tool has been designed to perform best on:
- Images of sandy/shingle coastlines 
- Haze and cloud-free image. The tool can perform well on some images where clouds not located over or in the immediate vicinity of the coastal vegetation edge
- Images of coastlines with a continuous vegetation edge. The tool has previously detected the seaward boundary of urban land covers or inland waterbodies in some images, but this is not guaranteed in all images.
- Images with an equal width and height (in number of pixels), and on images which do not contain any No Data or NAN values around its border. It is advised that you initially crop your image if it does not meet these requirements. 
- Images with a minimum of size of 480*480 pixels and a maximum size of xxxx. The tool can detect the vegetation edges in larger images, but performance may be compromised and the edge may be blurred. 

The VEdge_Detector tool was trained using Planet 3 – 5 m spatial resolution imagery. It has also detected vegetation edges in Landsat and Copernicus imagery, although performance is not guaranteed. The tool cannot detect the vegetation edge in aerial imagery. 

