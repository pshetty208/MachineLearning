{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "evaluation = pd.read_csv(\"evaluation_calculation.csv\", header = 0)\n",
    "evaluation= evaluation.drop(evaluation.columns[0], axis = 1)"
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
      "       TRUE Predicted\n",
      "0    Desert    Desert\n",
      "1    Desert    Desert\n",
      "2    Desert    Desert\n",
      "3    Desert    Desert\n",
      "4    Desert    Desert\n",
      "..      ...       ...\n",
      "125  Forest    Forest\n",
      "126  Forest    Forest\n",
      "127  Forest    Forest\n",
      "128  Forest    Forest\n",
      "129  Forest    Forest\n",
      "\n",
      "[130 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "print(evaluation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['TRUE', 'Predicted']\n",
      "0      Desert\n",
      "1      Desert\n",
      "2      Desert\n",
      "3      Desert\n",
      "4      Desert\n",
      "        ...  \n",
      "125    Forest\n",
      "126    Forest\n",
      "127    Forest\n",
      "128    Forest\n",
      "129    Forest\n",
      "Name: Predicted, Length: 130, dtype: object\n",
      "0      Desert\n",
      "1      Desert\n",
      "2      Desert\n",
      "3      Desert\n",
      "4      Desert\n",
      "        ...  \n",
      "125    Forest\n",
      "126    Forest\n",
      "127    Forest\n",
      "128    Forest\n",
      "129    Forest\n",
      "Name: TRUE, Length: 130, dtype: object\n",
      "['Desert' 'Beach' 'Forest']\n"
     ]
    }
   ],
   "source": [
    "Heading = list(evaluation.columns)\n",
    "print(Heading)\n",
    "\n",
    "Y_true = evaluation[Heading[1]]\n",
    "print(Y_true)\n",
    "\n",
    "Y_pred = evaluation[Heading[0]]\n",
    "print(Y_pred)\n",
    "\n",
    "classes_name = Y_true.unique()\n",
    "print(classes_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[28  1  1]\n",
      " [ 8 40  2]\n",
      " [ 0  0 50]]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "conf_matrix=confusion_matrix(Y_pred,Y_true, labels = classes_name)\n",
    "print(conf_matrix)"
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
      "              precision    recall  f1-score   support\n",
      "\n",
      "       Beach    0.80000   0.97561   0.87912        41\n",
      "      Desert    0.93333   0.77778   0.84848        36\n",
      "      Forest    1.00000   0.94340   0.97087        53\n",
      "\n",
      "    accuracy                        0.90769       130\n",
      "   macro avg    0.91111   0.89893   0.89949       130\n",
      "weighted avg    0.91846   0.90769   0.90804       130\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report\n",
    "print(classification_report(Y_true, Y_pred, zero_division=0, digits = 5))"
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
      "For class Desert\n",
      "\tprecision = 0.9333333333333333\n",
      "\trecall = 0.7777777777777778\n",
      "\tF1 Score = 0.8484848484848485\n",
      "\tAccuracy = 0.9230769230769231\n",
      "For class Beach\n",
      "\tprecision = 0.8\n",
      "\trecall = 0.975609756097561\n",
      "\tF1 Score = 0.8791208791208791\n",
      "\tAccuracy = 0.9153846153846154\n",
      "For class Forest\n",
      "\tprecision = 1.0\n",
      "\trecall = 0.9433962264150944\n",
      "\tF1 Score = 0.970873786407767\n",
      "\tAccuracy = 0.9769230769230769\n",
      "Micro Avg :\n",
      "\t For Precision = 0.9076923076923077\n",
      "\t For Recall = 0.9076923076923077\n",
      "\t For F1 score = 0.9076923076923076\n",
      "\t For Accuracy = \n",
      "Macro Avg :\n",
      "\t For Precision = 0.9111111111111111\n",
      "\t For Recall = 0.8989279200968111\n",
      "\t For F1 score = 0.8994931713378316\n",
      "\t For Accuracy =  0.9384615384615386\n"
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
    "for class_name in classes_name:\n",
    "    tp = conf_matrix[i,i]\n",
    "    TP.append(tp)\n",
    "    fp = sum(conf_matrix[i]) - tp\n",
    "    FP.append(fp)\n",
    "    fn = sum(conf_matrix[...,i]) - tp\n",
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
