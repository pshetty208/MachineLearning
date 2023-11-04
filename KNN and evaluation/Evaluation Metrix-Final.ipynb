{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####Write confusion matrix in CSV file with following condition1 :\n",
    "1. Heading and 1st column should be class name\n",
    "2. The data goes row wise i.e. 1st row will have detail of class1 classified to which classes"
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
      "['A', 'B', 'C']\n",
      "[[ nan  nan  nan  nan]\n",
      " [ nan  90.   7.   3.]\n",
      " [ nan  11. 162.   7.]\n",
      " [ nan  14.   8. 118.]]\n",
      "[[ 90.   7.   3.]\n",
      " [ 11. 162.   7.]\n",
      " [ 14.   8. 118.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from numpy import genfromtxt\n",
    "\n",
    "evaluation = pd.read_csv(\"evaluation.csv\", header = 0)\n",
    "evaluation= evaluation.drop(evaluation.columns[0], axis = 1)\n",
    "classes = list(evaluation.columns)\n",
    "print(classes)\n",
    "\n",
    "evaluation = genfromtxt('evaluation.csv', delimiter=',')\n",
    "print(evaluation)\n",
    "\n",
    "\n",
    "evaluation = np.delete(evaluation, 0, 0)\n",
    "evaluation = np.delete(evaluation, 0, 1)\n",
    "print(evaluation)\n",
    "\n",
    "conf_matrix = evaluation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TP 90.0\n",
      "TN 295.0\n",
      "FP 25.0\n",
      "FN 10.0\n",
      "For class A\n",
      "\tprecision = 0.782608695652174\n",
      "\trecall = 0.9\n",
      "\tF1 Score = 0.8372093023255814\n",
      "\tAccuracy = 0.9166666666666666\n",
      "TP 162.0\n",
      "TN 225.0\n",
      "FP 15.0\n",
      "FN 18.0\n",
      "For class B\n",
      "\tprecision = 0.9152542372881356\n",
      "\trecall = 0.9\n",
      "\tF1 Score = 0.9075630252100839\n",
      "\tAccuracy = 0.9214285714285714\n",
      "TP 118.0\n",
      "TN 270.0\n",
      "FP 10.0\n",
      "FN 22.0\n",
      "For class C\n",
      "\tprecision = 0.921875\n",
      "\trecall = 0.8428571428571429\n",
      "\tF1 Score = 0.880597014925373\n",
      "\tAccuracy = 0.9238095238095239\n",
      "Micro Avg :\n",
      "\t For Precision = 0.8809523809523809\n",
      "\t For Recall = 0.8809523809523809\n",
      "\t For F1 score = 0.880952380952381\n",
      "\t For Accuracy = \n",
      "Macro Avg :\n",
      "\t For Precision = 0.8732459776467699\n",
      "\t For Recall = 0.8809523809523809\n",
      "\t For F1 score = 0.8751231141536794\n",
      "\t For Accuracy =  0.9206349206349206\n"
     ]
    }
   ],
   "source": [
    "i=0\n",
    "TP = []\n",
    "TN = []\n",
    "FP = []\n",
    "FN = []\n",
    "Precision_list = []\n",
    "Recall_list = []\n",
    "F1_score = []\n",
    "Accuracy = []\n",
    "for class_name in classes:\n",
    "    tp = conf_matrix[i,i]\n",
    "    TP.append(tp)\n",
    "    fp = sum(conf_matrix[...,i]) - tp\n",
    "    FP.append(fp)\n",
    "    fn = sum(conf_matrix[i]) - tp\n",
    "    FN.append(fn)\n",
    "    tn = sum(sum(conf_matrix)) - tp - fp - fn\n",
    "    TN.append(tn)\n",
    "    \n",
    "    precision  = tp / (tp + fp)\n",
    "    Precision_list.append(precision)\n",
    "    recall     = tp / (tp + fn)\n",
    "    Recall_list.append(recall)\n",
    "    f1_score   = 2*( precision * recall)/(precision + recall)\n",
    "    F1_score.append(f1_score)\n",
    "    accuracy   = (tp+tn)/(tp+fn+fp+tn)\n",
    "    Accuracy.append(accuracy)\n",
    "    print(\"TP\", tp)\n",
    "    print(\"TN\", tn)\n",
    "    print(\"FP\", fp)\n",
    "    print(\"FN\", fn)\n",
    "\n",
    "    print('For class', class_name)\n",
    "    print('\\tprecision =', precision)\n",
    "    print('\\trecall =', recall)\n",
    "    print('\\tF1 Score =', f1_score)\n",
    "    print('\\tAccuracy =', accuracy)\n",
    "    i += 1\n",
    "\n",
    "print('Micro Avg :')\n",
    "print('\\t For Precision =', sum(TP)/(sum(TP) + sum(FP)))\n",
    "print('\\t For Recall =', sum(TP)/(sum(TP) + sum(FN)))\n",
    "print('\\t For F1 score =', 2*( sum(TP)/(sum(TP) + sum(FP)) * sum(TP)/(sum(TP) + sum(FN)))/(sum(TP)/(sum(TP) + sum(FP)) + sum(TP)/(sum(TP) + sum(FN))))\n",
    "print('\\t For Accuracy = ')\n",
    "\n",
    "print('Macro Avg :')\n",
    "print('\\t For Precision =', sum(Precision_list)/len(Precision_list))\n",
    "print('\\t For Recall =', sum(Recall_list)/len(Recall_list))\n",
    "print('\\t For F1 score =', sum(F1_score)/len(F1_score))\n",
    "print('\\t For Accuracy = ', sum(Accuracy)/len(Accuracy))"
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
