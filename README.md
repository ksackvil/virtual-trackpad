# Virtual Trackpad
Control your computer without touching your trackpad!

## Quickstart

1. Install the requirements in your working python environment

```
pip install -r requirements.txt
```

2. Run the main.py file from the root folder

```
cd src/
python app.py
```

## Gesture Recognition Model Training
 - link to the original repo: https://github.com/kinivi/hand-gesture-recognition-mediapipe
 - refer to the README.md in the repo for directory structure
 - refer to the README.md for training procedures:
   1. run the main with ```python src/app.py```
   2. press ```k``` to enter logging keypoint mode
   3. press ```Esc``` when finished to close the window
   4. run ```jupyter notebook``` to open training script
   5. open the file "keypoint_classification.ipynb"
   6. in cell 3, change NUM_CLASSES to the current num of models
   7. run all cells to start the training, then save and close