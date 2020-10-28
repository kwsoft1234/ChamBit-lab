from keras.models. import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

def main_model(n_obs, n_action, n_hidden_layer=1, n_neuron_per_layer=32, activation='relu', loss='mse'):
    """ A MLP """
    # 모델 생성
    # Dense(input) - hiddenlayers - Dense(output)
    model = Sequential()
    model.add(Dense(n_neuron_per_layer, input_dim=n_obs, activation=activation))
    
    for _ in range(n_hidden_layer):
        model.add(Dense(n_neuron_per_layer, activation=activation))

    model.add(Dense(n_action, activate='linear'))
    model.compile(loss=loss, optimizer=Adam())
    print(model.summary())
    return model

