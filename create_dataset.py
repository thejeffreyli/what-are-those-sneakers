# import packages
import matplotlib.pyplot as plt
import os
from PIL import Image
from path import Path
import numpy as np
import cv2
import shutil

'''
Note: Prior to creating the dataset, you will need to manually clean the dataset
and remove images if the shoe does not match the label.
'''

class InitData():

    def __init__(self, root_dir):
        
        self.root_dir = root_dir
        self.resize_shape = (224, 224)
        
        # extract class names through names of folders
        folders = [dir for dir in sorted(os.listdir(root_dir)) if os.path.isdir(root_dir/dir)]
        self.classes = {folder: i for i, folder in enumerate(folders)}
        self.counter = {folder: 0 for i, folder in enumerate(folders)}
    
        # iter through the different class labels
        self.files = []
        for label in self.classes.keys():
            
            # directory for the given label
            new_dir = root_dir/Path(label)
            
            # clean and save image into new desired directory (i.e. save_dir)
            for file in os.listdir(new_dir):
                img = plt.imread(new_dir/file)                
                img = self.__preproc__(img)
                img = Image.fromarray(img)
                
                img_name = str(self.counter[label]) +".jpg"         
    
                # specify directory
                output_dir = Path(label)
                
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                    print(f"Directory '{output_dir}' successfully created.")
                img.save(output_dir/img_name)
                
                # create dataframe 
                sample = {}
                sample['path'] = img_name
                sample['label'] = label
                self.files.append(sample)
                
                # numbering images
                self.counter[label] += 1
                
        self.__split_save__()
        
        

    def __len__(self):
        return len(self.files)

    def __preproc__(self, img):
        resized_img = cv2.resize(img, self.resize_shape, 
                                   interpolation=cv2.INTER_LINEAR)
        return resized_img
        
    def __split_save__(self):
        
        np.random.seed(42)
        np.random.shuffle(self.files)
        
        # split ratio
        split_idx = int(self.__len__() * 0.7)
        train_set = self.files[:split_idx]
        test_set = self.files[split_idx:]
        
        self.__save__(train_set, train = True)
        self.__save__(test_set, train = False)
        self.__del__()
        
    
    def __save__(self, dataset, train):
        
        base_path = Path("train" if train else "test")
        for entry in dataset:
            source_dir = Path(entry['label'])
            target_dir = base_path/source_dir
            
            if not os.path.exists(base_path/source_dir):
                os.makedirs(base_path/source_dir)          
        
            source_file = source_dir/entry['path']            
            shutil.move(source_file, target_dir) 

    def __del__(self):
        for label in self.classes:
            if os.path.exists(Path(label)):
                shutil.rmtree(Path(label))
                print(f"Directory '{Path(label)}' successfully deleted.")
    