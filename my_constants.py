from args import *
from termcolor import colored, cprint

#########################################################################
# please set this path according to the extracted folder
PREFIX_PATH = None
# PREFIX_PATH = "/home/qpp/data/preprocessed_data/"
#########################################################################

if PREFIX_PATH is None:
	cprint("Please set the PREFIX_PATH after downloading and extracting the preprocessed data", "red")
	raise SystemExit

args = make_args()
PREFIX_PATH += "{}/".format(args.dataset)

def get_fname(percent_data, s):
	assert s[-4:] == '.pkl', colored('wrong file format', 'red')
	fname = s[:-4] + '_partial_{}.pkl'.format(percent_data)
	return fname

# OUTDATED_DATASETS = ["harbin", "porto", "chengdu"]
OUTDATED_DATASETS = []
PERCENTAGES = [1, 5, 10, 20, 50, 100]

EDGE_DATA = PREFIX_PATH + "map/edges.shp"
NODE_DATA = PREFIX_PATH + "map/nodes.shp"

TRAIN_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = PREFIX_PATH + "preprocessed_train_trips_all.pkl"

TEST_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = PREFIX_PATH + "preprocessed_test_trips_all.pkl"

VAL_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = PREFIX_PATH + "preprocessed_validation_trips_all.pkl"

TRAIN_TRIP_SMALL_FIXED_DATA_PICKLED_WITH_TIMESTAMPS = PREFIX_PATH + "preprocessed_train_trips_small.pkl"
TEST_TRIP_SMALL_FIXED_DATA_PICKLED_WITH_TIMESTAMPS = PREFIX_PATH + "preprocessed_test_trips_small.pkl"
VAL_TRIP_SMALL_FIXED_DATA_PICKLED_WITH_TIMESTAMPS = PREFIX_PATH + "preprocessed_validation_trips_small.pkl"

assert not (args.check_script and args.percent_data is not None), colored('cannot take percent data with check script','red')
assert args.dataset not in OUTDATED_DATASETS or args.override_warnings, colored("these datasets are outdated - {}, are you sure you wanted to run this?".format(OUTDATED_DATASETS), 'red')

if args.check_script:
	TRAIN_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = TRAIN_TRIP_SMALL_FIXED_DATA_PICKLED_WITH_TIMESTAMPS
	TEST_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = TEST_TRIP_SMALL_FIXED_DATA_PICKLED_WITH_TIMESTAMPS
	VAL_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = VAL_TRIP_SMALL_FIXED_DATA_PICKLED_WITH_TIMESTAMPS
elif args.percent_data is not None:
	assert args.percent_data in PERCENTAGES, colored(
		"Choose a percentage value from the predefined ones - {}".format(PERCENTAGES), "red")
	assert args.dataset == "harbin_new", colored(
		"Small percentage of training data not created for this dataset", "red")

	TRAIN_TRIP_DATA_PICKLED_WITH_TIMESTAMPS = get_fname(args.percent_data, TRAIN_TRIP_DATA_PICKLED_WITH_TIMESTAMPS)
	

PICKLED_GRAPH = PREFIX_PATH + "map/graph_with_haversine.pkl"
LEARNT_FEATURE_REP = PREFIX_PATH + "pickled_pca_information_for_traffic_representation.pkl"
CRUCIAL_PAIRS = PREFIX_PATH + "crucial_pairs.pkl"
CACHED_DATA_FILE = PREFIX_PATH + "cached_data.pkl"
INITIALISED_EMBEDDINGS_PATH = "results/" 

model_string = "{}{}{}{}{}".format(('lipschitz_' if args.initialise_embeddings_lipschitz else 'random_'), ('' if args.gnn is None else '{}_'.format(args.gnn)), ('trainable_' if args.trainable_embeddings else 'fixed_'), ('{}_'.format(args.model_uid)), ('' if not args.check_script else 'checkscript'))
MODEL_SAVE_PATH = PREFIX_PATH + 'models/model_{}.pt'.format(model_string)
MODEL_SUPPORT_PATH =  PREFIX_PATH + 'models/model_support_{}.pkl'.format(model_string)
