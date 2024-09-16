<div align="center">
  <img src="./figures/Title.png">
  <img src="./figures/Generative-BIM.svg" width="50%">
</div>

# Generative AIBIM
This repository is the official implementation of the Structural Design Pipeline Integrating **BIM** and **Generative AI** **(Generative AIBIM)**.  
- :orange: **Paper:** [[Journal Version]](https://www.sciencedirect.com/science/article/pii/S1566253524004329?via%3Dihub) and [[ArXiv Version](https://arxiv.org/abs/2311.04052)]
- :watermelon: **Webpage:**  [[Project page](http://zl-he.com/Generative-BIM/)]
- 🍓 **Authors:** [Zhili He](http://zl-he.com/) (HKUST), [Yu-Hsing Wang](https://ce.hkust.edu.hk/people/yu-hsing-wang-wangyouxing) (HKUST), and [Jian Zhang](https://civil.seu.edu.cn/zj/list.htm) (Southeast University)
## ✒️ Introduction
This repository mainly includes 4 parts:  
- [ ] **Generative AIBIM: Structural design pipeline integrating BIM and generative AI**  
      This pipeline contains 4 stages. Stage I and Stage III are converting 3D BIM models to 2D architectural drawings and converting 2D structural drawings to 3D BIM models.  
      We write Python and Dynamo scripts to implement the two stages.  
      The simple **tutorial** and **implementation code** are publicly available at [Structural design pipeline](https://github.com/hzlbbfrog/Generative-BIM/tree/main/Structural%20design%20pipeline).
- [ ] Stage II introduces the the **P**hysics-based **C**onditional **D**iffusion **M**odel **(PCDM)**. The code is openly accessible at [PCDM](https://github.com/hzlbbfrog/Generative-BIM/tree/main/PCDM).
- [ ] **Modified-dataset**.
- [ ] **Evaluation code** including Score_IoU and FID.

## 📅 Updates
- **`2024/09/01`**: Our paper is publicly available. Link → [Journal version](https://www.sciencedirect.com/science/article/pii/S1566253524004329?via%3Dihub).
- **`2024/08/26`**: Our paper is finally accepted by a prestigious journal, Information Fusion!
- **`2023/11/07`**: The preprint of our paper is available online on arXiv. Link → [Arxiv Paper](https://arxiv.org/abs/2311.04052).
- **`2023/11/04`**: The preprint of our paper is submitted to arXiv.
- **`2022/12/06`**: This repository is built up! It is for the course project of **CIVL 5220 Building Information Modeling and Digital Construction**. Course instructor: [Jack C.P. Cheng](https://www.ce.ust.hk/people/jack-chin-pang-cheng-zhengzhanpeng), Department of Civil and Environmental Engineering, HKUST.

## 🥰 Cite Generative AIBIM!
If you have any problems, please do not hesitate to contact us!
You are very welcome to cite our paper! The BibTeX entry is as follows:
```BibTeX
@article{Generative_AIBIM,
title = {Generative AIBIM: An automatic and intelligent structural design pipeline integrating BIM and generative AI},
journal = {Information Fusion},
volume = {114},
pages = {102654},
year = {2025},
issn = {1566-2535},
doi = {https://doi.org/10.1016/j.inffus.2024.102654},
url = {https://www.sciencedirect.com/science/article/pii/S1566253524004329},
author = {Zhili He and Yu-Hsing Wang and Jian Zhang},
keywords = {Generative AI, Diffusion model, Building information modeling, Intelligent structural design, Shear wall structure}
}
```
## 💓 Acknowledgements
This repo benefits from [OpenAI improved-diffusion](https://github.com/openai/improved-diffusion/tree/main), [DDIM](https://github.com/ermongroup/ddim), and [StructGAN](https://github.com/wenjie-liao/StructGAN_v1).  
Thanks for their wonderful works!
