## Instalación local

- pip install tensorflow==2.4.0
- pip install keras==2.4.3 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1 h5py==2.10.0 matplotlib==3.3.2 opencv-python keras-resnet==0.2.0
- pip install imageai --upgrade


## Comprimir archivo ZIP

- pip install --target ./package tensorflow==2.4.0 keras==2.4.3 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1 h5py==2.10.0 matplotlib==3.3.2 opencv-python keras-resnet==0.2.0 imageai --upgrade

- cd package

- zip -r ../my-deployment-package.zip .

- cd ..

- zip -g my-deployment-package.zip lambda_function.py

-zip -g my-deployment-package.zip resnet50_coco_best_v2.1.0.h5

- zip -g my-deployment-package.zip video2.mp4

-El zip subirlo a S3