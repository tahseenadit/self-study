### **Purpose of the Criterion Class**

The `Criterion` class is used in decision trees (like the ones in machine learning) to help evaluate how good a split is at a given node of the tree. 

1. **Nodes in Decision Trees:**
   - In a decision tree, data is split into smaller groups at each node to help make predictions. 
   - The split is based on a feature of the data (like age or income) to reduce the “impurity” of the groups. Impurity measures how mixed the data is:
     - For **classification**, impurity is high when the group has many different classes (like a mix of cats and dogs).
     - For **regression**, impurity measures how spread out the numbers are.

2. **What the Criterion Class Does:**
   - It calculates:
     - How “impure” the data at a node is.
     - How much splitting reduces the impurity.
     - The statistics needed to decide whether the split is useful (e.g., means for regression or probabilities for classification).

3. **Why These Metrics Matter:**
   - A good split reduces impurity a lot. The decision tree algorithm uses this to decide the best feature and threshold to split the data at each node.

---

### **Key Concepts in the Class**

Let’s break down the attributes of the class with simpler explanations:

1. **Input Data (Attributes):**
   - `y`: The target values (what we are trying to predict, like class labels or numbers for regression).
   - `sample_weight`: The weight of each sample (some samples might be more important than others).
   - `sample_indices`: Indices of the samples currently being considered.

2. **Splitting the Data:**
   - The data is divided into three parts:
     - **Left node**: Samples from `start` to `pos`.
     - **Right node**: Samples from `pos` to `end`.
     - **Missing values**: Samples that don’t have data for the feature being used to split.

3. **Statistics for the Split:**
   - `n_node_samples`: Total samples in the current node.
   - `weighted_n_node_samples`: Total weighted samples in the node.
   - Similar stats for the left and right nodes (`weighted_n_left` and `weighted_n_right`) and for missing values (`weighted_n_missing`).

4. **Handling Missing Data:**
   - `n_missing`: How many samples are missing a value for the splitting feature.
   - `missing_go_to_left`: Whether missing samples are assigned to the left node.

---

### **Example: Using the Criterion Class**

Let’s say you’re building a decision tree to classify animals based on their features (like weight and height). Your target (`y`) is the animal type (cat = 0, dog = 1).

#### Data at a Node:
| Sample | Weight (kg) | Height (cm) | Animal Type (`y`) |
|--------|-------------|-------------|--------------------|
| 1      | 4.5         | 30          | Cat (0)           |
| 2      | 6.2         | 35          | Cat (0)           |
| 3      | 7.8         | 40          | Dog (1)           |
| 4      | Missing     | 38          | Dog (1)           |
| 5      | 8.1         | 42          | Dog (1)           |

#### Splitting on Feature: `Weight`
The criterion evaluates a split based on `Weight`. For example, we might split the data at `Weight < 6.0`.

1. **Left Node**: Samples 1 and 2 (Weight < 6.0)
   - **Impurity**: Both are cats, so the impurity is **0.0** (pure node).

2. **Right Node**: Samples 3 and 5 (Weight ≥ 6.0)
   - **Impurity**: Both are dogs, so the impurity is **0.0** (pure node).

3. **Missing Data**: Sample 4
   - If `missing_go_to_left` is true, it joins the left node.
   - Otherwise, it joins the right node.

#### Statistics:
The `Criterion` class calculates these statistics for each split:
- **Node Impurity**: Measures how mixed the data in each node is.
- **Impurity Reduction**: How much splitting improves purity compared to the original node.
- **Weighted Stats**: If `sample_weight` assigns more importance to certain samples, those weights are used in the calculations.

---

### **Illustration**

Here’s a diagram of what’s happening:

```
Original Node (Start: 0, End: 5)
--------------------------------
Samples: 1, 2, 3, 4, 5
Impurity: High (Mix of cats and dogs)

Split on Weight < 6.0:
--------------------------------
Left Node (Start: 0, Pos: 2): [1, 2] -> Pure (Cats only)
Right Node (Pos: 3, End: 5): [3, 5] -> Pure (Dogs only)
Missing Data: [4] -> Depends on `missing_go_to_left`.

Statistics:
- Left Node Impurity: 0.0
- Right Node Impurity: 0.0
- Impurity Reduction: Significant
```

The criterion determines whether this split (or another split) gives the best reduction in impurity.

---

### **Why is This Useful?**

The `Criterion` class handles the math and bookkeeping for each split:
1. It keeps track of which samples go where.
2. It calculates impurity and the benefit of the split.
3. It helps the decision tree algorithm pick the best split for each node.

Without these calculations, it would be hard to automatically decide how to split the data in the most meaningful way.

