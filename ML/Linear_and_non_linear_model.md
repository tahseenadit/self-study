### What is a Decision Tree?

A **Decision Tree** is like a flowchart where:
- You start at the top (the root) and ask a series of **yes/no questions**.
- Depending on the answer, you go down a different branch of the tree until you reach a final decision at the bottom (the leaf node).

Each question in a decision tree usually checks if a feature (e.g., age, height, price) is **greater than** or **less than** some value.

### What is a Linear Model?

A **Linear Model** (like linear regression) works by drawing a **straight line** (or a flat plane in higher dimensions) to predict the output. It assumes the relationship between the input (e.g., features like age, price) and the output (e.g., house price, pass/fail) is a **straight line**.

- If you change the input slightly, the output changes in a smooth, proportional way.
- **Linear models** are all about simple relationships that can be drawn with straight lines.

### Now, Why is a Decision Tree **Non-Linear**?

A **non-linear model** means that the relationship between the input and the output can be more complicated than just a straight line. Here’s why the decision tree is non-linear:

1. **Piecewise Decisions**:
   - Imagine you want to predict if a house is expensive. The decision tree could ask, "Is the size of the house bigger than 2000 sq ft?" If the answer is yes, it might check another feature like "Is the house in an expensive area?"
   - At each step, the decision tree **splits the data into parts** based on a question.
   - This creates a **non-smooth**, step-like behavior. The tree doesn’t gradually move from one price range to another; it jumps from one decision to the next.

2. **Irregular Boundaries**:
   - Unlike a straight line, a decision tree can make **jagged, irregular boundaries**. For example:
     - If you’re classifying fruits as "apples" or "oranges," a decision tree might first ask about the color and then the size.
     - It’s like dividing a piece of paper with a lot of **zigzag lines** rather than one clean, straight line.

3. **Complex Relationships**:
   - Let’s say you want to predict whether someone will pass a class. Maybe both the number of hours they studied and the quality of their sleep are important, but there’s no clear, simple rule that connects them directly.
   - A decision tree can handle these **complex interactions** between features by asking different questions for different cases. A linear model, on the other hand, would try to fit everything into one straight rule (like "more study hours = better performance"), which might not always work.

### Example:

Let’s compare a simple **linear** vs **non-linear** example:

1. **Linear Example**:
   - Imagine you have data on the price of ice cream based on temperature.
   - A linear model might say, "For every 1 degree increase in temperature, the price of ice cream increases by $1."
   - This is a simple straight-line relationship.

2. **Non-linear Example (Decision Tree)**:
   - A decision tree might say:
     - "If the temperature is more than 20°C, then if it's a weekend, the price is $5."
     - "If the temperature is less than 20°C, then the price is $2."
   - Notice how this doesn’t follow a smooth rule. The output **jumps** from one value to another depending on the conditions.

### Key Points:

- **Linear models** make predictions by drawing straight lines. They assume that if you change the input a little, the output will change smoothly.
- **Decision Trees** split the data into pieces, creating complex, jagged decision boundaries. The output changes in steps based on the questions it asks, making it **non-linear**.
  
This ability to handle more complex situations without needing straight-line assumptions is why decision trees are **non-linear models**.
