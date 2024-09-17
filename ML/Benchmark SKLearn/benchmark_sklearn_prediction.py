import gc
import time
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder


def _not_in_sphinx():
    # Hack to detect whether we are running by the sphinx builder
    return "__file__" in globals()

def atomic_benchmark_estimator(estimator, X_test, verbose=False, sample_size=1000):
    """Measure runtime prediction of each instance with an option to sample."""
    
    # Ensure the sample size doesn't exceed the number of available instances
    n_instances = min(sample_size, X_test.shape[0])
    
    # Randomly sample a subset of the test set
    sampled_X_test = X_test.sample(n=n_instances, random_state=42).reset_index(drop=True)
    
    runtimes = np.zeros(n_instances, dtype=float)
    
    for i in range(n_instances):
        instance = sampled_X_test.iloc[[i], :]  # Select a single instance (as DataFrame)
        
        start = time.time()
        estimator.predict(instance)  # Make a prediction
        runtimes[i] = time.time() - start  # Measure prediction time
    
    if verbose:
        print(
            "atomic_benchmark runtimes:",
            min(runtimes),
            np.percentile(runtimes, 50),  # Median runtime
            max(runtimes),
        )
        
    return runtimes


def bulk_benchmark_estimator(estimator, X_test, n_bulk_repeats, verbose):
    """Measure runtime prediction of the whole input."""
    n_instances = X_test.shape[0]
    runtimes = np.zeros(n_bulk_repeats, dtype=float)
    for i in range(n_bulk_repeats):
        start = time.time()
        estimator.predict(X_test)
        runtimes[i] = time.time() - start
    runtimes = np.array(list(map(lambda x: x / float(n_instances), runtimes)))
    if verbose:
        print(
            "bulk_benchmark runtimes:",
            min(runtimes),
            np.percentile(runtimes, 50),
            max(runtimes),
        )
    return runtimes

def benchmark_estimator(estimator, X_test, n_bulk_repeats=30, verbose=False):
    """
    Measure runtimes of prediction in both atomic and bulk mode.

    Parameters
    ----------
    estimator : already trained estimator supporting `predict()`
    X_test : test input
    n_bulk_repeats : how many times to repeat when evaluating bulk mode

    Returns
    -------
    atomic_runtimes, bulk_runtimes : a pair of `np.array` which contain the
    runtimes in seconds.

    """
    atomic_runtimes = atomic_benchmark_estimator(estimator, X_test, verbose)
    bulk_runtimes = bulk_benchmark_estimator(estimator, X_test, n_bulk_repeats, verbose)
    return atomic_runtimes, bulk_runtimes

def boxplot_runtimes(runtimes, pred_type, configuration):
    """
    Plot a new `Figure` with boxplots of prediction runtimes.

    Parameters
    ----------
    runtimes : list of `np.array` of latencies in micro-seconds
    cls_names : list of estimator class names that generated the runtimes
    pred_type : 'bulk' or 'atomic'

    """

    fig, ax1 = plt.subplots(figsize=(10, 6))
    bp = plt.boxplot(
        runtimes,
    )

    cls_infos = [
        "%s\n(Max Depth: %d, Number of Nodes: %d)"
        % (
            estimator_conf["name"],
            *estimator_conf["complexity_computer"](estimator_conf["instance"])  # Unpack tuple values
        )
        for estimator_conf in configuration["estimators"]
    ]
    plt.setp(ax1, xticklabels=cls_infos)
    plt.setp(bp["boxes"], color="black")
    plt.setp(bp["whiskers"], color="black")
    plt.setp(bp["fliers"], color="red", marker="+")

    ax1.yaxis.grid(True, linestyle="-", which="major", color="lightgrey", alpha=0.5)

    ax1.set_axisbelow(True)
    ax1.set_title(
        "Prediction Time per Instance - %s, %d feats."
        % (pred_type.capitalize(), configuration["n_features"])
    )
    ax1.set_ylabel("Prediction Time (us)")

    plt.show()

def benchmark_throughputs(configuration, duration_secs=0.1):
    """benchmark throughput for different estimators."""

    # Use the already pre-split dataset instead of generating a new one
    X_train = configuration['X_train']
    y_train = configuration['y_train']
    X_test = configuration['X_test']
    y_test = configuration['y_test']

    throughputs = dict()
    for estimator_config in configuration["estimators"]:
        estimator_config["instance"].fit(X_train, y_train)
        start_time = time.time()
        n_predictions = 0
        while (time.time() - start_time) < duration_secs:
            estimator_config["instance"].predict(X_test.iloc[[0]])
            n_predictions += 1
        throughputs[estimator_config["name"]] = n_predictions / duration_secs
    return throughputs