To understand why **means** are used for regression and **probabilities** for classification when deciding whether a split is useful, let’s break this down with examples.

---

### **The Purpose of Splitting in Decision Trees**

When building a decision tree:
- We repeatedly split the dataset into two groups (left and right nodes) based on some feature.
- The goal is to make these groups (nodes) as "pure" as possible:
  - In **regression**, this means minimizing the variability of the target values (y-values) in each node.
  - In **classification**, this means increasing the likelihood of a single class dominating each node.

The "usefulness" of a split is determined by how much it improves this purity, measured using **statistics** like means (for regression) or probabilities (for classification).

---

### **Regression: Using Means**

In regression, the target variable \( y \) is continuous (e.g., house prices, temperatures). After a split:
- Each node contains a group of \( y \)-values.
- We calculate the **mean** of the \( y \)-values in each node, as it represents the "center" of the data in that node.

#### **Why the Mean?**
- If the data in each node is tightly clustered around the mean, the node is "pure."
- The **variance** or **sum of squared errors (SSE)**, calculated relative to the mean, measures this purity:
  \[
  \text{SSE} = \sum_{i=1}^n (y_i - \bar{y})^2
  \]
  - Smaller SSE = More useful split.

#### **Example: House Prices**

Imagine a dataset with house prices (\( y \)) and square footage (\( x \)):

| Square Footage (x) | Price (y) |
|---------------------|-----------|
| 1000               | 200,000   |
| 1200               | 220,000   |
| 1500               | 240,000   |
| 1800               | 300,000   |
| 2000               | 350,000   |

We split on \( x = 1500 \), creating two groups:
- Left node (\( x \leq 1500 \)): \( y = [200,000, 220,000, 240,000] \), mean = \( 220,000 \)
- Right node (\( x > 1500 \)): \( y = [300,000, 350,000] \), mean = \( 325,000 \)

Calculate SSE:
- Left node: \( (200,000 - 220,000)^2 + (220,000 - 220,000)^2 + (240,000 - 220,000)^2 = 800,000,000 \)
- Right node: \( (300,000 - 325,000)^2 + (350,000 - 325,000)^2 = 1,250,000,000 \)

If this split reduces overall SSE compared to the parent node (no split), it’s considered useful.

---

### **Classification: Using Probabilities**

In classification, the target variable \( y \) is categorical (e.g., class labels like "cat" or "dog"). After a split:
- Each node contains a group of samples with different class labels.
- We calculate the **probability distribution** of the classes in each node.

#### **Why Probabilities?**
- A node is "pure" if most (or all) samples belong to one class, meaning one probability dominates.
- We use measures like **Gini Impurity** or **Entropy**, based on the class probabilities, to evaluate purity.

##### **Gini Impurity:**
\[
G = 1 - \sum_{k=1}^C p_k^2
\]
Where \( p_k \) is the probability of class \( k \).

##### **Entropy:**
\[
H = - \sum_{k=1}^C p_k \log(p_k)
\]
- Lower Gini/Entropy = More useful split.

#### **Example: Animal Classification**

Imagine a dataset with animals (\( y \)) and weight (\( x \)):

| Weight (x) | Class (y) |
|------------|-----------|
| 10         | Dog       |
| 12         | Dog       |
| 15         | Dog       |
| 50         | Cat       |
| 55         | Cat       |

We split on \( x = 20 \), creating two groups:
- Left node (\( x \leq 20 \)): \( y = [Dog, Dog, Dog] \), probabilities = \( [1, 0] \) (100% Dog, 0% Cat)
- Right node (\( x > 20 \)): \( y = [Cat, Cat] \), probabilities = \( [0, 1] \) (0% Dog, 100% Cat)

**Gini Impurity:**
- Left node: \( G = 1 - (1^2 + 0^2) = 0 \) (pure).
- Right node: \( G = 1 - (0^2 + 1^2) = 0 \) (pure).

This split perfectly separates the classes, so it’s very useful.

---

### **Comparison: Regression vs. Classification**

| Regression                           | Classification                       |
|--------------------------------------|--------------------------------------|
| Target variable is continuous (\( y \)) | Target variable is categorical (\( y \)) |
| Measure "purity" using variance or SSE | Measure "purity" using class probabilities |
| Use the **mean** of \( y \) in each node | Use **probabilities** of each class in each node |
| Example: House prices                | Example: Dog vs. Cat classification |

---

### **Summary**

- **Means for Regression:** The mean represents the central value, and the split's quality is based on how well the values cluster around their means.
- **Probabilities for Classification:** Probabilities describe the class distribution, and the split's quality is based on how well the classes are separated.

These measures help decision trees decide whether a split improves the model's ability to predict outcomes.
