%******************************************************************************************************************%
% This synthesis dataset is provided for model training. There are 116,500 synthetic images from 116 3D            %
% objects. Images are filmed with random attributes, i.e., random object orientation, camera pose,                 %
% lighting and backgrounds.                                                                                        %
%******************************************************************************************************************%


## Synthetic Training Data for Automated Retail Checkout 

Synthetic data is used for model training. Following the generation pipeline in [1], images are filmed with random attributes, i.e., random object orientation, camera pose, lighting and background images. The label format for synthetic data is “id_num.jpg”: 

Taking “00001_697.jpg” for example: 

00001 means the object class id is 00001. 

697 is the counting number. 

We also provide segmentation labels for these images. For example, “00001_697_seg.jpg” is the segmentation label for image “00001_697.jpg”. The white area denotes the area of the object while the black shows the background.   

## Content in the directory:

1. "syn_image_train/". This dir contains 116,500 images for training. 
2. "segmentation_labels/". This dir contains 116,500 segmentation labels. 
3. "labels.txt". It lists the object name and its ID corresponding. 

## Citation 

[1] The synthetic data is generated using the pipeline from

```
@article{yao2022attribute,
  title={Attribute Descent: Simulating Object-Centric Datasets on the Content Level and Beyond},
  author={Yao, Yue and Zheng, Liang and Yang, Xiaodong and Napthade, Milind and Gedeon, Tom},
  journal={arXiv preprint arXiv:2202.14034},
  year={2022}
}
```

## Contact 

If you have any questions, feel free to contact aicitychallenges@gmail.com or yue.yao@anu.edu.au 