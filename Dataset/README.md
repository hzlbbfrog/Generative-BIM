# Dataset description
This is the dataset employed in our paper. As it has been adapted from the dataset presented in the StructGAN paper, we have designated it as the **Modified-dataset**.

In comparison to the original dataset presented in StructGAN, we have implemented several beneficial modifications, as outlined in [Subsection 6.1](https://www.sciencedirect.com/science/article/pii/S1566253524004329).  

The dataset includes two sub-datasets: [**All_with_degree**](https://github.com/hzlbbfrog/Generative-BIM/tree/main/Dataset#all_with_degree) and [**Shearwall_with_degree**](https://github.com/hzlbbfrog/Generative-BIM/tree/main/Dataset#shearwall_with_degree). **With degree** signifies that the names of the images incorporate the physical condition, as referenced in [Subsection 5.5.1](https://www.sciencedirect.com/science/article/pii/S1566253524004329).

## All_with_degree
This sub-dataset is utilized in our conference paper (i3CE 2025).
The images in this sub-dataset encompass all components, including shear walls, infill walls, doors, and windows. 

## Shearwall_with_degree
This sub-dataset is the adopted dataset in our [journal paper](https://www.sciencedirect.com/science/article/pii/S1566253524004329).
The images in this sub-dataset focus exclusively on shear walls and infill walls.
Besides, **1channel** indicates the bit depth of the images is 8 (i.e., grayscale images), while **3channel** means the bit depth is 24 (i.e., RGB images).
