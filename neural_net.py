import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense


def categorical_to_binary(df, key):
    dummies = pd.get_dummies(df[key])
    for col in dummies:
        df[col] = dummies[col]
    del(df[key])


def scale_dataset(dataframe):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(dataframe)
    return pd.DataFrame(scaled, columns=dataframe.columns)


def split_train_test(dataset, ratio=0.8):
    np.random.seed(0)
    train_size = int(ratio * len(dataset))
    values = dataset.values
    np.random.shuffle(values)

    train_x = np.array([v[:-3] for v in values[:train_size-1]])
    test_x = np.array([v[:-3] for v in values[train_size:]])

    train_y = np.array([v[:-4:-1] for v in values[:train_size-1]])
    test_y = np.array([v[:-4:-1] for v in values[train_size:]])

    return train_x, train_y, test_x, test_y


def create_model(input_shape):
    model = Sequential()
    model.add(Dense(50, input_shape=input_shape))
    model.add(Dense(30, activation='sigmoid'))
    model.add(Dense(10, activation='sigmoid'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    return model


def create_dataset():
    #load dataset
    dataframe = pd.read_csv('abalone_dataset.csv')

    #one-hot encoding on categorical field (Sex)
    categorical_to_binary(dataframe, 'sex')

    #scale features between 0 and 1
    scaled = scale_dataset(dataframe)

    #split dataset in train and test
    return split_train_test(scaled)


if __name__ == '__main__':
    train_x, train_y, test_x, test_y = create_dataset()
    model = create_model((8,))

    hist = model.fit(train_x, train_y, epochs=30,
                     validation_data=(test_x, test_y))

    #plot training and test loss history
    plt.figure()
    plt.title('Loss history')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.plot(hist.history['loss'], label='train')
    plt.plot(hist.history['val_loss'], label='test')
    plt.legend()


    #plot training and test accuracy history
    plt.figure()
    plt.title('Accuracy history')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.plot(hist.history['acc'], label='train')
    plt.plot(hist.history['val_acc'], label='test')
    plt.legend()
    plt.show()
