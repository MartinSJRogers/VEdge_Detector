# VEdge_Detector
## 1. Introduction: A tool for automatic coastal vegetation edge detection

VEdge_Detector is a python-based tool for the automated detection of coastal vegetation edges in remote sensing imagery. The tool produces a heatmap, showing the pixels predicted with the highest confidence as being the vegetation line. The images below show the outputs produced by the VEdge_Detector tool in A) Suffolk, United Kingdom; B) Wilk auf Föhr, Germany and C) Varela, Guinea Bissau. 

![alt text](https://github.com/MartinSJRogers/VEdge_Detector/blob/main/example_Images.png) 

## 2. Background description

Recent advances in satellite imagery availability and spatial resolution is providing new opportunities for the rapid, cost-effective detection of a shoreline’s location and dynamics. VEdge_Detector has been developed by training a convolutional neural network to identify coastal vegetation edges in c.30,000 satellite images. Further details of how the model has been trained and developed is outlined in the publication by Rogers et al. (2021). 

The VEdge_Detector tool has been trained to differentiate between the coastal vegetation edge and other boundaries in a remote sensing image. This semantic information means the tool can discard other boundaries, including most inland field edges and other urban features. 

## 3. Instructions for running the VEdge_Detector tool

### 3.1. Setting up the python environment

VEdge_Detector is best run using the **Spyder** development environment within **Anaconda**- which can be downloaded [here](https://docs.anaconda.com/anaconda/install/).

To run this tool, first download the repository of files contained within this Github directory onto your computer. It is best to download these files into a new separate folder, e.g. C:/Users/username/Documents/VEdge_Detector

After you have installed Anaconda onto your computer and downloaded the file repository, you then need to install the required python packages in an environment. To create an environment, open the Anaconda prompt (or open a terminal window in Mac and Linux) and use the change directory command, `cd` to go the folder where you have downloaded this repository, e.g.:

```
cd  C:/Users/username/Documents/VEdge_Detector 
```

Then type the following line to create a new environment named VEdge_Detector containing all the necessary packages:

```
conda env create -f environment.yml -n VEdge_Detector
```

This command installs all the required packages into an environment called VEdge_Detector. 

To activate the new environment, type the following command in Anaconda Prompt: 

```
conda activate VEdge_Detector
```

If these steps have worked correctly, you should see the text (VEdge_Detector) in the Anaconda Prompt window before your directory. 

### 3.2. Running the code
Start by opening **Anaconda**, which can be found by typing ‘Anaconda’ into your PC’s search tool. When Anaconda launches, in the top left-hand corner click on the 'Environments' tab (1). Within the Environments tab select the 'VEdge_Detector' environment (2). Finally, click on the 'Home' tab and then launch the Spyder development environment (3)- see picture below. 

![alt text](https://github.com/MartinSJRogers/VEdge_Detector/blob/main/Anaconda_Instructions.png) 

There are two python files you can open and run in spyder: **example_Predict.py** and **ownImage_Predict.py**. If you are new to VEdge_Detector, it is recommended that you first open and run example_Predict.py. If you have correctly downloaded the file repository from this Github directory and set up the python environment (steps explained above), when you press run in it will output the predicted coastal vegetation edge location from an image of Covehithe, Suffolk, UK. The output image will be saved in the same directory. 

There are three parameters you can change in the file: 
-	`testImage` This is the image you want the VEdge_Detector tool to detect the coastal vegetation edge in. There are three other example images which are contained within the downloaded github file directory. Ensure the image filename is perfectly written, otherwise an error will be produced when you run the code. If you want to use your own image, use the ownImage_Predict.py file. Addiitonal instructions for using this file are outlined in the section below. 
-	`Export_Image`- This states whether you want to save the image to your directory or not. This variable can either take the value ‘yes’ or ‘no’ (all lower case). 
-	`Output_Image_Name`- The user-defined filename for the output image. The filename must be placed in quotation marks e.g. “fileName.tif” or apostrophes e.g. ‘fileName.tif’. It is important you also include the file extension type, .tif, otherwise the file will not save. 

#### 3.2.1 Additional instructions if using your own image

If you are using your own image, ensure that it is a .tif file and refer to the **image specification** section below which outlines considerations for the image you use.
In addition to the variable names described above, this file contains an additional parameter which you can change the value of.:

- `Image type`- This variable defines what satellite the image was captured from and can take three values: **'planet'**, **'landsat'** or **'sentinel-2'** (all lower case). As discussed in the image specification section below, this tool was trained using exclusively Planet Imagery. In some circumstances, this tool can work on Landsat and Sentinel-2 imagery, although work is still ongoing to make the tool more robust at detecting the coastal vegetation edge position in these images. 

#### 3.2.2 Image specification

The VEdge_Detector tool has been designed to perform best on:
- Images of sandy/shingle coastlines. 
- Haze and cloud-free images. The tool may detect the coastal vegetation edge in some images where clouds are not located over or in the immediate vicinity of the coastal vegetation edge.
- Images of coastlines with a continuous vegetation edge. The tool has previously also detected the seaward boundary of urban land covers or inland waterbodies in some images, but this is not guaranteed in all images.
- Images with an equal width and height (in number of pixels), and images which do not contain any No Data or NAN values around its border. It is advised that you initially crop your image if it does not meet these requirements. 
- Images with a minimum of size of 480 by 480 pixels and a maximum size of 1000 by 1000 pixels. The tool can detect the vegetation edges in larger images, but performance may be compromised and the edge may be blurred. 

The VEdge_Detector tool was trained using Planet 3 – 5 m spatial resolution imagery. It has also detected vegetation edges in Landsat and Copernicus imagery, although performance is not guaranteed. The tool cannot detect the vegetation edge in aerial imagery. 

