import numpy as np
import timeit

class Perceptron:
    """
    A simple implementation of a perceptron, which is a type of artificial neuron used in machine learning.

    The perceptron is a binary classifier that maps input features to a binary output (0 or 1) using a linear
    decision boundary. It is one of the simplest types of artificial neural networks and is used for supervised
    learning of binary classifiers.

    Key Characteristics:
    - The perceptron calculates a weighted sum of the input features and applies a step function to determine
      the output.
    - It includes a bias term, which allows the decision boundary to be shifted away from the origin.
    - The perceptron is trained using the perceptron learning rule, which updates the weights based on the
      error between the predicted and target outputs.

    This implementation supports training on a dataset with a specified number of epochs and a learning rate
    to control the step size of weight updates.
    """
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        # Initialize the perceptron with the specified input size, learning rate, and number of epochs
        # Weights are initialized to zero, with an additional weight for the bias term
        # The bias term allows the decision boundary to be shifted away from the origin
        self.weights = np.zeros(input_size + 1)  # +1 for the bias term
        self.learning_rate = learning_rate  # The step size for weight updates
        self.epochs = epochs  # Number of times to iterate over the training dataset

    def predict(self, x):
        # Add a bias term (1) to the input vector to account for the bias weight
        # The bias term allows the decision boundary to be shifted away from the origin.
        # Without a bias, the perceptron can only create a decision boundary that passes through the origin.
        # This means the line must be of the form ax + by = 0. For some datasets, such a line cannot separate
        # the two classes because all points might be on the same side of any line passing through the origin.
        # By introducing a bias, the decision boundary can be of the form ax + by + c = 0, where c is the bias term.
        # This allows the line to be shifted, enabling it to separate the classes effectively.
        #
        # Example:
        # Consider a simple 2D dataset where you want to classify points into two categories:
        # - Class 0: Points (1, 1), (2, 2)
        # - Class 1: Points (3, 3), (4, 4)
        # Without a bias, the perceptron can only create a decision boundary that passes through the origin.
        # Such a line cannot separate the two classes because all points are on the same side of any line
        # passing through the origin.
        # With a bias, the decision boundary can be of the form ax + by + c = 0, allowing it to shift.
        # For example, a line like x + y - 5 = 0 (where the bias c = -5) can separate the two classes:
        # - Points (1, 1) and (2, 2) will be on one side of the line.
        # - Points (3, 3) and (4, 4) will be on the other side.
        x_with_bias = np.insert(x, 0, 1)
        # Calculate the linear combination of inputs and weights (dot product)
        # This represents the activation of the perceptron
        # Example with Cats and Dogs:
        # Assume we have two input features: weight and height. Let's say the learned weights are
        # w1 = 0.5 for weight and w2 = 0.3 for height, with a bias b = -20.
        #
        # - Cats: Typically have lower weight and height, e.g., (4, 30), (5, 35).
        # - Dogs: Typically have higher weight and height, e.g., (20, 60), (25, 70).
        #
        # For Cats:
        # Input: (4, 30)
        # Weighted Sum: z = 0.5 * 4 + 0.3 * 30 - 20 = 2 + 9 - 20 = -9
        # Since z < 0, the TLU outputs 0 (assuming 0 represents cats).
        #
        # For Dogs:
        # Input: (20, 60)
        # Weighted Sum: z = 0.5 * 20 + 0.3 * 60 - 20 = 10 + 18 - 20 = 8
        # Since z >= 0, the TLU outputs 1 (assuming 1 represents dogs).
        linear_output = np.dot(x_with_bias, self.weights)
        # Apply the step function to the linear output
        # If the result is >= 0, the perceptron outputs 1; otherwise, it outputs 0
        return 1 if linear_output >= 0 else 0

    def fit(self, x, y):
        # Train the perceptron using the provided dataset (x: inputs, y: target outputs)
        # Iterate over the dataset for the specified number of epochs
        for _ in range(self.epochs):
            for input_x, target_y in zip(x, y):
                # Make a prediction for the current input
                prediction = self.predict(input_x)
                # Calculate the error as the difference between the target and prediction
                error = target_y - prediction
                # Update the weights (excluding the bias) using the perceptron learning rule
                # The rule is: w = w + learning_rate * error * input
                # This adjusts the weights in the direction that reduces the error between the
                # predicted and target outputs.
                # 
                # Mathematically, if the input vector is x = [x1, x2, ..., xn] and the weights
                # are w = [w1, w2, ..., wn], the update for each weight wi is:
                # wi = wi + learning_rate * (target_y - prediction) * xi
                #
                # Example:
                # Suppose we have a single input feature x = [2] and the target output is 1.
                # If the prediction is 0, the error is 1 (1 - 0).
                # With a learning rate of 0.1, the weight update would be:
                # w1 = w1 + 0.1 * 1 * 2 = w1 + 0.2
                # This increases the weight, making the perceptron more likely to predict 1
                # for this input in the future.
                self.weights[1:] += self.learning_rate * error * input_x
                # Update the bias term separately using the same learning rule
                # The bias weight is updated to adjust the decision boundary independently of the input features.
                # The update rule is: bias_weight = bias_weight + learning_rate * error
                # This allows the perceptron to shift the decision boundary up or down.
                #
                # Example:
                # Continuing from the previous example, if the error is 1 and the learning rate is 0.1,
                # the bias weight update would be:
                # bias_weight = bias_weight + 0.1 * 1 = bias_weight + 0.1
                # This adjustment helps the perceptron to better fit the training data by shifting
                # the decision boundary.
                self.weights[0] += self.learning_rate * error  # Update bias


if __name__ == "__main__":
    # Example dataset: OR logic gate
    # The first set of square brackets `[]` is used to define the outer structure of the 2D array,
    # which is essentially a list of lists in Python. This outer list contains all the individual
    # input vectors (which are themselves lists) as its elements. Here's why it's structured this way:
    # 1. 2D Array Representation: In Python, a 2D array is typically represented as a list of lists.
    #    Each inner list represents a row in the 2D array, and the outer list contains all these rows.
    # 2. Input Vectors: Each inner list [0, 0], [0, 1], [1, 0], and [1, 1] is an individual input vector.
    #    These vectors are the individual data points that the perceptron will process.
    # 3. Batch Processing: By storing all input vectors in a single 2D array, you can easily iterate
    #    over them in a loop, which is useful for batch processing during training. This structure
    #    allows you to apply operations across all input vectors efficiently using NumPy's vectorized operations.
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 1])

    perceptron = Perceptron(input_size = 2)
    perceptron.fit(x, y)

    # Fucntion to perform and time the prediction
    def time_prediction():
        # Let's make a prediction
        new_input = np.array([1, 0]) # Example input
        prediction = perceptron.predict(new_input) # Perform prediction
        print(f"Prediction for input {new_input}: {prediction}")
    
    # Time the prediction
    execution_time = timeit.timeit(time_prediction, number=1)
    print(f"Time taken for prediction: {execution_time} seconds")

