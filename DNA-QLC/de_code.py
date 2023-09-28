#!/usr/bin/env python
# coding: utf-8

# In[1]:



# from PIL import Image
import torch
import torchvision.transforms.functional as tvf
import pickle

from models.library import qres34m
# from utils import bits_sequence
from utils import sequence_bits

dna_path = "Data/compression/Mona Lisa.dna"
save_path = './Data/compression/Mona Lisa.bits'
Reimage_path = "./Data/compression/ReMona Lisa.jpg"
# Initialize model and load pre-trained weights

# In[2]:


model = qres34m()

msd = torch.load('checkpoints/qres34m/lmb128/last_ema.pt')['model']
model.load_state_dict(msd) #torch.load_state_dict()函数就是用于将预训练的参数权重加载到新的模型之中

model.eval()
model.compress_mode()
# Decode, Decompress and reconstruct the image

# In[3]:
sequence_bits.decode(input_path=dna_path, output_path=save_path, has_index=True, need_log=True)
print("decode completed")







# In[4]:
with open(save_path,'rb') as f:
    compressed_obj = pickle.load(file=f)
img_h, img_w = compressed_obj.pop()
im_hat = model.decompress(compressed_obj)
im_hat = im_hat[:, :, :img_h, :img_w]
print('The image reconstruction is complete')
img0=tvf.to_pil_image(im_hat[0])
img0.save(Reimage_path)





