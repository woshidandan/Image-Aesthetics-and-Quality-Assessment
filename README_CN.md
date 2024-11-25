[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)

这是我们组在ACMMM 2023关于图像美学评估最新的一篇工作: 

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

因我个人热衷于开源，希望更多的小伙伴关注到这篇工作，故额外写了一篇中文的介绍，不要忘记给我们一个小星星哦，Star一下吧！
------------------------------------------------------------------------------------------------------------


# 网络结构EAT &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* 简要版：通过魔改可变形transformer，解决IAA任务中的注意力偏见问题。
* 太长不看版：若各位同仁，曾对现有的各种IAA网络进行了热力图的可视化，不难发现两个问题，一个是目前的热力图，存在注意力弥散现象，这个在我们去年的[工作](https://github.com/woshidandan/TANet)中有提到，并给了一个
基础的解决办法；还有一个问题，即是本文所关注的注意力偏见问题，即模型只表现出对前景区域的关注。我们是怎么发现这个问题的呢？我们在给甲方交付demo的时候，经常发现，对于一些存在背景虚化的图片评分异常很大，从
人类的角度来说，这种特效还蛮好看的，但对于模型来说，可能就不这么觉得了。另外，我们把AVA数据集内一些背景比较空旷的图像都找出来了，目前的各种IAA模型，在这些样张上表现的效果都比较差。为了解决这个问题，
我们的出发点，是先模拟人类对于图像的关注，并将这种关注以兴趣点形式的最小单元进行表示。但由于目前的IAA模型，均会在ImageNet数据集上进行训练，这些兴趣点还是会优先集中在显著性物体所在的前景区域。为了引导注意
力的方向，我们借助了可变形Transformer中的offset，并对其进行一定的规则限制：探索和利用（做强化学习的同学应该挺熟悉这两个词的）。在网络训练的前期，我们通过计算兴趣点（默认在前景区域）和offset的方向差异，如果
offset奔着兴趣点所在的象限去，则削弱它的趋势，反之，则增强，鼓励网络从非显著性物体所在的背景区域探索更多的美学信息，在训练的后期，则不做什么约束，鼓励网络利用已探索的信息进行美学评分。
* 这套框架性能真的很强，在很多下游的小型IAA任务上表现的都很不错，包括给甲方的基于这套框架改进的demo，在各种牛鬼蛇神的测试场景鲁棒性也较强。这篇工作，也是我个人在IAA赛道上刷SOTA的收官之作，我们也train过一些更SOTA的
版本，但启发性不强。未来会做一些和IAA相关非刷SOTA的，但更有趣的工作！希望各位同行看到我们的工作，审稿时能高抬贵手，ღ( ´･ᴗ･` )比心！

<p align="center">
  <img src="https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/17a1ea80-7b09-49d4-a85e-bd05464ead82" alt="Image" />
  <img src="https://github.com/woshidandan/Image-Aesthetics-Assessment/assets/15050507/142f495b-0129-4776-bbc7-d808507f643a" alt="Image" />
</p>

# 代码环境
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

# 怎么使用代码
* 我们用了微软的自动调参工具[nni](https://github.com/microsoft/nni)，网上有很多nni相关的[使用教程](https://blog.csdn.net/weixin_43653494/article/details/101039198)，强烈推荐同学们使用这个工具，不仅能自动调参，还能替代TensorBoard对训练过程的各项指标可视化。
* 如果你安装好了nni之后，训练时请配置好config.yml和超参数文件search_space.json，然后运行nnictl create --config config.yml -p 8999，训练的可视化后台可以在本地的http://127.0.0.1:8999 或 http://172.17.0.3:8999 看到。
* 如果你不想用这个工具训练或测试，只需要将代码中类似于param_group['lr']这样的超参数的中括号都改为param_group.lr就可以了。
* EAT用到的预训练权重dat_base_in1k_224.pth搁这里下载：链接：https://pan.baidu.com/s/1kzXIp8V-QRSLOyRNMA-nUw?pwd=8888，提取码：8888

# 如果你觉得这篇工作对你有帮助，请引用，不要白嫖-_-:
```
@article{heeat,
  title={EAT: An Enhancer for Aesthetics-Oriented Transformers},
  author={Shuai He, Anlong Ming, Shuntian Zheng, Haobin Zhong, Huadong Ma},
  journal={ACMMM},
  year={2023},
}
```

# 组内其它同类型工作:
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

# 其它
* 我们实验室的主页：[视觉机器人与智能技术实验室](http://www.mrobotit.cn/Default.aspx)。
* 我的个人主页：[博客](https://xiaohegithub.cn/)，[知乎](https://www.zhihu.com/people/wo-shi-dan-dan-87)。
