{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "tuga2fM9K4-Z"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "DG2Rw-s6K4-Z"
   },
   "outputs": [],
   "source": [
    "# Feature values\n",
    "x1 = np.array([1.1,2.2,2.5,4,5.2,6.1]) # first feature\n",
    "x2 = np.array([1.4,2.1,2.9,5,5.1,6.7]) # second feature\n",
    "assert len(x1) == len(x2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "AA9ZkAmZK4-Z",
    "outputId": "e7548175-e83a-4846-f499-899f576d8138"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.1 1.4]\n",
      " [2.2 2.1]\n",
      " [2.5 2.9]\n",
      " [4.  5. ]\n",
      " [5.2 5.1]\n",
      " [6.1 6.7]]\n"
     ]
    }
   ],
   "source": [
    "# Combine features to data matrix\n",
    "mat = np.array([x1, x2]).transpose()\n",
    "print(mat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 265
    },
    "id": "Gj-_6UOmK4-Z",
    "outputId": "18415e8e-ea3d-4f1d-b494-1c205de5bc60"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
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
    "# Plot the data\n",
    "plt.scatter(mat[:,0], mat[:,1])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ierEJF-WK4-Z",
    "outputId": "10eab763-ee46-4b10-f052-3e05551f2346"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-1.38195552 -1.31932673]\n",
      " [-0.75292749 -0.9449232 ]\n",
      " [-0.58137439 -0.51703345]\n",
      " [ 0.2763911   0.60617714]\n",
      " [ 0.9626035   0.65966336]\n",
      " [ 1.4772628   1.51544286]]\n"
     ]
    }
   ],
   "source": [
    "# Standardize the features\n",
    "mean1 = np.mean(mat[:,0])\n",
    "std1 = np.std(mat[:,0])\n",
    "mean2 = np.mean(mat[:,1])\n",
    "std2 = np.std(mat[:,1])\n",
    "z_mat = np.zeros(mat.shape)\n",
    "z_mat[:,0] = (mat[:,0] - mean1) / std1\n",
    "z_mat[:,1] = (mat[:,1] - mean2) / std2\n",
    "print(z_mat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 265
    },
    "id": "7sJ_Nm2FK4-a",
    "outputId": "08cbe694-8881-49a1-d7d0-44be303ff82b"
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAAD4CAYAAADvsV2wAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAQBElEQVR4nO3dXWhk533H8e+/sgwiBNR05RfJTtaBRdTBJGvE1q6huJBG9lLYjUmCfRMTAotDfCvYxZBAbuxWV03ixizBxLlo3Fys5aVZV3mjODcu1kZx1m6iZus6taTFqySV05ChXm/+vdDI1a71MqM5mrfn+4FB5zzn+Dz/Z571T6NnjkaRmUiS+t8fdboASVJ7GPiSVAgDX5IKYeBLUiEMfEkqxDWdLmA7+/bty/3793e6DEnqGWfPnv1VZo5sdqyrA3///v3Mzc11ugxJ6hkR8cutjrmkI0mFMPAlqRAGviQVwsCXpEIY+JJUiK6+S0eSSjIzv8T07ALLqzVGh4eYmhzn6MGxyq5fySv8iHgyIi5GxMtbHL87It6MiJ/UH1+ool9J6hcz80ucOHWOpdUaCSyt1jhx6hwz80uV9VHVks43gHt2OOdHmfmR+uNLFfUrSX1henaB2qXLV7TVLl1menahsj4qCfzMfB74TRXXkqQSLa/WmmrfjXa+aXtnRLwUEc9FxIe2OikijkXEXETMraystLE8Seqc0eGhptp3o12B/2PgA5n5YeArwMxWJ2bmycycyMyJkZFNPw5CkvrO1OQ4Q4MDV7QNDQ4wNTleWR9tCfzM/G1m/q6+fQYYjIh97ehbknrB0YNjPHrfbYwNDxHA2PAQj953W6V36bTltsyIuAF4IzMzIg6x9o3m1+3oW5J6xdGDY5UG/NUqCfyI+BZwN7AvIhaBLwKDAJn5BPAJ4HMR8TZQA+5P/3q6JLVVJYGfmQ/scPyrwFer6EuStDt+tIIkFcLAl6RCGPiSVAgDX5IKYeBLUiEMfEkqhIEvSYUw8CWpEAa+JBXCwJekQhj4klQIA1+SCmHgS1IhDHxJKoSBL0mFMPAlqRAGviQVwsCXpEIY+JJUCANfkgph4EtSIQx8SSqEgS9JhTDwJakQBr4kFcLAl6RCVBL4EfFkRFyMiJe3OB4R8eWIOB8RP42I26voV5LUuKpe4X8DuGeb4/cCB+qPY8DXKupXktSgSgI/M58HfrPNKUeAb+aaF4DhiLixir4lSY1p1xr+GPD6hv3Fetu7RMSxiJiLiLmVlZW2FCdJJWhX4McmbbnZiZl5MjMnMnNiZGRkj8uSpHK0K/AXgZs37N8ELLepb0kS7Qv808Cn63fr3AG8mZkX2tS3JAm4poqLRMS3gLuBfRGxCHwRGATIzCeAM8Bh4Dzwe+AzVfQrSWpcJYGfmQ/scDyBz1fRlyRpd/xNW0kqhIEvSYUw8CWpEAa+JBXCwJekQhj4klQIA1+SCmHgS1IhDHxJKoSBL0mFMPAlqRAGviQVwsCXpEIY+JJUCANfkgpRyefhS1K7zMwvMT27wPJqjdHhIaYmxzl6cKzTZfUEA19Sz5iZX+LEqXPULl0GYGm1xolT5wAM/Qa4pCOpZ0zPLrwT9utqly4zPbvQoYp6i4EvqWcsr9aaateVXNKRuojr09sbHR5iaZNwHx0e6kA1vcdX+FKXWF+fXlqtkfz/+vTM/FKnS+saU5PjDA0OXNE2NDjA1OR4hyrqLQa+1CVcn97Z0YNjPHrfbYwNDxHA2PAQj953mz8FNcglHalLuD7dmKMHxwz4XfIVvtQltlqHdn1aVTHwpS7h+rT2mks6UpdYX6bwLh3tlUoCPyLuAf4OGAC+npmPXXX8buBZ4D/rTacy80tV9C31E9entZdaDvyIGAAeB/4KWARejIjTmflvV536o8z861b7kyTtThVr+IeA85n5ama+BTwNHKngupKkClUR+GPA6xv2F+ttV7szIl6KiOci4kNbXSwijkXEXETMraysVFCeJAmqCfzYpC2v2v8x8IHM/DDwFWBmq4tl5snMnMjMiZGRkQrKkyRBNYG/CNy8Yf8mYHnjCZn528z8XX37DDAYEfsq6FuS1KAqAv9F4EBE3BIR1wL3A6c3nhARN0RE1LcP1fv9dQV9S5Ia1PJdOpn5dkQ8DMyydlvmk5n5SkQ8VD/+BPAJ4HMR8TZQA+7PzKuXfSRJeyi6OXcnJiZybm6u02VIUs+IiLOZObHZMT9aQZIKYeBLUiEMfEkqhIEvSYUw8CWpEAa+JBXCwJekQhj4klQIA1+SCmHgS1IhDHxJKoSBL0mFMPAlqRAGviQVwsCXpEIY+JJUCANfkgph4EtSIQx8SSqEgS9JhTDwJakQBr4kFcLAl6RCGPiSVAgDX5IKYeBLUiEqCfyIuCciFiLifEQc3+R4RMSX68d/GhG3V9GvJKlxLQd+RAwAjwP3ArcCD0TErVeddi9woP44Bnyt1X4lSc2p4hX+IeB8Zr6amW8BTwNHrjrnCPDNXPMCMBwRN1bQtySpQVUE/hjw+ob9xXpbs+cAEBHHImIuIuZWVlYqKE+SBNUEfmzSlrs4Z60x82RmTmTmxMjISMvFSZLWVBH4i8DNG/ZvApZ3cY4kaQ9VEfgvAgci4paIuBa4Hzh91TmngU/X79a5A3gzMy9U0LckqUHXtHqBzHw7Ih4GZoEB4MnMfCUiHqoffwI4AxwGzgO/Bz7Tar+SpOa0HPgAmXmGtVDf2PbEhu0EPl9FX5Kk3fE3bSWpEAa+JBXCwJekQhj4klQIA1+SCmHgS1IhDHxJKoSBL0mFMPAlqRAGviQVwsCXpEIY+JJUCANfkgph4EtSIQx8SSqEgS9JhTDwJakQBr4kFcLAl6RCGPiSVAgDX5IKYeBLUiEMfEkqhIEvSYUw8CWpEAa+JBXimlb+44h4H/CPwH7gNeBTmfnfm5z3GvA/wGXg7cycaKVfSVLzWn2Ffxz4QWYeAH5Q39/KX2bmRwz73jMzv8Rdj/2QW45/h7se+yEz80udLknSLrQa+EeAp+rbTwFHW7yeuszM/BInTp1jabVGAkurNU6cOmfoSz2o1cC/PjMvANS/XrfFeQl8NyLORsSx7S4YEcciYi4i5lZWVlosT62anl2gdunyFW21S5eZnl3oUEWSdmvHNfyI+D5wwyaHHmmin7syczkirgO+FxE/z8znNzsxM08CJwEmJiayiT60B5ZXa021S+peOwZ+Zn50q2MR8UZE3JiZFyLiRuDiFtdYrn+9GBHPAIeATQNf3WV0eIilTcJ9dHioA9VIakWrSzqngQfr2w8Cz159QkS8JyLeu74NfAx4ucV+1SZTk+MMDQ5c0TY0OMDU5HiHKpK0Wy3dlgk8Bnw7Ij4L/BfwSYCIGAW+npmHgeuBZyJivb9/yMx/brFftcnRg2PA2lr+8mqN0eEhpibH32mX1Dsis3uXyScmJnJubq7TZUhSz4iIs1vd/u5v2kpSIQx8SSqEgS9JhTDwJakQBr4kFcLAl6RCGPiSVAgDX5IKYeBLUiEMfEkqhIEvSYUw8CWpEAa+JBXCwJekQhj4klQIA1+SCmHgS1IhDHxJKoSBL0mFMPAlqRAGviQVwsCXpEJc0+kCtHdm5peYnl1gebXG6PAQU5PjHD041umyJHWIgd+nZuaXOHHqHLVLlwFYWq1x4tQ5AENfKpRLOn1qenbhnbBfV7t0menZhQ5VJKnTWgr8iPhkRLwSEX+IiIltzrsnIhYi4nxEHG+lTzVmebXWVLuk/tfqK/yXgfuA57c6ISIGgMeBe4FbgQci4tYW+9UORoeHmmqX1P9aCvzM/Flm7rRGcAg4n5mvZuZbwNPAkVb61c6mJscZGhy4om1ocICpyfEOVSSp09rxpu0Y8PqG/UXgz9rQb9HW35j1Lh1J63YM/Ij4PnDDJoceycxnG+gjNmnLbfo7BhwDeP/739/A5bWVowfHDHhJ79gx8DPzoy32sQjcvGH/JmB5m/5OAicBJiYmtvzGIElqTjtuy3wROBARt0TEtcD9wOk29CtJ2qDV2zI/HhGLwJ3AdyJitt4+GhFnADLzbeBhYBb4GfDtzHyltbIlSc1q6U3bzHwGeGaT9mXg8Ib9M8CZVvqSJLXG37SVpEIY+JJUCANfkgph4EtSIQx8SSqEgS9JhTDwJakQBr4kFcLAl6RCGPiSVAgDX5IKYeBLUiEMfEkqhIEvSYVox9+0bauZ+SX/jqskbaKvAn9mfokTp85Ru3QZgKXVGidOnQMw9CUVr6+WdKZnF94J+3W1S5eZnl3oUEWS1D36KvCXV2tNtUtSSfoq8EeHh5pql6SS9FXgT02OMzQ4cEXb0OAAU5PjHapIkrpHX71pu/7GrHfpSNK79VXgw1roG/CS9G59taQjSdqagS9JhTDwJakQBr4kFcLAl6RCRGZ2uoYtRcQK8EtgH/CrDpdTtX4cE/TnuBxTb+jHMUHz4/pAZo5sdqCrA39dRMxl5kSn66hSP44J+nNcjqk39OOYoNpxuaQjSYUw8CWpEL0S+Cc7XcAe6McxQX+OyzH1hn4cE1Q4rp5Yw5ckta5XXuFLklpk4EtSIboy8CPikxHxSkT8ISK2vB0pIl6LiHMR8ZOImGtnjc1qYkz3RMRCRJyPiOPtrHE3IuJ9EfG9iPhF/esfb3Fe18/VTs99rPly/fhPI+L2TtTZjAbGdHdEvFmfl59ExBc6UWejIuLJiLgYES9vcbzn5ggaGlc185SZXfcA/hQYB/4FmNjmvNeAfZ2ut6oxAQPAfwAfBK4FXgJu7XTtO4zrb4Hj9e3jwN/04lw18twDh4HngADuAP6103VXMKa7gX/qdK1NjOkvgNuBl7c43lNz1MS4KpmnrnyFn5k/y8y++svjDY7pEHA+M1/NzLeAp4Eje19dS44AT9W3nwKOdrCWVjTy3B8BvplrXgCGI+LGdhfahF7897StzHwe+M02p/TaHAENjasSXRn4TUjguxFxNiKOdbqYCowBr2/YX6y3dbPrM/MCQP3rdVuc1+1z1chz32vz02i9d0bESxHxXER8qD2l7Zlem6NmtDxPHfuLVxHxfeCGTQ49kpnPNniZuzJzOSKuA74XET+vf6fsiArGFJu0dfy+2e3G1cRlumquNtHIc9+V87ONRur9MWufvfK7iDgMzAAH9ryyvdNrc9SoSuapY4GfmR+t4BrL9a8XI+IZ1n6E7ViIVDCmReDmDfs3AcstXrNl240rIt6IiBsz80L9R+eLW1yjq+ZqE4089105P9vYsd7M/O2G7TMR8fcRsS8ze/VDyHptjhpS1Tz17JJORLwnIt67vg18DNj0He4e8iJwICJuiYhrgfuB0x2uaSengQfr2w8C7/pJpkfmqpHn/jTw6fqdIHcAb64vZ3WpHccUETdERNS3D7GWCb9ue6XV6bU5akhl89Tpd6e3eEf646x9p/5f4A1gtt4+Cpypb3+QtbsOXgJeYW3ZpOO1tzKm+v5h4N9Zu7uiq8dUr/dPgB8Av6h/fV+vztVmzz3wEPBQfTuAx+vHz7HNHWTd8mhgTA/X5+Ql4AXgzztd8w7j+RZwAbhU///ps70+Rw2Oq5J58qMVJKkQPbukI0lqjoEvSYUw8CWpEAa+JBXCwJekQhj4klQIA1+SCvF/V9kkek8MaWsAAAAASUVORK5CYII=",
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
    "# Plot the standardized data\n",
    "plt.scatter(z_mat[:,0], z_mat[:,1])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "LzPo-r1BK4-a",
    "outputId": "0918a63c-46a6-45d6-dbc8-3f6ca771eb17"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.2        1.17530862]\n",
      " [1.17530862 1.2       ]]\n"
     ]
    }
   ],
   "source": [
    "# Compute the covariance matrix\n",
    "covariance_mat = np.cov(z_mat.transpose())\n",
    "print(covariance_mat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "dBbr6mhUK4-a",
    "outputId": "59506ca6-ec60-460a-e312-3b27f8d5b969"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eigenvectors: \n",
      " [[ 0.70710678 -0.70710678]\n",
      " [ 0.70710678  0.70710678]] \n",
      "\n",
      "Eigenvalues: \n",
      " [2.37530862 0.02469138] \n",
      "\n"
     ]
    }
   ],
   "source": [
    " # Compute the eigendecomposition\n",
    "eigen_values, eigen_vectors = np.linalg.eig(covariance_mat)\n",
    "print(\"Eigenvectors: \\n\", eigen_vectors,\"\\n\")\n",
    "print(\"Eigenvalues: \\n\", eigen_values, \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 265
    },
    "id": "f0GC86OlK4-a",
    "outputId": "88209145-46a0-4925-f090-7d5fb9987b86"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
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
    "# Plot of standarized data and eigenvectors\n",
    "plt.scatter(z_mat[:,0], z_mat[:,1])\n",
    "plt.arrow(0, 0, eigen_vectors[0,0], eigen_vectors[1,0], color='r',\n",
    "          head_width=0.2, head_length=0.2)\n",
    "plt.arrow(0, 0, eigen_vectors[0,1], eigen_vectors[1,1], color='g',\n",
    "          head_width=0.2, head_length=0.2)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "HijLA2pWK4-a"
   },
   "source": [
    "## Task 1.1: Application of PCA (30 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 282
    },
    "id": "72d45ke8K4-a",
    "outputId": "358c4b94-480f-454f-98a4-d70f65afd32d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-1.910095   -1.20056174 -0.77669163  0.62406999  1.1471159   2.11616247]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x26b338ab8b0>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
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
    "# TODO. See assignment sheet for instructions.\n",
    "\n",
    "#Transpose the eigen vectors\n",
    "eigen_vectors1 = eigen_vectors.transpose()\n",
    "\n",
    "#Sorting eigen values and corresponding eigen vectors in descending order\n",
    "idxs = np.argsort(eigen_values)[::-1]\n",
    "eigen_values = eigen_values[idxs]\n",
    "eigen_vectors1 = eigen_vectors1[idxs]\n",
    "\n",
    "#calculating the projected matrix for highest 1st principle component\n",
    "projected_Z = z_mat.dot(eigen_vectors1[0])\n",
    "print(projected_Z)\n",
    "#Plost of transformed data\n",
    "y_axis = np.zeros(projected_Z.shape)\n",
    "plt.scatter(projected_Z,y_axis)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RDinFVXGK4-a"
   },
   "source": [
    "## Task 1.2: Reconstruction of data (30 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Acj4uoujK4-a",
    "outputId": "dea6d274-8f38-4767-835f-9b1c40cc5d0b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-1.35064113 -1.35064113]\n",
      " [-0.84892534 -0.84892534]\n",
      " [-0.54920392 -0.54920392]\n",
      " [ 0.44128412  0.44128412]\n",
      " [ 0.81113343  0.81113343]\n",
      " [ 1.49635283  1.49635283]]\n",
      "Reconstructed matrix:\n",
      "[[1.15476042 1.34145333]\n",
      " [2.03212571 2.27948147]\n",
      " [2.55625746 2.83985278]\n",
      " [4.28835332 4.69170933]\n",
      " [4.93511979 5.38319458]\n",
      " [6.1333833  6.66430851]]\n"
     ]
    }
   ],
   "source": [
    "# TODO. See assignment sheet for instructions.\n",
    "eigen_vectors2=eigen_vectors.transpose()\n",
    "new_mat=np.asmatrix(projected_Z).transpose().dot(np.asmatrix([eigen_vectors2[0]]))\n",
    "recon_mat = np.array(new_mat)\n",
    "print(recon_mat)\n",
    "recons_mat = np.zeros(recon_mat.shape)\n",
    "#To add mean and multiply with standard deviation to get reconstructed data\n",
    "recons_mat[:,0] = (recon_mat[:,0]*std1) + mean1\n",
    "recons_mat[:,1] = (recon_mat[:,1]*std2) + mean2 \n",
    "print(\"Reconstructed matrix:\")\n",
    "print(recons_mat)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "9IHH2VY3K4-a"
   },
   "source": [
    "## Task 1.3: Plotting of data (20 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 265
    },
    "id": "27ubQO18K4-b",
    "outputId": "5c44532a-14b9-4f82-a220-9dc03a4340f1"
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWoAAAD4CAYAAADFAawfAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAYLElEQVR4nO3df3CU5b338fe3AQmNmFSIDpp6gg6eYsImQJA6in0AZTxVLCJEOuo0nimMg1aPdnrUx1EEZzpP1TGWwdJDpUdUfHwCHKy/6ugQnGKtPfIjBAIeLJIzpBxrxBIJCZgf3+ePTSI/NskGs7tX2M9rZmezV6697++9ho/3XnvtdZu7IyIi4fpGqgsQEZGeKahFRAKnoBYRCZyCWkQkcApqEZHADUrERkeMGOH5+fmJ2LSIyGlp8+bNn7l7bqzfJSSo8/Pz2bRpUyI2LSJyWjKz/+7udxr6EBEJnIJaRCRwCmoRkcAlZIw6lpaWFurq6jhy5EiydimBy8zMJC8vj8GDB6e6FJGgJS2o6+rqGDZsGPn5+ZhZsnYrgXJ3Dhw4QF1dHaNGjUp1OSJBS9rQx5EjRxg+fLhCWgAwM4YPH653WDKwVVdAeSE8khO9r65IyG6SdkYNKKTlOPp7kAGtugJevQtamqOPG/ZFHwNESvt1V0kNahGR08b6xV+FdKeWZurWPMAVL2aRNSSDmkXX9Muu0mrWR0ZGBsXFxRQWFjJjxgwOHjyYslreeecd3nvvvX7b3ssvv8zOnTv7/LwzzzwzZnvna1VQUEBRURFPPvkk7e3tPW6rtraWF198sc81iAxIDXUxm8+zAwAcPtrWb7tKq6AeOnQoVVVV7Nixg7PPPpunn346ZbX0FNStra193t6pBnV3Ol+rmpoa3n77bd544w0WLVrU43MU1JJWsvNiNu/34f2+qyCDumDhm+Tf//pJt4KFb/bbPi677DL++te/ArBnzx6uueYaJkyYwOTJk/nwww8B+Nvf/sYNN9xAUVERRUVFXcH65JNPUlhYSGFhIU899RQQDakxY8Ywb948CgoKmD59Os3N0bdFS5Ys4ZJLLiESiTB37lxqa2v59a9/TXl5OcXFxWzcuJGysjLuvfdepkyZwn333ccjjzzCE0880VVvYWEhtbW1ADz33HNEIhGKioq49dZbee+993jllVf42c9+RnFxMXv27On2mPbu3ctll13GxIkTeeihh+J6rc455xyWL1/O0qVLcXdqa2uZPHky48ePZ/z48V2vy/3338/GjRspLi6mvLy8234ip4VpD8Pgocc1NfkZPNbav+PTQHSaVH/fJkyY4CfauXPnSW3d+Yf7Xuv29nVkZWW5u3tra6vPnj3bf//737u7+9SpU3337t3u7v7+++/7lClT3N29tLTUy8vLu55z8OBB37RpkxcWFnpjY6MfOnTIL7nkEt+yZYvv3bvXMzIyfOvWre7uPmfOHH/++efd3X3kyJF+5MgRd3f/+9//7u7uCxcu9Mcff7yrth/96Ed+7bXXemtra8zfFxQU+N69e33Hjh1+8cUXe319vbu7HzhwoOv5q1ev7urf3THNmDHDV65c6e7uS5cu7XpNunutjpWTk+OffPKJHz582Jubm93dfffu3d7533vDhg1+7bXXdvXvrt+x+vJ3IRKcbf/P9z10obc9nO37HrrQf/LA/aecV8Am7yZT0+rDxObmZoqLi6mtrWXChAlcffXVNDY28t577zFnzpyufkePHgWgsrKS5557DoiO2WZnZ/Puu+9yww03kJWVBcCsWbPYuHEj119/PaNGjaK4uBiACRMmdJ0BRyIRbr75ZmbOnMnMmTO7rW/OnDlkZGT0eAyVlZXMnj2bESNGAHD22Wef1KenY/rjH//I2rVrAbj11lu57777etzfsbzj+potLS3ceeedVFVVkZGRwe7du2P2j7efyIAVKeWKF7MSvpu0CurOcdeGhgauu+46nn76acrKysjJyaGqqiqubXgPFwMeMmRI188ZGRldQx+vv/46f/jDH3jllVd49NFHqampifn8zvAHGDRo0HEf3nXON3b3Xqe1tbe393hMpzIt7uOPPyYjI4NzzjmHRYsWce6557Jt2zba29vJzMyM+Zzy8vK4+okMZFlDMmJ+cJg1pOeTrr4Icow60bKzs1myZAlPPPEEQ4cOZdSoUaxevRqIBuG2bdsAmDZtGsuWLQOgra2NL774giuvvJKXX36ZpqYmDh8+zLp165g8eXK3+2pvb2ffvn1MmTKFxx57jIMHD9LY2MiwYcM4dOhQt8/Lz89ny5YtAGzZsoW9e/d21VRRUcGBA9FPlj///HOA47Z31llndXtMl19+OS+99BIAq1atiuv1qq+v5/bbb+fOO+/E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",
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
    "# TODO. See assignment sheet for instructions.\n",
    "plt.scatter(recons_mat[:,0],recons_mat[:,1],marker=',',label='Reconstructed Data')\n",
    "plt.scatter(mat[:,0], mat[:,1],label='Original Data')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dceEuVfiK4-b"
   },
   "source": [
    "## Task 1.4: Error of PCA (20 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "bQUSY2hR8Fwb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.2670368335684183\n"
     ]
    }
   ],
   "source": [
    "err=0\n",
    "for i in range(mat.shape[0]):\n",
    "    a=mat[i,:]\n",
    "    b=recons_mat[i,:]\n",
    "    err+=np.linalg.norm(a-b)\n",
    "print(err)"
   ]
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
  "colab": {
   "collapsed_sections": [],
   "name": "MLDM_Assignment03.ipynb",
   "provenance": []
  },
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
 "nbformat_minor": 1
}
