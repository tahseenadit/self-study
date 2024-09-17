import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import time
from tqdm import tqdm
import psutil
from memory_profiler import memory_usage


# Load dataset
df = pd.read_csv('ML/assets/train.csv')

# Drop rows where target or important features are missing (optional, based on your dataset)
df = df.dropna(subset=['OpenStatus'])

# Preprocess columns with missing values, we can use fillna or drop rows
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


def batch_processing(X, y, batch_size=10000):
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Number of batches
    num_batches = int(np.ceil(X_train.shape[0] / batch_size))

    total_time = 0
    batch_accuracies = []

    print(f"Total number of batches: {num_batches}\n")

    # Start tqdm progress bar
    for i in tqdm(range(num_batches), desc="Processing Batches"):
        # Get the current batch
        start = i * batch_size
        end = min((i + 1) * batch_size, X_train.shape[0])

        X_batch = X_train[start:end]
        y_batch = y_train[start:end]

        # Monitor CPU usage and memory usage
        start_cpu = psutil.cpu_percent(interval=None)
        mem_usage_before = memory_usage()[0]

        # Train a DecisionTreeClassifier on this batch
        clf = DecisionTreeClassifier()
        start_time = time.time()
        clf.fit(X_batch, y_batch)
        end_time = time.time()

        # Measure time taken to train
        training_time = end_time - start_time
        total_time += training_time

        # Monitor CPU and memory after training
        end_cpu = psutil.cpu_percent(interval=None)
        mem_usage_after = memory_usage()[0]

        # Evaluate the batch model on test data
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        batch_accuracies.append(accuracy)

        print(f"\nBatch {i+1}/{num_batches} - Training Time: {training_time:.4f} seconds")
        print(f"CPU usage: {end_cpu - start_cpu}%")
        print(f"Memory used: {mem_usage_after - mem_usage_before:.2f} MiB")
        print(f"Accuracy: {accuracy:.4f}")

    print(f"\nTotal Training Time: {total_time:.4f} seconds")
    print(f"Mean Accuracy across batches: {np.mean(batch_accuracies):.4f}")


# Run the batch processing
batch_processing(X, y, batch_size=100000)
