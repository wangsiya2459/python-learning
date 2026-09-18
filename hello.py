import numpy as np


class Loss:
    def __call__(self, y_pred, y_true):
        return np.mean((y_pred - y_true) ** 2)


class GradientDescent:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def step(self, w, b, x, y):
        y_pred = w * x + b

        # 计算梯度,m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        dw = np.mean(2 * x * (y_pred - y))
        db = np.mean(2 * (y_pred - y))

        # 更新参数
        w = w - self.learning_rate * dw
        b = b - self.learning_rate * db

        return w, b
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

w = 0
b = 0

loss = Loss()
optimizer = GradientDescent(learning_rate=0.01)

for epoch in range(1000):
    w, b = optimizer.step(w, b, x, y)

    y_pred = w * x + b
    current_loss = loss(y_pred, y)

    if epoch % 100 == 0:
        print(epoch, current_loss)

print("w =", w)
print("b =", b)