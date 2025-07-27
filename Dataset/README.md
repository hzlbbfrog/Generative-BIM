# Dataset description
This is the dataset utilized in our paper, adapted from the StructGAN paper, which we have designated as the **Modified-dataset**.  

In comparison to the original dataset presented in StructGAN, we have implemented several beneficial modifications, as outlined in [Subsection 6.1](https://arxiv.org/abs/2311.04052).  

The dataset includes two sub-datasets: [**All_with_degree**](https://github.com/hzlbbfrog/Generative-BIM/edit/main/Dataset/README.md#all_with_degree) and [**Shearwall_with_degree**](https://github.com/hzlbbfrog/Generative-BIM/edit/main/Dataset/README.md#shearwall_with_degree). **With degree** signifies that the names of the images incorporate the physical condition, as referenced in [Subsection 5.5.1](https://arxiv.org/abs/2311.04052).

## All_with_degree
The images in this sub-dataset encompass all components, including shear walls, infill walls, doors, and windows. 

## Shearwall_with_degree
The images in this sub-dataset focus exclusively on shear walls and infill walls.
Besides, **1channel** indicates the bit depth of the images is 8 (i.e., grayscale images), while **3channel** means the bit depth is 24 (i.e., RGB images).
