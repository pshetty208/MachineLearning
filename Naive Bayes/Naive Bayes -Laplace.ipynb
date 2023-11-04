{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Input file specification :\n",
    "\n",
    "1. File should be CSV format (can be changed from excel to CSV)\n",
    "2. File name is bayes (.csv will come automatic if you save from excel)\n",
    "3. Don't remove the headers\n",
    "4. Remove \"S. No.\" column if present in excel file and then change to CSV\n",
    "5. Assumption : That the last column of csv is the target class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def probability(val,total) :\n",
    "    prob = val/total\n",
    "    return prob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def overall_probability(test_data):\n",
    "    #making dictionary of every class\n",
    "    output_class = dict()\n",
    "    for every_value in test_data:\n",
    "        isPresent = every_value in output_class\n",
    "        if(isPresent == False):\n",
    "            output_class[every_value] = 1\n",
    "        else:\n",
    "            output_class[every_value] += 1\n",
    "    print(output_class)\n",
    "   \n",
    "    #calculating total\n",
    "    values = output_class.values()\n",
    "    total = sum(values)\n",
    "    print(\"Total number of data : \", total)\n",
    "    \n",
    "    #calculating entropy of each key in the dictionary\n",
    "    probability_dict = dict()\n",
    "    probability_list = []\n",
    "    for every_key in output_class.keys() :\n",
    "        val = output_class[every_key]\n",
    "        probability_list.append(val/total)\n",
    "        print(\"\\Probability of\",every_key,\"is: \", val, \"/\", total, \"=\", probability(val,total))\n",
    "        probability_dict[every_key] = probability(val,total)\n",
    "#    print(probability_list)\n",
    "    print(\"\\033[1m\\nOverall Probability is : \", sum(probability_list), \"\\033[0m\")\n",
    "    return probability_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def node_classification(feature_data):\n",
    "    classes_dict = dict()\n",
    "    features_dict = dict()\n",
    "\n",
    "    i=0\n",
    "    for feature in feature_data:\n",
    "        isPresent = classes[i] in classes_dict\n",
    "        if(isPresent == False):\n",
    "            classes_dict[classes[i]] = 1\n",
    "            child = classes[i] + \" and \" + feature\n",
    "            isPresent = child in features_dict\n",
    "            if(isPresent == False):\n",
    "                features_dict[child] = 1\n",
    "            else :\n",
    "                features_dict[child] += 1\n",
    "        else:\n",
    "            classes_dict[classes[i]] += 1\n",
    "            child = classes[i] + \" and \" + feature\n",
    "            isPresent = child in features_dict\n",
    "            if(isPresent == False):\n",
    "                features_dict[child] = 1  \n",
    "            else :\n",
    "                features_dict[child] += 1\n",
    "        i += 1\n",
    "    return classes_dict,features_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def feature_probability_laplace(features_dict,classes_dict,count):\n",
    "    print(features_dict)\n",
    "    print(classes_dict)\n",
    "    for feature in features_dict.keys() :\n",
    "        print(\"\\n\\tFor Feature\", feature, \"with total samples =\", features_dict[feature])\n",
    "        tot = features_dict[feature]\n",
    "        for classes in classes_dict.keys() :\n",
    "            if classes.startswith(feature) :\n",
    "                val = classes_dict[classes]\n",
    "                print(\"\\t\\tFor class\",classes,\":\", val+1,\"/\",tot+count, \"=\" ,probability(val+1,tot+count))\n",
    "#        entropy_feature = entropy(prob_list)\n",
    "#        print(\"\\tEntropy (sum((p*log2p) of all classes) for Feature\", feature, \"with probability\", features_dict[feature], \"/\", total, \"is :\", entropy_feature)"
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
      "  Pain Breathing Flue\n",
      "0   NP         B    Y\n",
      "1    M         B    N\n",
      "2   NP         P    Y\n",
      "3    S         G    Y\n",
      "4   NP         P    N\n",
      "5    M         B    Y\n",
      "6   NP         G    Y\n",
      "7    S         B    N\n",
      "8    M         G    Y\n",
      "9   NP         P    N\n",
      "['Pain', 'Breathing', 'Flue']\n",
      "0    Y\n",
      "1    N\n",
      "2    Y\n",
      "3    Y\n",
      "4    N\n",
      "5    Y\n",
      "6    Y\n",
      "7    N\n",
      "8    Y\n",
      "9    N\n",
      "Name: Flue, dtype: object\n",
      "['Y' 'N']\n"
     ]
    }
   ],
   "source": [
    "dataset = pd.read_csv(\"bayes.csv\", header = 0)\n",
    "print(dataset)\n",
    "Attributes = list(dataset.columns)\n",
    "print(Attributes)\n",
    "classes = dataset[Attributes[-1]]\n",
    "print(classes)\n",
    "classes_name = classes.unique()\n",
    "print(classes_name)\n"
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
      "{'Y': 6, 'N': 4}\n",
      "Total number of data :  10\n",
      "\\Probability of Y is:  6 / 10 = 0.6\n",
      "\\Probability of N is:  4 / 10 = 0.4\n",
      "\u001b[1m\n",
      "Overall Probability is :  1.0 \u001b[0m\n"
     ]
    }
   ],
   "source": [
    "Probability_dict = overall_probability(classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "For attribute Pain the Probabilities are -->\n",
      "3\n",
      "{'Y': 6, 'N': 4}\n",
      "{'Y and NP': 3, 'N and M': 1, 'Y and S': 1, 'N and NP': 2, 'Y and M': 2, 'N and S': 1}\n",
      "\n",
      "\tFor Feature Y with total samples = 6\n",
      "\t\tFor class Y and NP : 4 / 9 = 0.4444444444444444\n",
      "\t\tFor class Y and S : 2 / 9 = 0.2222222222222222\n",
      "\t\tFor class Y and M : 3 / 9 = 0.3333333333333333\n",
      "\n",
      "\tFor Feature N with total samples = 4\n",
      "\t\tFor class N and M : 2 / 7 = 0.2857142857142857\n",
      "\t\tFor class N and NP : 3 / 7 = 0.42857142857142855\n",
      "\t\tFor class N and S : 2 / 7 = 0.2857142857142857\n",
      "\n",
      "************************\n",
      "\n",
      "For attribute Breathing the Probabilities are -->\n",
      "3\n",
      "{'Y': 6, 'N': 4}\n",
      "{'Y and B': 2, 'N and B': 2, 'Y and P': 1, 'Y and G': 3, 'N and P': 2}\n",
      "\n",
      "\tFor Feature Y with total samples = 6\n",
      "\t\tFor class Y and B : 3 / 9 = 0.3333333333333333\n",
      "\t\tFor class Y and P : 2 / 9 = 0.2222222222222222\n",
      "\t\tFor class Y and G : 4 / 9 = 0.4444444444444444\n",
      "\n",
      "\tFor Feature N with total samples = 4\n",
      "\t\tFor class N and B : 3 / 7 = 0.42857142857142855\n",
      "\t\tFor class N and P : 3 / 7 = 0.42857142857142855\n",
      "\n",
      "************************\n"
     ]
    }
   ],
   "source": [
    "for every_attribute in Attributes[:-1]:\n",
    "    print(\"\\nFor attribute\",every_attribute, \"the Probabilities are -->\")\n",
    "    input_value = dataset[every_attribute]\n",
    "    features_dict,classes_dict = node_classification(input_value)\n",
    "    count = len(dataset[every_attribute].unique())\n",
    "    print(count)\n",
    "    feature_probability_laplace(features_dict,classes_dict,count)\n",
    "    \n",
    "    print(\"\\n************************\")\n"
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
