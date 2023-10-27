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
1. download weights from: https://drive.google.com/drive/folders/1UpLYGLU5omztVsIWkRPFTVKAOVe_4p3K?usp=sharing
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
+ "Thinking Image Color Aesthetics Assessment: Models, Datasets and Benchmarks.", [[pdf]](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/blob/main/Delegate%20Transformer%20for%20Image%20Color%20Aesthetics%20Assessment.pdf) [[code]](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment), ICCV, 2023.
+ "Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks.", [[pdf]](https://www.ijcai.org/proceedings/2022/0132.pdf) [[code]](https://github.com/woshidandan/TANet), IJCAI, 2022.
