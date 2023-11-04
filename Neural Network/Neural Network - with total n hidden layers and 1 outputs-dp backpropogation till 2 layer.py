{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Note\n",
    "BackPropogation work for every layer, but was not verified beyond 2 layer back propogation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the input neurons (seprated by ',') : 0.3,0.4\n",
      "Enter the number of hidden layer: 2\n",
      "Enter the activation function (s for sigmoid, r for relu, lr for leaky relu) : s\n",
      "Enter the learning rate : 0.7\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "Input_layer = [float(item) for item in input(\"Enter the input neurons (seprated by ',') : \").split(',')]\n",
    "n_hidden_layers = int(input(\"Enter the number of hidden layer: \"))\n",
    "Func_type = input(\"Enter the activation function (s for sigmoid, r for relu, lr for leaky relu) : \")\n",
    "learning_rate = float(input(\"Enter the learning rate : \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def activation_func(input,type):\n",
    "    if(type == \"s\"):\n",
    "        out = (1/(1+np.exp(-input)))\n",
    "    elif(type == \"r\"):\n",
    "        out = max(0,input)\n",
    "    elif(type == \"lr\"):\n",
    "        out = max(0.01,input)\n",
    "    return out"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def der_activation_func(input,type):\n",
    "    if(type == \"s\"):\n",
    "        out = input*(1-input)\n",
    "        print(\"\\tder 2 =\", str(input), \"*(1 -\", str(input),\") = \", out)\n",
    "    elif(type == \"r\"):\n",
    "        if(input>0) :\n",
    "            out = 1\n",
    "            print(\"\\tder 2 ->\", str(input),\"is > 0 , therefore =\", out)\n",
    "        else :\n",
    "            out = 0\n",
    "            print(\"\\tder 2 -> input is <= 0 , therefore = 0\")\n",
    "    elif(type == \"lr\"):\n",
    "        if(input>0) :\n",
    "            out = 1*0.01\n",
    "            print(\"\\tder 2 ->\", str(input),\"is > 0 , therefore =\", str(input), \"*0.01=\", out)\n",
    "        else :\n",
    "            out = 0\n",
    "            print(\"\\tder 2 -> input is <= 0 , therefore = 0\")\n",
    "    return out"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#making 3 dictionaries to store the weights, netoutput(without actication) and output(with actication function)\n",
    "weights = dict()\n",
    "weights_netoutput = dict()\n",
    "weights_output = dict()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hidden Layer : 1\n",
      "Enter the number of neuron in this hidden layer : 1\n",
      "\tNeuron : 1\n",
      "\tEnter the Bias for neuron : 0.33\n",
      "\t\tFor weight from neuron 1\n",
      "\t\tEnter the weight name: w1\n",
      "\t\tEnter the weight : 0.5\n",
      "\t\tFor weight from neuron 2\n",
      "\t\tEnter the weight name: w2\n",
      "\t\tEnter the weight : 0.1\n",
      "\tActivation function of  + 0.15 + 0.04000000000000001 + 0.33 (Net H 1 _ 1 ) = 0.52 is : (Out H 1 ) 0.6271477663131956\n",
      "*****************************************************\n",
      "[0.6271477663131956]\n",
      "===========================================================================\n",
      "Hidden Layer : 2\n",
      "Enter the number of neuron in this hidden layer : 1\n",
      "\tNeuron : 1\n",
      "\tEnter the Bias for neuron : 0.1\n",
      "\t\tFor weight from neuron 1\n",
      "\t\tEnter the weight name: w3\n",
      "\t\tEnter the weight : 0.85\n",
      "\tActivation function of  + 0.5330756013662162 + 0.1 (Net H 1 _ 2 ) = 0.6330756013662162 is : (Out H 1 ) 0.6531865179983487\n",
      "*****************************************************\n",
      "[0.6531865179983487]\n",
      "===========================================================================\n"
     ]
    }
   ],
   "source": [
    "y = Input_layer.copy()\n",
    "for every_layer in range(n_hidden_layers):\n",
    "    y_new = []\n",
    "    print(\"Hidden Layer :\", every_layer+1)\n",
    "    n_layer = int(input(\"Enter the number of neuron in this hidden layer : \"))\n",
    "    for neuron in range(n_layer) :\n",
    "        g = 0\n",
    "        string = \"\"\n",
    "        print(\"\\tNeuron :\", neuron+1)\n",
    "        bias = float(input(\"\\tEnter the Bias for neuron : \"))\n",
    "        for n in range(len(y)) :\n",
    "            print(\"\\t\\tFor weight from neuron\", n+1)\n",
    "            weight_name = input(\"\\t\\tEnter the weight name: \")\n",
    "            weight = float(input(\"\\t\\tEnter the weight : \"))\n",
    "            weights[weight_name] = weight\n",
    "            weights_netoutput[weight_name] = 'na'\n",
    "            weights_output[weight_name] = 'na'\n",
    "            g = g +  (weight*y[n])\n",
    "            string = string + \" + \" + str((weight*y[n]))\n",
    "        g = g + bias\n",
    "        string = string + \" + \" + str(bias)\n",
    "        ac = activation_func(g,Func_type)\n",
    "        for key in weights_netoutput.keys():\n",
    "            if weights_netoutput[key] == 'na':\n",
    "                weights_netoutput[key] = g\n",
    "        for key in weights_output.keys():\n",
    "            if weights_output[key] == 'na':\n",
    "                weights_output[key] = ac\n",
    "        print(\"\\tActivation function of\", string, \"(Net H\",neuron+1,\"_\",every_layer+1,\") =\" , g, \"is : (Out H\",neuron+1,\")\", ac)\n",
    "        y_new.append(ac)\n",
    "        print(\"*****************************************************\")\n",
    "    y = y_new.copy() \n",
    "    print(y_new)\n",
    "    print(\"===========================================================================\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of neuron in the output layer : 1\n",
      "\tNeuron : 1\n",
      "\tEnter the Bias for neuron : 0\n",
      "\t\tFor weight from neuron 1\n",
      "\t\tEnter the weight name: w4\n",
      "\t\tEnter the weight : 0.45\n",
      "\tActivation function of  + 0.2939339330992569 + 0.0 (Net O 1 ) = 0.2939339330992569 is : (Out O 1 ) 0.5729589509490358\n",
      "*****************************************************\n",
      "The Output is:  [0.5729589509490358]\n",
      "===========================================================================\n"
     ]
    }
   ],
   "source": [
    "o_layer = int(input(\"Enter the number of neuron in the output layer : \"))\n",
    "y_new = []\n",
    "for neuron in range(o_layer) :\n",
    "    g = 0\n",
    "    string = \"\"\n",
    "    print(\"\\tNeuron :\", neuron+1)\n",
    "    bias = float(input(\"\\tEnter the Bias for neuron : \"))\n",
    "    for n in range(len(y)) :\n",
    "        print(\"\\t\\tFor weight from neuron\", n+1)\n",
    "        weight_name = input(\"\\t\\tEnter the weight name: \")\n",
    "        weight = float(input(\"\\t\\tEnter the weight : \"))\n",
    "        weights[weight_name] = weight\n",
    "        weights_netoutput[weight_name] = 'na'\n",
    "        weights_output[weight_name] = 'na'\n",
    "        g = g +  (weight*y[n])\n",
    "        string = string + \" + \" + str((weight*y[n]))\n",
    "    g = g + bias\n",
    "    string = string + \" + \" + str(bias)\n",
    "    ac = activation_func(g,Func_type)\n",
    "    for key in weights_netoutput.keys():\n",
    "        if weights_netoutput[key] == 'na':\n",
    "            weights_netoutput[key] = g\n",
    "    for key in weights_output.keys():\n",
    "        if weights_output[key] == 'na':\n",
    "            weights_output[key] = ac\n",
    "    print(\"\\tActivation function of\", string, \"(Net O\",neuron+1,\") =\" , g, \"is : (Out O\",neuron+1,\")\", ac)\n",
    "    y_new.append(ac)\n",
    "    print(\"*****************************************************\")\n",
    "y = y_new.copy() \n",
    "print(\"The Output is: \", y_new)\n",
    "print(\"===========================================================================\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Output Neuron O: 1\n",
      "Enter the target output : 0.01\n",
      "Error is : 0.15846139022681946\n",
      "total Error is : 0.15846139022681946\n",
      "************************\n",
      "{'w1': 0.5, 'w2': 0.1, 'w3': 0.85, 'w4': 0.45}\n",
      "{'w1': 0.52, 'w2': 0.52, 'w3': 0.6330756013662162, 'w4': 0.2939339330992569}\n",
      "{'w1': 0.6271477663131956, 'w2': 0.6271477663131956, 'w3': 0.6531865179983487, 'w4': 0.5729589509490358}\n"
     ]
    }
   ],
   "source": [
    "Error_total = 0\n",
    "for n in range(len(y)) :\n",
    "    print(\"Output Neuron O:\", n+1)\n",
    "    target_output = float(input(\"Enter the target output : \"))\n",
    "    error = 0.5* pow((target_output - y[n]),2)\n",
    "    print(\"Error is :\" , error)\n",
    "    Error_total = Error_total + error\n",
    "print(\"total Error is :\", Error_total)\n",
    "print(\"************************\")\n",
    "print(weights)\n",
    "print(weights_netoutput)\n",
    "print(weights_output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "back Propogation\n",
      "Gradient discent of weights linked to output layer\n",
      "Enter the no. of weights linked to output layer: 1\n",
      "\tFor weight: w4\n",
      "\tEnter the target output from this weight: 0.01\n",
      "\tder 1 = -1 * ( 0.01 - 0.5729589509490358 )\n",
      "\tder 2 = 0.5729589509490358 *(1 - 0.5729589509490358 ) =  0.2446769914764162\n",
      "\tEnter the weight name for any previous weight directly linked to this weight: w3\n",
      "\tder 3 =  0.6531865179983487\n",
      "\tGradient discent for this weight is :  0.5629589509490358 * 0.2446769914764162 * 0.6531865179983487 = 0.08997193746298693\n",
      "\tNew weight is : 0.38701964377590914\n",
      "\t**************************************************\n",
      "=================================================================\n",
      "Gradient discent of weights linked hidden layer 1\n",
      "Enter the no. of weights linked between previous layer to this layers: 1\n",
      "For weight: w3\n",
      "Enter the weight linked to output1: w4\n",
      "Enter the output10.01\n",
      "DER1 0.5629589509490358\n",
      "\tder 2 = 0.5729589509490358 *(1 - 0.5729589509490358 ) =  0.2446769914764162\n",
      "DER1 0.2446769914764162\n",
      "DER1 0.45\n",
      "0.06198439609931825\n",
      "\tder 2 = 0.6531865179983487 *(1 - 0.6531865179983487 ) =  0.2265338907035416\n",
      "\t\tEnter the weight name for any previous weight directly linked to this weight: w1\n",
      "der 3 =  0.6271477663131956\n",
      "Gradient discent for this weight is :  0.06198439609931825 * 0.2265338907035416 * 0.6271477663131956 = 0.008806137010377657\n",
      "\tNew weight is : 0.8438357040927357\n",
      "\t**************************************************\n",
      "***************************************************\n"
     ]
    }
   ],
   "source": [
    "#calculating gradient discent\n",
    "gradient_discent_lst = dict()\n",
    "new_weight_list = dict()\n",
    "list_weights = sorted(weights, reverse=True)\n",
    "i = 0\n",
    "hidden_layers = range(n_hidden_layers)\n",
    "print(\"back Propogation\")\n",
    "fool = False\n",
    "for layers in sorted(hidden_layers,reverse=True) :\n",
    "    if fool is False :\n",
    "        print(\"Gradient discent of weights linked to output layer\")\n",
    "        n = int(input(\"Enter the no. of weights linked to output layer: \"))        \n",
    "        for key in range(i,n):\n",
    "#            print(key)\n",
    "            print(\"\\tFor weight:\", list_weights[key])\n",
    "            weight = list_weights[key]\n",
    "            out = float(input(\"\\tEnter the target output from this weight: \"))\n",
    "            der_1 = -1 * (out - weights_output[weight])\n",
    "            print(\"\\tder 1 = -1 * (\", str(out), \"-\", str(weights_output[weight]), \")\",)\n",
    "            der_2 = der_activation_func(weights_output[weight],Func_type)\n",
    "            wght_name = input(\"\\tEnter the weight name for any previous weight directly linked to this weight: \")\n",
    "            der_3 = weights_output[wght_name]\n",
    "            print(\"\\tder 3 = \", str(weights_output[wght_name]))\n",
    "            gradient_discent = der_1*der_2*der_3\n",
    "            print(\"\\tGradient discent for this weight is : \",str(der_1),\"*\",str(der_2),\"*\", str(der_3),\"=\", gradient_discent)\n",
    "            gradient_discent_lst[weight] = gradient_discent\n",
    "            new_weight = weights[weight] - (gradient_discent_lst[weight]*learning_rate)\n",
    "            new_weight_list[weight] = new_weight\n",
    "            print(\"\\tNew weight is :\", new_weight)\n",
    "            print(\"\\t**************************************************\") \n",
    "        i = i+n            \n",
    "        fool = True\n",
    "        print(\"=================================================================\") \n",
    "    else : \n",
    "        j=1\n",
    "        print(\"Gradient discent of weights linked hidden layer\", n_hidden_layers-j)\n",
    "        n = int(input(\"Enter the no. of weights linked between previous layer to this layers: \"))\n",
    "#        print(i)\n",
    "#        print(n)\n",
    "        for key in range(i,i+n):\n",
    "#            print(key)\n",
    "            print(\"For weight:\", list_weights[key])\n",
    "            weight = list_weights[key]\n",
    "            wt1 = input(\"Enter the weight linked to output1: \")\n",
    "            out1 = float(input(\"Enter the output1\"))\n",
    "            der_1_1 =  -1 * (out1 - weights_output[wt1])\n",
    "            print(\"DER1\", der_1_1)\n",
    "            der_1_2 = der_activation_func(weights_output[wt1],Func_type)\n",
    "            print(\"DER2\", der_1_2)\n",
    "            der_1_3 = weights[wt1]\n",
    "            print(\"DER3\", der_1_3)\n",
    "            print(der_1_1*der_1_2*der_1_3)\n",
    "            der_1 = (der_1_1*der_1_2*der_1_3)\n",
    "            der_2 = der_activation_func(weights_output[weight],Func_type)\n",
    "            wght_name = input(\"\\t\\tEnter the weight name for any previous weight directly linked to this weight: \") \n",
    "            der_3 = weights_output[wght_name]\n",
    "            print(\"der 3 = \", der_3)\n",
    "            gradient_discent = der_1*der_2*der_3\n",
    "            print(\"Gradient discent for this weight is : \",str(der_1),\"*\",str(der_2),\"*\", str(der_3),\"=\", gradient_discent)\n",
    "            gradient_discent_lst[weight] = gradient_discent\n",
    "            new_weight = weights[weight] - (gradient_discent_lst[weight]*learning_rate)\n",
    "            new_weight_list[weight] = new_weight\n",
    "            print(\"\\tNew weight is :\", new_weight)\n",
    "            print(\"\\t**************************************************\") \n",
    "        i = i+n\n",
    "        j = j+1\n",
    "        print(\"***************************************************\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Gradient discent of weights first hidden layer\", n_hidden_layers-j)\n",
    "n = int(input(\"Enter the no. of weights linked between input layer to this layers: \"))\n",
    "print(i)\n",
    "print(n)\n",
    "for key in range(i,i+n):\n",
    "    print(key)\n",
    "    print(\"For weight:\", list_weights[key])\n",
    "    weight = list_weights[key]\n",
    "    wt1 = input(\"Enter the weight linked to output1: \")\n",
    "    out1 = float(input(\"Enter the output1\"))\n",
    "    der_1_1 =  -1 * (out1 - weights_output[wt1])\n",
    "    print(\"DER1\", der_1_1)\n",
    "    der_1_2 = der_activation_func(weights_output[wt1],Func_type)\n",
    "    print(\"DER1\", der_1_2)\n",
    "    der_1_3 = weights[wt1]\n",
    "    print(\"DER1\", der_1_3)\n",
    "    print(der_1_1*der_1_2*der_1_3)\n",
    "    der_1 = (der_1_1*der_1_2*der_1_3)\n",
    "    der_2 = der_activation_func(weights_output[weight],Func_type)\n",
    "    der_3 = float(input(\"\\t\\tEnter if last layer enter input\")) \n",
    "    print(\"der 3 = \", der_3)\n",
    "    gradient_discent = der_1*der_2*der_3\n",
    "    print(\"Gradient discent for this weight is : \",str(der_1),\"*\",str(der_2),\"*\", str(der_3),\"=\", gradient_discent)\n",
    "    gradient_discent_lst[weight] = gradient_discent\n",
    "    new_weight = weights[weight] - (gradient_discent_lst[weight]*learning_rate)\n",
    "    new_weight_list[weight] = new_weight\n",
    "    print(\"\\tNew weight is :\", new_weight)\n",
    "    print(\"\\t**************************************************\") \n",
    "    i = i+n\n",
    "j = j+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(weights)\n",
    "print(gradient_discent_lst)\n",
    "learning_rate = float(input(\"Enter the learning rate : \"))\n",
    "for key in weights.keys() :\n",
    "    print(key)\n",
    "    new_weight = weights[key] - (gradient_discent_lst[key]*learning_rate)\n",
    "    print(\"for key\", key, \"New weight is \",new_weight)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