def plot_benchmark_throughput(throughputs, configuration):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["r", "g", "b"]
    cls_infos = [
        "%s\n(Max Depth: %d, Number of Nodes: %d)"
        % (
            estimator_conf["name"],
            *estimator_conf["complexity_computer"](estimator_conf["instance"])  # Unpack tuple values
        )
        for estimator_conf in configuration["estimators"]
    ]
    cls_values = [
        throughputs[estimator_conf["name"]]
        for estimator_conf in configuration["estimators"]
    ]
    plt.bar(range(len(throughputs)), cls_values, width=0.5, color=colors)
    ax.set_xticks(np.linspace(0.25, len(throughputs) - 0.75, len(throughputs)))
    ax.set_xticklabels(cls_infos, fontsize=10)
    ymax = max(cls_values) * 1.2
    ax.set_ylim((0, ymax))
    ax.set_ylabel("Throughput (predictions/sec)")
    ax.set_title(
        "Prediction Throughput for different estimators (%d features)"
        % configuration["n_features"]
    )
    plt.show()

def benchmark(configuration):
    """Run the whole benchmark."""

    # Use the already pre-split dataset instead of generating a new one
    X_train = configuration['X_train']
    y_train = configuration['y_train']
    X_test = configuration['X_test']
    y_test = configuration['y_test']

    stats = {}
    for estimator_conf in configuration["estimators"]:
        print("Benchmarking", estimator_conf["instance"])
        estimator_conf["instance"].fit(X_train, y_train)
        gc.collect()
        a, b = benchmark_estimator(estimator_conf["instance"], X_test)
        stats[estimator_conf["name"]] = {"atomic": a, "bulk": b}

    cls_names = [
        estimator_conf["name"] for estimator_conf in configuration["estimators"]
    ]
    runtimes = [1e6 * stats[clf_name]["atomic"] for clf_name in cls_names]
    boxplot_runtimes(runtimes, "atomic", configuration)
    runtimes = [1e6 * stats[clf_name]["bulk"] for clf_name in cls_names]
    boxplot_runtimes(runtimes, "bulk (%d)" % configuration["n_test"], configuration)




# Load your dataset
df = pd.read_csv('ML/assets/train.csv')

# Drop rows where target or important features are missing (optional, based on your dataset)
df = df.dropna(subset=['OpenStatus'])

# Preprocess columns with missing values, you can use fillna or drop rows
df.fillna(value={'Tag1': 'unknown', 'Tag2': 'unknown', 'Tag3': 'unknown', 'Tag4': 'unknown', 'Tag5': 'unknown'}, inplace=True)

# Encode categorical variables using LabelEncoder
le = LabelEncoder()

# Convert 'PostCreationDate' and 'OwnerCreationDate' to datetime and extract features like year, month, etc.
df['PostCreationDate'] = pd.to_datetime(df['PostCreationDate'], errors='coerce')
df['OwnerCreationDate'] = pd.to_datetime(df['OwnerCreationDate'], errors='coerce')

# Create new features from datetime
df['PostYear'] = df['PostCreationDate'].dt.year
df['OwnerYear'] = df['OwnerCreationDate'].dt.year

# Select categorical columns to encode
for column in ['OpenStatus', 'Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5']:
    df[column] = le.fit_transform(df[column].astype(str))

# Define features (X) and target (y)
X = df[['PostId', 'OwnerUserId', 'ReputationAtPostCreation', 'OwnerUndeletedAnswerCountAtPostTime', 'PostYear', 'OwnerYear', 'Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5']]
y = df['OpenStatus']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the configuration dictionary
configuration = {
    "X_train": X_train,
    "y_train": y_train,
    "X_test": X_test,
    "y_test": y_test,
    "n_train": X_train.shape[0],  # Number of training samples
    "n_test": X_test.shape[0],    # Number of testing samples
    "n_features": X_train.shape[1],  # Number of features (columns) in X
    "estimators": [
        {
            "name": "DecisionTreeClassifier",
            "instance": DecisionTreeClassifier(random_state=42),
            "complexity_label": "complexity metrics",
            "complexity_computer": lambda clf: (
                clf.tree_.max_depth,       # Maximum depth of the decision tree
                clf.tree_.node_count       # Total number of nodes in the tree
            ),
        }
    ],
}

benchmark(configuration)
throughputs = benchmark_throughputs(configuration)
plot_benchmark_throughput(throughputs, configuration)
