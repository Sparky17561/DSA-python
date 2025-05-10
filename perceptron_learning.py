import numpy as np

def get_input():
    x1, x2 = [], []
    print("\nEnter 4 input values for x1 and x2:")
    for i in range(4):
        x1.append(int(input(f'Enter x1[{i + 1}]: ')))
        x2.append(int(input(f'Enter x2[{i + 1}]: ')))
    return np.array(x1), np.array(x2)

def perceptron_learning(x1, x2, t, alpha, threshold, epochs):
    w1 = w2 = b = 0

    def output(yin):
        return 1 if yin >= threshold else 0

    for epoch in range(epochs):
        print(f'\nEpoch {epoch + 1}')
        print(f'X1\tX2\tT\tYin\tY\tW1\tW2\tB')
        print('-' * 60)

        for i in range(4):
            yin = x1[i] * w1 + x2[i] * w2 + b
            op = output(yin)
            if op != t[i]:
                w1 += alpha * x1[i] * t[i]
                w2 += alpha * x2[i] * t[i]
                b += alpha * t[i]

            print(f'{x1[i]}\t{x2[i]}\t{t[i]}\t{yin:.2f}\t{op}\t{w1}\t{w2}\t{b}')

# Main program
gates = {
    "AND": [0, 0, 0, 1],
    "OR": [0, 1, 1, 1]
}

selected_gate = input("Enter gate (AND/OR): ").upper()

if selected_gate in gates:
    x1, x2 = get_input()
    alpha = float(input("Enter learning rate (alpha): "))
    threshold = float(input("Enter threshold value: "))
    epochs = int(input("Enter number of epochs: "))
    print(f"\nPerceptron Learning for {selected_gate} Gate")
    perceptron_learning(x1, x2, gates[selected_gate], alpha, threshold, epochs)
else:
    print("Invalid gate selection.")
