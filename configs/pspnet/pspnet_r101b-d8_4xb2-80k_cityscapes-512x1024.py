_base_ = './pspnet_r50-d8_4xb2-80k_cityscapes-512x1024.py'
model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(type='ResNet', depth=101))
