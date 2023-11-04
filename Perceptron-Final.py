{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Input the following things : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#x_0 = [w0,w1,w2]\n",
    "w_0 = [-18,9,-3]\n",
    "l_rate = 0.1\n",
    "#Point above the hyperplane - check notes\n",
    "class_1_pt = [(3,2)]\n",
    "#Point below the hyperplane\n",
    "class_2_pt = [(0,-5)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_graph(weight):\n",
    "    import matplotlib.pyplot as plt\n",
    "    x_list = []\n",
    "    y_list = []\n",
    "    for i in range(-7,7) :\n",
    "        x_list.append(i)\n",
    "        j = (-weight[0] - (weight[1]*i)) / weight[2]\n",
    "        y_list.append(j)\n",
    "    print(\"Points on the line are :\")\n",
    "    print(\"\\tFor x = 0, y is \", ((-weight[0])/ weight[2]))\n",
    "    print(\"\\tFor y = 0, x is \", ((-weight[0])/ weight[1]))\n",
    "    print(x_list)\n",
    "    print(y_list)\n",
    "    plt.plot(x_list,y_list)\n",
    "    plt.grid()\n",
    "    plt.xlim(-7, 7)\n",
    "    plt.ylim(-7, 7)\n",
    "    \n",
    "\n",
    "    plt.arrow(x_list[5],y_list[5],2,2, head_width=0.5, head_length=0.7, fc='lightblue', ec='black')\n",
    "\n",
    "    for every_point in class_1_pt:\n",
    "        plt.scatter(every_point[0],every_point[1],c='#d62728')\n",
    "    for every_point in class_2_pt:\n",
    "        plt.scatter(every_point[0],every_point[1],c='#1f77b4')\n",
    "\n",
    "        \n",
    "def predict(row, weights):\n",
    "    activation = weights[0]\n",
    "    for i in range(len(row)):\n",
    "        activation += weights[i + 1] * row[i]\n",
    "    return 1.0 if activation >= 0.0 else -1.0\n",
    "\n",
    "def train_weights(weights, points, l_rate):\n",
    "    w_1 = [0,0,0]\n",
    "    for every_point in points:\n",
    "        prediction = predict(every_point, weights)\n",
    "        print(\"For point\", every_point, \"sign is\", prediction)\n",
    "        w_1[0] = w_1[0] + (prediction*l_rate)\n",
    "        w_1[1] = w_1[1] + (prediction*l_rate*every_point[0])\n",
    "        w_1[2] = w_1[2] + (prediction*l_rate*every_point[1])\n",
    "    return w_1\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Points on the line are :\n",
      "\tFor x = 0, y is  -6.0\n",
      "\tFor y = 0, x is  2.0\n",
      "[-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]\n",
      "[-27.0, -24.0, -21.0, -18.0, -15.0, -12.0, -9.0, -6.0, -3.0, -0.0, 3.0, 6.0, 9.0, 12.0]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_graph(w_0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For point (3, 2) sign is 1.0\n",
      "For point (0, -5) sign is -1.0\n",
      "NEW 'w' is : [-18.0, 8.7, -3.7]\n"
     ]
    }
   ],
   "source": [
    "weights_1 = train_weights(w_0, class_1_pt, l_rate)\n",
    "weights_2 = train_weights(w_0, class_2_pt, l_rate)\n",
    "w_new = [w_0[0]-weights_1[0]-weights_2[0], w_0[1]-weights_1[1]-weights_2[1], w_0[2]-weights_1[2]-weights_2[2]]\n",
    "print(\"NEW 'w' is :\", w_new)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Points on the line are :\n",
      "\tFor x = 0, y is  -4.864864864864865\n",
      "\tFor y = 0, x is  2.0689655172413794\n",
      "[-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]\n",
      "[-21.32432432432432, -18.97297297297297, -16.62162162162162, -14.270270270270268, -11.918918918918918, -9.567567567567567, -7.216216216216216, -4.864864864864865, -2.5135135135135136, -0.16216216216216253, 2.1891891891891886, 4.5405405405405395, 6.891891891891891, 9.243243243243242]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_graph(w_new)"
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
