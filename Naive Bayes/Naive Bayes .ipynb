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
    "def feature_probability(features_dict,classes_dict):\n",
    "    print(features_dict)\n",
    "    print(classes_dict)\n",
    "    for feature in features_dict.keys() :\n",
    "        print(\"\\n\\tFor Feature\", feature, \"with total samples =\", features_dict[feature])\n",
    "        tot = features_dict[feature]\n",
    "        for classes in classes_dict.keys() :\n",
    "            if classes.startswith(feature) :\n",
    "                val = classes_dict[classes]\n",
    "                print(\"\\t\\tFor class\",classes,\":\", val,\"/\",tot, \"=\" ,probability(val,tot))\n",
    "#        entropy_feature = entropy(prob_list)\n",
    "#        print(\"\\tEntropy (sum((p*log2p) of all classes) for Feature\", feature, \"with probability\", features_dict[feature], \"/\", total, \"is :\", entropy_feature)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "execution_count": 8,
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
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For attribute Pain the Probabilities are -->\n",
      "{'Y': 6, 'N': 4}\n",
      "{'Y and NP': 3, 'N and M': 1, 'Y and S': 1, 'N and NP': 2, 'Y and M': 2, 'N and S': 1}\n",
      "\n",
      "\tFor Feature Y with total samples = 6\n",
      "\t\tFor class Y and NP : 3 / 6 = 0.5\n",
      "\t\tFor class Y and S : 1 / 6 = 0.16666666666666666\n",
      "\t\tFor class Y and M : 2 / 6 = 0.3333333333333333\n",
      "\n",
      "\tFor Feature N with total samples = 4\n",
      "\t\tFor class N and M : 1 / 4 = 0.25\n",
      "\t\tFor class N and NP : 2 / 4 = 0.5\n",
      "\t\tFor class N and S : 1 / 4 = 0.25\n",
      "\n",
      "************************\n",
      "For attribute Breathing the Probabilities are -->\n",
      "{'Y': 6, 'N': 4}\n",
      "{'Y and B': 2, 'N and B': 2, 'Y and P': 1, 'Y and G': 3, 'N and P': 2}\n",
      "\n",
      "\tFor Feature Y with total samples = 6\n",
      "\t\tFor class Y and B : 2 / 6 = 0.3333333333333333\n",
      "\t\tFor class Y and P : 1 / 6 = 0.16666666666666666\n",
      "\t\tFor class Y and G : 3 / 6 = 0.5\n",
      "\n",
      "\tFor Feature N with total samples = 4\n",
      "\t\tFor class N and B : 2 / 4 = 0.5\n",
      "\t\tFor class N and P : 2 / 4 = 0.5\n",
      "\n",
      "************************\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "for every_attribute in Attributes[:-1]:\n",
    "    print(\"For attribute\",every_attribute, \"the Probabilities are -->\")\n",
    "    input_value = dataset[every_attribute]\n",
    "    features_dict,classes_dict = node_classification(input_value)\n",
    "    feature_probability(features_dict,classes_dict)\n",
    "    \n",
    "    print(\"\\n************************\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def conditional_prob(class_name, feature_name, feature_data):\n",
    "    feature_dictionary = dict()\n",
    "    i=0\n",
    "    for feature in feature_data:\n",
    "        if (classes[i] ==class_name) : \n",
    "            isPresent = feature in feature_dictionary\n",
    "            if(isPresent == False):\n",
    "                feature_dictionary[feature] = 1\n",
    "            else :\n",
    "                feature_dictionary[feature] += 1\n",
    "        i += 1\n",
    "\n",
    "    values = feature_dictionary.values()\n",
    "    total = sum(values)\n",
    "    isPresent = feature_name in feature_dictionary\n",
    "    if(isPresent == False):\n",
    "        val = 0\n",
    "    else :\n",
    "        val = feature_dictionary[feature_name]\n",
    "    probab = probability(val,total)\n",
    "    print(\"\\tCond. Probability of\",class_name,\"and\",feature_name, 'is', val,'/',total, '=', probab)\n",
    "    return(probab)\n"
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
      "for Pain the feature should be (put 0 if not require)\n",
      ":M\n",
      "for Breathing the feature should be (put 0 if not require)\n",
      ":G\n",
      "For class Y\n",
      "\tCond. Probability of Y and M is 2 / 6 = 0.3333333333333333\n",
      "\tCond. Probability of Y and G is 3 / 6 = 0.5\n",
      "Class conditional Probability P(X|Y) or P(X|N)  0.16666666666666666\n",
      "Joint Probabiity P(Y|X) or P(N|X) : 0.09999999999999999\n",
      "For class N\n",
      "\tCond. Probability of N and M is 1 / 4 = 0.25\n",
      "\tCond. Probability of N and G is 0 / 4 = 0.0\n",
      "Class conditional Probability P(X|Y) or P(X|N)  0.0\n",
      "Joint Probabiity P(Y|X) or P(N|X) : 0.0\n"
     ]
    }
   ],
   "source": [
    "Cond_prob = []\n",
    "for atr in Attributes[:-1]:\n",
    "    print(\"for\",atr,\"the feature should be (put 0 if not require)\")\n",
    "    feat = input(\":\")\n",
    "    Cond_prob.append(feat)\n",
    "\n",
    "for every_class in Probability_dict.keys() :  \n",
    "    print(\"For class\", every_class)   \n",
    "    i=0\n",
    "    P = 1\n",
    "    for every_feature in Cond_prob :\n",
    "        if (every_feature == \"0\") :\n",
    "            continue\n",
    "        Probab = conditional_prob(every_class,Cond_prob[i],dataset[Attributes[i]])        \n",
    "        i += 1        \n",
    "        P = P * Probab\n",
    "    print(\"Class conditional Probability P(X|Y) or P(X|N) \", P)\n",
    "    Prob = Probability_dict[every_class]\n",
    "    Prob = Prob * P\n",
    "    print(\"Joint Probabiity P(Y|X) or P(N|X) :\", Prob)"
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
