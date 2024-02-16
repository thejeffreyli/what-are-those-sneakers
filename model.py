import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        
        # input layer: (224, 224, 3)
        
        # output size: (224, 224, 32)
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=32)
        # output size: (112, 112, 32)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # output size: (112, 112, 64)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features=64)
        # output size: (56, 56, 64)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # output size: (56, 56, 128)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(num_features=128)
        # output size: (28, 28, 128)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        
        self.flatten = nn.Flatten()
        
        # in: (28, 28, 128) = 100352 
        self.fc1 = nn.Linear(128 * 28 * 28, 256)
        self.fc2 = nn.Linear(256, 10)

        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool1(self.relu(self.bn1(self.conv1(x))))
        x = self.pool2(self.relu(self.bn2(self.conv2(x))))
        x = self.pool3(self.relu(self.bn3(self.conv3(x))))
        
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x
