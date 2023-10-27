[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)


## Image-Aesthetics-Assessment
This repo contains the official implementation of the ACMMM 2023 paper:

<div align="center">
<h1>
<b>
EAT: An Enhancer for Aesthetics-Oriented Transformers
</b>
</h1>
<h4>
<b>
Shuai He, Anlong Ming, Shuntian Zheng, Haobin Zhong, Huadong Ma
    
Beijing University of Posts and Telecommunications
</b>
</h4>
</div>

[[国内的小伙伴请看更详细的中文说明]](https://github.com/woshidandan/Image-Aesthetics-Assessment/blob/main/README_CN.md)This repo contains the official implementation of the **ACMMM 2023** paper.

# EAT &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Background：Although CNN models have yielded many remarkable achievements, they are susceptible to the attention dispersion phenomenon in IAA tasks and may even fail to properly focus on the aesthetic information of the foreground. Compared to CNN counterparts, Transformer-based models are driven by attention mechanisms, which have larger receptive fields and excel at modeling long-range dependencies, thus allowing models to avoid the above problem. Nevertheless, applying Transformers for IAA is challenging because the attention mechanism of Transformers is a double-edged sword. Most Transformer models have been designed in a saliency-oriented manner to solve classic classification or segmentation problems; consequently, they can more easily focus on or even overemphasize salient objects or foreground areas, which also means that they are more prone to ignore background regions and result in \textbf{\textit{attention bias}} problem. For aesthetic tasks, however, a lack of the attention to a background is inconsistent with the original intention of a photographic work, e.g., hierarchical compositions are usually formed with the deliberate consideration of background regions. Most Transformer-based models tend to generate large prediction errors for background-sensitive images. Therefore, Transformer-based models \textbf{\textit{have not comprehensively surpassed CNN models on IAA tasks yet}}, to our knowledge. Moreover, the superfluous attention in Transformers usually leads to unnecessarily computational cost and slow convergence on IAA tasks and may even result in overfitting on small IAA datasets.

![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/252d9bfc-4fac-47f5-bee8-930aecdec109)


## Environment Installation
* pandas==0.22.0
* nni==1.8
* requests==2.18.4
* torchvision==0.8.2+cu101
* numpy==1.13.3
* scipy==0.19.1
* tqdm==4.43.0
* torch==1.7.1+cu101
* scikit_learn==1.0.2
* tensorboardX==2.5


## How to Run&Check the Code
1. download weights from: https://drive.google.com/drive/folders/1UpLYGLU5omztVsIWkRPFTVKAOVe_4p3K?usp=sharing
2. download datasets from their official website
2. run main_nni.py
