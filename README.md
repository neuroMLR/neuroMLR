<!-- README.md -->
# Data

Download the [preprocessed data](https://drive.google.com/file/d/1bICE26ndR2C29jkfG2qQqVkmpirK25Eu/view?usp=sharing) and unzip the downloaded .zip file.  

Set the PREFIX_PATH variable in my_constants.py as the path to this extracted folder.

For each city (Chengdu, Harbin etc), there are two types of data:

#### 1. Mapmatched pickled trajectories

Stored as a python pickled list of tuples, where each tuple is of the form (trip_id, trip, time_info). Here each trip is a list of edge identifiers.


#### 2. OSM map data
	
In the map folder, there are the following files-

1. _nodes.shp_ : Contains OSM node information (global node id mapped to (latitude, longitude)) 
2. _edges.shp_ : Contains network connectivity information (global edge id mapped to corresponding node ids)
3. _graph_with_haversine.pkl_ : Pickled NetworkX graph corresponding to the OSM data  


# Dependencies

The code has been tested for Python version 3.7.7 and CUDA 10.2. We recommend that you use the same. 

To create a virtual environment using conda, 
```bash
conda create -n ENV_NAME python=3.7.7
conda activate ENV_NAME
```

All dependencies can be installed by running the following commands - 

```bash
pip install -r requirements.txt
pip install --no-index torch-scatter -f https://pytorch-geometric.com/whl/torch-1.6.0+cu102.html
pip install --no-index torch-sparse -f https://pytorch-geometric.com/whl/torch-1.6.0+cu102.html
pip install --no-index torch-cluster -f https://pytorch-geometric.com/whl/torch-1.6.0+cu102.html
pip install --no-index torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.6.0+cu102.html
pip install torch-geometric
```


# Usage

After setting PREFIX_PATH in the my_constants.py file, the script can be run directly as follows- 
```bash
python -i main.py -dataset harbin_data -gnn GCN -lipschitz 
```
Other functionality can be toggled by adding them as arguments, for example,

```bash
python -i main.py -dataset DATASET -gpu_index GPU_ID -eval_frequency EVALUATION_PERIOD_IN_EPOCHS -epochs NUM_EPOCHS 
python -i main.py -traffic -attention
python -i main.py -check_script
python -i main.py -cpu

```

Brief description of other arguments/functionality - 

<!-- - _-check_script_: to run on partial subset of train_data, as a sanity test
- _-cpu_: forces computation on a cpu instead of the available gpu
- _-gnn_: can choose between a GCN or a GAT
- _-gnn_layers_: number of layers for the graph neural network used
- _-epochs_: number of epochs to train for
- _-percent_data_: percentage data used for training
- _-fixed_embeddings_: to make the embeddings static, they aren't learnt as parameters of the network
- _-embedding_size_: the dimension of embeddings used
- _-hidden_size_: hidden dimension for the MLP 
- _-traffic_: to toggle the attention module
- _-attention_: to toggle the attention module -->


| Argument  | Functionality |
| ------------- |-------------|
| _-check_script_ | to run on a fixed subset of train_data, as a sanity test |
| _-cpu_ | forces computation on a cpu instead of the available gpu |
| _-gnn_ | can choose between a GCN or a GAT |
| _-gnn_layers_ | number of layers for the graph neural network used |
| _-epochs_ | number of epochs to train for |
| _-percent_data_ | percentage data used for training |
| _-fixed_embeddings_ | to make the embeddings static, they aren't learnt as parameters of the network |
| _-embedding_size_ | the dimension of embeddings used |
| _-hidden_size_ | hidden dimension for the MLP  |
| _-traffic_ | to toggle the attention module |
| _-attention_ | to toggle the attention module |

For exact details about the expected format and possible inputs please refer to the args.py and my_constants.py files. 


