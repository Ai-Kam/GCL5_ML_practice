import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

#(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
print(x_train.shape)

#plt.imshow(x_train[1])
#plt.show()

x_train, x_test = x_train / 255.0, x_test / 255.0

models = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(10, activation='softmax')
])

models.summary()

models.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

history = models.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test), batch_size=256)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

