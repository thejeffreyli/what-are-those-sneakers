# import packages
import os
from PIL import Image
from torch.utils.data import Dataset, DataLoader
# from path import Path

class SneakerDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        
        self.root_dir = root_dir
        self.transform = transform
         
        self.classes = sorted(os.listdir(root_dir))
        self.class_to_idx = {cls: i for i, cls in enumerate(self.classes)}
        self.file_list = self._build_file_list()

    def _build_file_list(self):
        file_list = []
        
        for cls in self.classes:
            class_path = os.path.join(self.root_dir, cls)
            class_idx = self.class_to_idx[cls]
            for file_name in os.listdir(class_path):
                file_list.append((os.path.join(class_path, file_name), class_idx))
        return file_list

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img_path, label = self.file_list[idx]
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image, label
