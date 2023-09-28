#!/usr/bin/env python
# coding: utf-8

# In[1]:



from PIL import Image
import torch
import torchvision.transforms.functional as tvf
import pickle

from models.library import qres34m
from models import qresvae
from utils import bits_sequence
# from utils import sequence_bits
img_path = './images/Mona Lisa.jpg'
dna_path = "Data/compression/Mona Lisa.dna"
# save_path = 'results/celaba64-1.bits'
max_stride = 64
# Initialize model and load pre-trained weights

# In[2]:


model = qres34m()

msd = torch.load('checkpoints/qres34m/lmb128/last_ema.pt')['model']
model.load_state_dict(msd) #torch.load_state_dict()函数就是用于将预训练的参数权重加载到新的模型之中

model.eval()
model.compress_mode()


# Compress and encode an RGB image

# In[3]:



img = Image.open(img_path)
img_padded = qresvae.pad_divisible_by(img, div=max_stride)
im = tvf.to_tensor(img_padded).unsqueeze_(0)
compressed_obj = model.compress(im)
tup = (img.height, img.width)
end=[]
for i in range(len(tup)):
    end.append('{:0>16}'.format(str(bin(tup[i]))[2:]))
k = 0
a_str = ''
while k < len(end):
    a_str = a_str + str(end[k])
    k += 1
compressed_obj.append(a_str)
for i in range(len(compressed_obj)):
    compressed_obj[i]=''.join(['01001100010010010101001101010100', compressed_obj[i]])
compressed_b=''.join(compressed_obj)


#encode
bits_sequence.encode(binary_str=compressed_b, output_path=dna_path, need_log=True)
print("Encode completed")




