from audioop import bias
import math
import numpy as np
accuracyList = []

class Neural_Network:
    # Initialize the network
    def __init__(self, num_inputs, num_hidden, num_outputs, hidden_layer_weights, output_layer_weights, learning_rate, hidden_bias, output_bias):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        self.hidden_layer_weights = hidden_layer_weights
        self.output_layer_weights = output_layer_weights

        self.learning_rate = learning_rate
        self.hidden_bias = hidden_bias
        self.output_bias = output_bias

    # Calculate neuron activation for an input
    def sigmoid(self, input):
        return 1./(1. + math.e**(input * -1.))


    # Feed forward pass input to a network output
    def forward_pass(self, inputs):
        hidden_layer_outputs = []
        for i in range(self.num_hidden):
            weighted_sum = 0.
            # TODO! Calculate the weighted sum, and then compute the final output.
            for j in range(self.num_inputs):
                weighted_sum += inputs[j] * self.hidden_layer_weights[j,i] + self.hidden_bias[i]
            output = self.sigmoid(weighted_sum)

            hidden_layer_outputs.append(output)
        output_layer_outputs = []
        for i in range(self.num_outputs):
            weighted_sum = 0.
            for j in range (self.num_hidden):
                weighted_sum += hidden_layer_outputs[j] * self.output_layer_weights[j,i] + self.output_bias[i]
            # TODO! Calculate the weighted sum, and then compute the final output.
            output = self.sigmoid(weighted_sum)
            output_layer_outputs.append(output)

        return hidden_layer_outputs, output_layer_outputs

    # Backpropagate error and store in neurons
    def backward_propagate_error(self, inputs, hidden_layer_outputs, output_layer_outputs, desired_outputs):

        output_layer_betas = np.zeros(self.num_outputs)
        # TODO! Calculate output layer betas.
        for i in range(self.num_outputs):
            output_layer_betas[i] = desired_outputs[i]- output_layer_outputs[i]
        print('OL betas: ', output_layer_betas)

        hidden_layer_betas = np.zeros(self.num_hidden)
        # TODO! Calculate hidden layer betas.
        for i in range(self.num_hidden):
            for j in range(self.num_outputs):
                hidden_layer_betas[i] += self.output_layer_weights[i,j] * output_layer_outputs[j] * (1-output_layer_outputs[j]) * output_layer_betas[j]
        print('HL betas: ', hidden_layer_betas)

        # This is a HxO array (H hidden nodes, O outputs)
        delta_output_layer_weights = np.zeros((self.num_hidden, self.num_outputs))
        # TODO! Calculate output layer weight changes.
        for i in range(self.num_outputs):
            for j in range(self.num_hidden):
                delta_output_layer_weights[j,i] = self.learning_rate * hidden_layer_outputs[j] * output_layer_outputs[i] * (1-output_layer_outputs[i]) * output_layer_betas[i]
        # This is a IxH array (I inputs, H hidden nodes)
        delta_hidden_layer_weights = np.zeros((self.num_inputs, self.num_hidden))
        # TODO! Calculate hidden layer weight changes.
        for i in range(self.num_hidden):
            for j in range(self.num_inputs):
                delta_hidden_layer_weights[j,i] = self.learning_rate * inputs[j] * hidden_layer_outputs[i] * (1-hidden_layer_outputs[i]) * hidden_layer_betas[i]
        # Return the weights we calculated, so they can be used to update all the weights.
        return delta_output_layer_weights, delta_hidden_layer_weights, hidden_layer_betas, output_layer_betas

    def update_bias(self, hidden_layer_outputs, output_layer_outputs, hidden_layer_betas, output_layer_betas):
        for i in range(self.num_hidden):
            self.hidden_bias[i] += (self.learning_rate * hidden_layer_outputs[i] * (1-hidden_layer_outputs[i]) * hidden_layer_betas[i])
        for i in range(self.num_outputs):
            self.output_bias[i] += (self.learning_rate * output_layer_outputs[i] * (1-output_layer_outputs[i]) * output_layer_betas[i])


    def update_weights(self, delta_output_layer_weights, delta_hidden_layer_weights):
        for i in range(self.num_inputs):
            for j in range(self.num_hidden):
                self.hidden_layer_weights[i,j] += delta_hidden_layer_weights[i,j] 

        for i in range(self.num_hidden):
            for j in range(self.num_outputs):
                self.output_layer_weights[i,j] += delta_output_layer_weights[i,j] 
        # TODO! Update the weights.

    def train(self, instances, desired_outputs, epochs, integer_encoded):
        for epoch in range(epochs):
            print('epoch = ', epoch)
            predictions = []
            for i, instance in enumerate(instances):
                hidden_layer_outputs, output_layer_outputs = self.forward_pass(instance)
                delta_output_layer_weights, delta_hidden_layer_weights, hidden_layer_betas, output_layer_betas = self.backward_propagate_error(
                    instance, hidden_layer_outputs, output_layer_outputs, desired_outputs[i])
                predicted_class = output_layer_outputs.index(max(output_layer_outputs))
                predictions.append(predicted_class)

                # We use online learning, i.e. update the weights after every instance.
                self.update_weights(delta_output_layer_weights, delta_hidden_layer_weights)
                self.update_bias(hidden_layer_outputs, output_layer_outputs, hidden_layer_betas, output_layer_betas)

            # Print new weights
            print('Hidden layer weights \n', self.hidden_layer_weights)
            print('Output layer weights  \n', self.output_layer_weights)

            # TODO: Print accuracy achieved over this epoch
            accuracy=0   
            for i in range(len(predictions)):
                if str(predictions[i]) in str(integer_encoded[i]):
                    accuracy+=1
            accuracyList.append(accuracy)
            print('acc = ', accuracy)
            print("Accuracy is",accuracy,"/",len(instances)," which is ",accuracy/len(instances),"%")

    def predict(self, instances):
        predictions = []
        for instance in instances:
            hidden_layer_outputs, output_layer_outputs = self.forward_pass(instance)
            predicted_class = output_layer_outputs.index(max(output_layer_outputs))
            predictions.append(predicted_class)
        return predictions
    def getPredictionList(self):
        return accuracyList