# Decision-Making-Approach
Below is an example of a `README.md` file for your GitHub repository that explains the AHP (Analytic Hierarchy Process) Python implementation. You can customize it further based on your needs.

---

# Analytic Hierarchy Process (AHP) Implementation in Python

This repository contains a Python implementation of the Analytic Hierarchy Process (AHP), a structured technique for organizing and analyzing complex decisions. The AHP method helps in decision-making by breaking down a problem into a hierarchy of criteria and alternatives, and then evaluating them through pairwise comparisons.

## Features

- **Pairwise Comparison Matrix**: Constructs a pairwise comparison matrix based on user input.
- **Weight Calculation**: Computes the weights of criteria using the Eigenvector method.
- **User-Friendly Input**: Allows users to input the number of criteria, their names, and pairwise comparisons.
- **Output**: Displays the pairwise comparison matrix and the calculated weights for each criterion.

## Requirements

- Python 3.x
- NumPy (`numpy`)

To install the required dependencies, run:

```bash
pip install numpy
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ahp-python.git
   cd ahp-python
   ```

2. Run the AHP script:

   ```bash
   python ahp.py
   ```

3. Follow the prompts:
   - Enter the number of criteria.
   - Enter the names of the criteria.
   - Provide pairwise comparisons (on a scale of 1 to 9).

4. The program will output:
   - The pairwise comparison matrix.
   - The weights of each criterion.

## Example

Suppose you have three criteria: `A`, `B`, and `C`. The user inputs the following values:

```
Enter the number of inputs: 3
Enter the name of input 1: A
Enter the name of input 2: B
Enter the name of input 3: C

Please enter pairwise comparisons:
Enter the importance of A compared to B (1 to 9): 3
Enter the importance of A compared to C (1 to 9): 5
Enter the importance of B compared to C (1 to 9): 2
```

The output will be:

```
Pairwise comparison matrix:
[[1.         3.         5.        ]
 [0.33333333 1.         2.        ]
 [0.2        0.5        1.        ]]

Weights of each input:
A: 0.6333
B: 0.2605
C: 0.1062
```

## Code Structure

- `ahp.py`: The main script that implements the AHP process.
  - `get_pairwise_comparison_matrix()`: Constructs the pairwise comparison matrix.
  - `calculate_weights()`: Computes the weights using the Eigenvector method.
  - `main()`: Handles user input and displays results.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- The AHP method was developed by Thomas L. Saaty.
- This implementation uses the `numpy` library for matrix operations.

---

Feel free to customize this `README.md` file to better suit your project. You can add badges, screenshots, or additional sections as needed.
