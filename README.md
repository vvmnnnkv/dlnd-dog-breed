# Dog Breed Classifier Project

This project was done as part of Udacity Deeplearning Nanodegree.

Data, model, and algorithm exploration is contained in the jupyter notebook in the `model` folder. 

To download training data, execute `cd model/data/download && ./download_data.sh`.

YOLO detection part relies on code from here: https://github.com/ultralytics/yolov3. 
To make it working, download 3rd-party code and weights: 
`cd model && git clone https://github.com/ultralytics/yolov3 && cd yolov3 && ./weights/download_yolov3_weights.sh`
