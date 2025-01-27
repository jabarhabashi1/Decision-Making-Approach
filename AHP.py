import numpy as np


def get_pairwise_comparison_matrix(n, names):
    matrix = np.ones((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            value = float(input(f"Enter the importance of {names[i]} compared to {names[j]} (1 to 9): "))
            matrix[i, j] = value
            matrix[j, i] = 1 / value
    return matrix


def calculate_weights(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_index = np.argmax(eigenvalues)
    weights = np.real(eigenvectors[:, max_index])
    weights = weights / np.sum(weights)
    return weights


def main():
    n = int(input("Enter the number of inputs: "))
    names = [input(f"Enter the name of input {i + 1}: ") for i in range(n)]

    print("\nPlease enter pairwise comparisons:")
    pairwise_matrix = get_pairwise_comparison_matrix(n, names)

    print("\nPairwise comparison matrix:")
    print(pairwise_matrix)

    weights = calculate_weights(pairwise_matrix)

    print("\nWeights of each input:")
    for i in range(n):
        print(f"{names[i]}: {weights[i]:.4f}")


if __name__ == "__main__":
    main()