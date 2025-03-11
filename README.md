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
* Background：Most Transformer-based models tend to generate large prediction errors for background-sensitive images. Therefore, Transformer-based models \textbf{\textit{have not comprehensively surpassed CNN models on IAA tasks yet}}, to our knowledge. However, a lack of the attention to a background is inconsistent with the original intention of a photographic work, e.g., hierarchical compositions are usually formed with the deliberate consideration of background regions. Moreover, the superfluous attention in Transformers usually leads to unnecessarily computational cost and slow convergence on IAA tasks and may even result in overfitting on small IAA datasets.
![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/252d9bfc-4fac-47f5-bee8-930aecdec109)
* EAT: To guide the IAA model to locate more reasonable regions, we present an Enhancer for Aesthetics-Oriented Transformers (EAT) based on the deformable attention, which is able to learn where to locate interest points and how to refine attention by means of offsets for IAA.
![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/b83441bf-45be-422c-9591-0a65a407ce11)
![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/862933ad-76bf-438f-960e-9cfc60fe3253)


# Performance
* Sota on the AVA, TAD66K, FLICKR-AES datasets
![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/e9ad3d0f-d42a-4c6b-87fd-460d2399c1f6)
![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/0ab7f955-42d4-4d25-9ad7-1dd96a58b679)
![image](https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/ffade6f5-e1be-45ff-9be1-edfee459e08e)


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
1. download weights from: https://drive.google.com/drive/folders/1UpLYGLU5omztVsIWkRPFTVKAOVe_4p3K?usp=sharing，the weights of pre-train weight dat_base_in1k_224.pth：https://pan.baidu.com/s/1kzXIp8V-QRSLOyRNMA-nUw?pwd=8888   code：8888
2. download datasets from their official website
2. run main_nni.py

## If you find our work is useful, pleaes cite our paper:
```
@article{heeat,
  title={EAT: An Enhancer for Aesthetics-Oriented Transformers},
  author={Shuai He, Anlong Ming, Shuntian Zheng, Haobin Zhong, Huadong Ma},
  journal={ACMMM},
  year={2023},
}
```

## Our other works:
<table>
  <thead align="center">
    <tr>
      <td><b>🎁 Projects</b></td>
      <td><b>📚 Publication</b></td>
      <td><b>🌈 Content</b></td>
      <td><b>⭐ Stars</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/woshidandan/Pixel-level-No-reference-Image-Exposure-Assessment"><b>Pixel-level image exposure assessment【首个像素级曝光评估】</b></a></td>
      <td><b>NIPS 2024</b></td>
      <td><b>Code, Dataset</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/Pixel-level-No-reference-Image-Exposure-Assessment?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/Long-Tail-image-aesthetics-and-quality-assessment"><b>Long-tail solution for image aesthetics assessment【美学评估数据不平衡解决方案】</b></a></td>
      <td><b>ICML 2024</b></td>
      <td><b>Code</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/Long-Tail-image-aesthetics-and-quality-assessment?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/Prompt-DeT"><b>CLIP-based image aesthetics assessment【基于CLIP多因素色彩美学评估】</b></a></td>
      <td><b>Information Fusion 2024</b></td>
      <td><b>Code, Dataset</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/Prompt-DeT?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/SR-IAA-image-aesthetics-and-quality-assessment"><b>Compare-based image aesthetics assessment【基于对比学习的多因素美学评估】</b></a></td>
      <td><b>ACMMM 2024</b></td>
      <td><b>Code</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/SR-IAA-image-aesthetics-and-quality-assessment?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/Image-Color-Aesthetics-and-Quality-Assessment"><b>Image color aesthetics assessment【首个色彩美学评估】</b></a></td>
      <td><b>ICCV 2023</b></td>
      <td><b>Code, Dataset</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/Image-Color-Aesthetics-and-Quality-Assessment?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/Image-Aesthetics-and-Quality-Assessment"><b>Image aesthetics assessment【通用美学评估】</b></a></td>
      <td><b>ACMMM 2023</b></td>
      <td><b>Code</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/Image-Aesthetics-and-Quality-Assessment?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/TANet-image-aesthetics-and-quality-assessment"><b>Theme-oriented image aesthetics assessment【首个多主题美学评估】</b></a></td>
      <td><b>IJCAI 2022</b></td>
      <td><b>Code, Dataset</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/TANet-image-aesthetics-and-quality-assessment?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/AK4Prompts"><b>Select prompt based on image aesthetics assessment【基于美学评估的提示词筛选】</b></a></td>
      <td><b>IJCAI 2024</b></td>
      <td><b>Code</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/AK4Prompts?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/mRobotit/M2Beats"><b>Motion rhythm synchronization with beats【动作与韵律对齐】</b></a></td>
      <td><b>IJCAI 2024</b></td>
      <td><b>Code, Dataset</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/mRobotit/M2Beats?style=flat-square&labelColor=343b41"/></td>
    </tr>
    <tr>
      <td><a href="https://github.com/woshidandan/Champion-Solution-for-CVPR-NTIRE-2024-Quality-Assessment-on-AIGC"><b>Champion Solution for AIGC Image Quality Assessment【NTIRE AIGC图像质量评估赛道冠军】</b></a></td>
      <td><b>CVPRW NTIRE 2024</b></td>
      <td><b>Code</b></td>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/woshidandan/Champion-Solution-for-CVPR-NTIRE-2024-Quality-Assessment-on-AIGC?style=flat-square&labelColor=343b41"/></td>
    </tr>
  </tbody>
</table>
