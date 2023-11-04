{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Input file specification :\n",
    "1. File should be CSV format (can be changed from excel to CSV)\n",
    "2. File name is my_file (.csv will come automatic if you save from excel)\n",
    "3. Don't remove the headers\n",
    "4. Remove \"S. No.\" column if present in excel file and then change to CSV\n",
    "\n",
    "5. Assumption : That the last column of csv is the target class\n",
    "6. There is no normalization in this code."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Code for Decision Tree\n",
    "\n",
    "Predefined functions"
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
    "def entropy(prob) :\n",
    "    ent = 0\n",
    "    for p in prob :\n",
    "        ent1 = - (p * np.log2(p))\n",
    "        ent = ent + ent1\n",
    "    return ent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def overall_entropy(test_data):\n",
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
    "    probability_list = []\n",
    "    for every_key in output_class.keys() :\n",
    "        val = output_class[every_key]\n",
    "        probability_list.append(val/total)\n",
    "        print(\"\\tEntropy of\",every_key,\"with probability\", val, \"/\", total, \"is :\", entropy([val/total]))\n",
    "#    print(probability_list)\n",
    "    print(\"\\033[1m\\nOverall System Entropy is : \", entropy(probability_list), \"\\033[0m\")\n",
    "    return entropy(probability_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def node_classification(feature_data):\n",
    "    features_dict = dict()\n",
    "    classes_dict = dict()\n",
    "    i=0\n",
    "    for feature in feature_data:\n",
    "        isPresent = feature in features_dict\n",
    "        if(isPresent == False):\n",
    "            features_dict[feature] = 1\n",
    "            child = feature + \" and \" + classes[i]\n",
    "            isPresent = child in classes_dict\n",
    "            if(isPresent == False):\n",
    "                classes_dict[child] = 1\n",
    "            else :\n",
    "                classes_dict[child] += 1\n",
    "        else:\n",
    "            features_dict[feature] += 1\n",
    "            child = feature + \" and \" + classes[i]\n",
    "            isPresent = child in classes_dict\n",
    "            if(isPresent == False):\n",
    "                classes_dict[child] = 1  \n",
    "            else :\n",
    "                classes_dict[child] += 1\n",
    "        i += 1\n",
    "    return features_dict,classes_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def node_impurity(features_dict,classes_dict):\n",
    "    values = features_dict.values()\n",
    "    total = sum(values)\n",
    "    \n",
    "    #calculating entropy of each key in the dictionary\n",
    "    impurity_list = []\n",
    "    for feature in features_dict.keys() :\n",
    "        prob_list = []\n",
    "        print(\"\\n\\tFor Feature\", feature, \"with total samples =\", features_dict[feature])\n",
    "        tot = features_dict[feature]\n",
    "        for classes in classes_dict.keys() :\n",
    "            if classes.startswith(feature) :\n",
    "                val = classes_dict[classes]\n",
    "                print(\"\\t\\tFor class\",classes,\":\", val,\"/\",tot)\n",
    "                prob_list.append(val/tot)\n",
    "                print(\"\\t\\tEntropy is: \",entropy([val/total]))\n",
    "        entropy_feature = entropy(prob_list)\n",
    "        print(\"\\tEntropy (sum((p*log2p) of all classes) for Feature\", feature, \"with probability\", features_dict[feature], \"/\", total, \"is :\", entropy_feature)\n",
    "        probability = features_dict[feature]/total\n",
    "        impurity_list.append(entropy_feature*probability)\n",
    "        print(\"\\tImpurity (p*entropy) for Feature\", feature, \"with probability\", features_dict[feature], \"/\", total, \"is :\", entropy_feature*probability)\n",
    "    return sum(impurity_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def overall_error_rate(features_dict,classes_dict):\n",
    "    print(features_dict)\n",
    "    print(classes_dict, \"\\n\")\n",
    "    error_list = []\n",
    "    for feature in features_dict.keys() :\n",
    "        prob_list = []\n",
    "        print(feature, \"has\", features_dict[feature], \"samples\")\n",
    "        total = features_dict[feature]\n",
    "        for classes in classes_dict.keys() :\n",
    "            if classes.startswith(feature) :\n",
    "                val = classes_dict[classes]\n",
    "                prob_list.append(val)\n",
    "        highest = max(prob_list)\n",
    "        error = (total-highest)/total\n",
    "        error_list.append(error)\n",
    "        print(\"\\tError of\", feature, \"with e(t)/n(t) i.e.\", (total-highest), \"/\", total, \"is :\", error)\n",
    "    return sum(error_list)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def node_entropy(feature_data):\n",
    "    features_dict = dict()\n",
    "    classes_dict = dict()\n",
    "    for feature in feature_data:\n",
    "        isPresent = feature in features_dict\n",
    "        if(isPresent == False):\n",
    "            features_dict[feature] = 1\n",
    "        else:\n",
    "            features_dict[feature] += 1\n",
    "            \n",
    "    probability_list = []\n",
    "    values = features_dict.values()\n",
    "    total = sum(values)\n",
    "    for every_feature in features_dict.keys():\n",
    "        probability = features_dict[every_feature]/total\n",
    "        probability_list.append(probability)\n",
    "    return entropy(probability_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Main Program"
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
      "  Income Married Gender Creditworthy\n",
      "0      L       N      M            N\n",
      "1      L       Y      F            Y\n",
      "2      H       Y      F            N\n",
      "3      H       N      F            N\n",
      "4      H       N      M            Y\n",
      "5      L       Y      F            Y\n",
      "['Income', 'Married', 'Gender', 'Creditworthy']\n",
      "0    N\n",
      "1    Y\n",
      "2    N\n",
      "3    N\n",
      "4    Y\n",
      "5    Y\n",
      "Name: Creditworthy, dtype: object\n",
      "['N' 'Y']\n"
     ]
    }
   ],
   "source": [
    "dataset = pd.read_csv(\"my_file.csv\", header = 0)\n",
    "print(dataset)\n",
    "Attributes = list(dataset.columns)\n",
    "print(Attributes)\n",
    "classes = dataset[Attributes[-1]]\n",
    "print(classes)\n",
    "classes_name = classes.unique()\n",
    "print(classes_name)"
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
      "For attribute Income the classification is -->\n",
      "\n",
      "\tFor Feature L with total samples = 3\n",
      "\t\tFor class L and N : 1 / 3\n",
      "\t\tEntropy is:  0.430827083453526\n",
      "\t\tFor class L and Y : 2 / 3\n",
      "\t\tEntropy is:  0.5283208335737187\n",
      "\tEntropy (sum((p*log2p) of all classes) for Feature L with probability 3 / 6 is : 0.9182958340544896\n",
      "\tImpurity (p*entropy) for Feature L with probability 3 / 6 is : 0.4591479170272448\n",
      "\n",
      "\tFor Feature H with total samples = 3\n",
      "\t\tFor class H and N : 2 / 3\n",
      "\t\tEntropy is:  0.5283208335737187\n",
      "\t\tFor class H and Y : 1 / 3\n",
      "\t\tEntropy is:  0.430827083453526\n",
      "\tEntropy (sum((p*log2p) of all classes) for Feature H with probability 3 / 6 is : 0.9182958340544896\n",
      "\tImpurity (p*entropy) for Feature H with probability 3 / 6 is : 0.4591479170272448\n",
      "\n",
      "************************\n",
      "For attribute Married the classification is -->\n",
      "\n",
      "\tFor Feature N with total samples = 3\n",
      "\t\tFor class N and N : 2 / 3\n",
      "\t\tEntropy is:  0.5283208335737187\n",
      "\t\tFor class N and Y : 1 / 3\n",
      "\t\tEntropy is:  0.430827083453526\n",
      "\tEntropy (sum((p*log2p) of all classes) for Feature N with probability 3 / 6 is : 0.9182958340544896\n",
      "\tImpurity (p*entropy) for Feature N with probability 3 / 6 is : 0.4591479170272448\n",
      "\n",
      "\tFor Feature Y with total samples = 3\n",
      "\t\tFor class Y and Y : 2 / 3\n",
      "\t\tEntropy is:  0.5283208335737187\n",
      "\t\tFor class Y and N : 1 / 3\n",
      "\t\tEntropy is:  0.430827083453526\n",
      "\tEntropy (sum((p*log2p) of all classes) for Feature Y with probability 3 / 6 is : 0.9182958340544896\n",
      "\tImpurity (p*entropy) for Feature Y with probability 3 / 6 is : 0.4591479170272448\n",
      "\n",
      "************************\n",
      "For attribute Gender the classification is -->\n",
      "\n",
      "\tFor Feature M with total samples = 2\n",
      "\t\tFor class M and N : 1 / 2\n",
      "\t\tEntropy is:  0.430827083453526\n",
      "\t\tFor class M and Y : 1 / 2\n",
      "\t\tEntropy is:  0.430827083453526\n",
      "\tEntropy (sum((p*log2p) of all classes) for Feature M with probability 2 / 6 is : 1.0\n",
      "\tImpurity (p*entropy) for Feature M with probability 2 / 6 is : 0.3333333333333333\n",
      "\n",
      "\tFor Feature F with total samples = 4\n",
      "\t\tFor class F and Y : 2 / 4\n",
      "\t\tEntropy is:  0.5283208335737187\n",
      "\t\tFor class F and N : 2 / 4\n",
      "\t\tEntropy is:  0.5283208335737187\n",
      "\tEntropy (sum((p*log2p) of all classes) for Feature F with probability 4 / 6 is : 1.0\n",
      "\tImpurity (p*entropy) for Feature F with probability 4 / 6 is : 0.6666666666666666\n",
      "\n",
      "************************\n"
     ]
    }
   ],
   "source": [
    "impurity_of_attributes = dict()\n",
    "for every_attribute in Attributes[:-1]:\n",
    "    print(\"For attribute\",every_attribute, \"the classification is -->\")\n",
    "    input_value = dataset[every_attribute]\n",
    "    features_dict,classes_dict = node_classification(input_value)\n",
    "    impurity = node_impurity(features_dict,classes_dict)\n",
    "    impurity_of_attributes[every_attribute] = impurity\n",
    "    print(\"\\n************************\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Overall Entropy and Decrease in Impurity (Information Gain)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'N': 3, 'Y': 3}\n",
      "Total number of data :  6\n",
      "\tEntropy of N with probability 3 / 6 is : 0.5\n",
      "\tEntropy of Y with probability 3 / 6 is : 0.5\n",
      "\u001b[1m\n",
      "Overall System Entropy is :  1.0 \u001b[0m\n"
     ]
    }
   ],
   "source": [
    "Root_node_entropy = overall_entropy(classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Income': 0.9182958340544896, 'Married': 0.9182958340544896, 'Gender': 1.0}\n",
      "\n",
      " 1 .For attribute Income -->  \tImpurity (Net Entropy i.i. sum of all feature values impurity) is 0.9182958340544896\n",
      "\u001b[1m\t\t\t\tDecrease in Impurity is 0.08170416594551044 \u001b[0m\n",
      "\n",
      " 2 .For attribute Married -->  \tImpurity (Net Entropy i.i. sum of all feature values impurity) is 0.9182958340544896\n",
      "\u001b[1m\t\t\t\tDecrease in Impurity is 0.08170416594551044 \u001b[0m\n",
      "\n",
      " 3 .For attribute Gender -->  \tImpurity (Net Entropy i.i. sum of all feature values impurity) is 1.0\n",
      "\u001b[1m\t\t\t\tDecrease in Impurity is 0.0 \u001b[0m\n",
      "\u001b[1m\n",
      "Best split with highest decrease in impurity is Income \u001b[0m\n"
     ]
    }
   ],
   "source": [
    "print(impurity_of_attributes)\n",
    "decrease_in_impurity = dict()\n",
    "n=1\n",
    "for every_impurity in impurity_of_attributes.keys():\n",
    "    print(\"\\n\",n, \".For attribute\",every_impurity, \"-->  \\tImpurity (Net Entropy i.i. sum of all feature values impurity) is\", impurity_of_attributes[every_impurity])\n",
    "    dec_impurity = Root_node_entropy - impurity_of_attributes[every_impurity]\n",
    "    print(\"\\033[1m\\t\\t\\t\\tDecrease in Impurity is\", dec_impurity, \"\\033[0m\")\n",
    "    decrease_in_impurity[every_impurity] = dec_impurity\n",
    "    n +=1\n",
    "    \n",
    "max_dec_impurity = max(decrease_in_impurity, key=decrease_in_impurity.get)\n",
    "print(\"\\033[1m\\nBest split with highest decrease in impurity is\", max_dec_impurity, \"\\033[0m\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Overall Error Rate"
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
      "{'L': 3, 'H': 3}\n",
      "{'L and N': 1, 'L and Y': 2, 'H and N': 2, 'H and Y': 1} \n",
      "\n",
      "L has 3 samples\n",
      "\tError of L with e(t)/n(t) i.e. 1 / 3 is : 0.3333333333333333\n",
      "H has 3 samples\n",
      "\tError of H with e(t)/n(t) i.e. 1 / 3 is : 0.3333333333333333\n",
      "\u001b[1m\n",
      "Overall error rate with Attributes Income as parent node =  0.6666666666666666 \u001b[0m\n"
     ]
    }
   ],
   "source": [
    "node = (dataset[max_dec_impurity])\n",
    "features_dict,classes_dict = node_classification(node)\n",
    "Error = overall_error_rate(features_dict,classes_dict)\n",
    "print(\"\\033[1m\\nOverall error rate with Attributes\", max_dec_impurity, \"as parent node = \", Error, \"\\033[0m\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Gain Ratio or Normalized Impurity Decrease \n",
    "Gain Ratio of an attribute is decrease in impurity of that attribute divided by entropy of that attribute(without doing dub-sivision with class)\n",
    "GR(S,A) = Information_Gain( S,A)/ IntI(S,A)"
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
      "\u001b[1m\n",
      "For attribute Income Gain ratio is 0.08170416594551044 \u001b[0m\n",
      "\u001b[1m\n",
      "For attribute Married Gain ratio is 0.08170416594551044 \u001b[0m\n",
      "\u001b[1m\n",
      "For attribute Gender Gain ratio is 0.0 \u001b[0m\n"
     ]
    }
   ],
   "source": [
    "for every_attribute in decrease_in_impurity.keys():\n",
    "    input_value = dataset[every_attribute]\n",
    "    node_entropy_Edt = node_entropy(input_value)\n",
    "    gain_ratio = decrease_in_impurity[every_attribute]/node_entropy_Edt\n",
    "    print(\"\\033[1m\\nFor attribute\",every_attribute , \"Gain ratio is\", gain_ratio, \"\\033[0m\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Decision Tree with best split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/svg+xml": [
       "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n",
       "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n",
       " \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n",
       "<!-- Generated by graphviz version 2.38.0 (20140413.2041)\r\n",
       " -->\r\n",
       "<!-- Title: Tree Pages: 1 -->\r\n",
       "<svg width=\"470pt\" height=\"314pt\"\r\n",
       " viewBox=\"0.00 0.00 470.00 314.00\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n",
       "<g id=\"graph0\" class=\"graph\" transform=\"scale(1 1) rotate(0) translate(4 310)\">\r\n",
       "<title>Tree</title>\r\n",
       "<polygon fill=\"white\" stroke=\"none\" points=\"-4,4 -4,-310 466,-310 466,4 -4,4\"/>\r\n",
       "<!-- 0 -->\r\n",
       "<g id=\"node1\" class=\"node\"><title>0</title>\r\n",
       "<path fill=\"#ffffff\" stroke=\"black\" d=\"M269,-306C269,-306 193,-306 193,-306 187,-306 181,-300 181,-294 181,-294 181,-235 181,-235 181,-229 187,-223 193,-223 193,-223 269,-223 269,-223 275,-223 281,-229 281,-235 281,-235 281,-294 281,-294 281,-300 275,-306 269,-306\"/>\r\n",
       "<text text-anchor=\"start\" x=\"189\" y=\"-290.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">Income ≤ 0.5</text>\r\n",
       "<text text-anchor=\"start\" x=\"189\" y=\"-275.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 1.0</text>\r\n",
       "<text text-anchor=\"start\" x=\"191.5\" y=\"-260.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 6</text>\r\n",
       "<text text-anchor=\"start\" x=\"190.5\" y=\"-245.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [3, 3]</text>\r\n",
       "<text text-anchor=\"start\" x=\"201.5\" y=\"-230.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = N</text>\r\n",
       "</g>\r\n",
       "<!-- 1 -->\r\n",
       "<g id=\"node2\" class=\"node\"><title>1</title>\r\n",
       "<path fill=\"#f2c09c\" stroke=\"black\" d=\"M210,-187C210,-187 118,-187 118,-187 112,-187 106,-181 106,-175 106,-175 106,-116 106,-116 106,-110 112,-104 118,-104 118,-104 210,-104 210,-104 216,-104 222,-110 222,-116 222,-116 222,-175 222,-175 222,-181 216,-187 210,-187\"/>\r\n",
       "<text text-anchor=\"start\" x=\"122\" y=\"-171.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">Gender ≤ 0.5</text>\r\n",
       "<text text-anchor=\"start\" x=\"114\" y=\"-156.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 0.918</text>\r\n",
       "<text text-anchor=\"start\" x=\"124.5\" y=\"-141.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 3</text>\r\n",
       "<text text-anchor=\"start\" x=\"123.5\" y=\"-126.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [2, 1]</text>\r\n",
       "<text text-anchor=\"start\" x=\"134.5\" y=\"-111.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = N</text>\r\n",
       "</g>\r\n",
       "<!-- 0&#45;&gt;1 -->\r\n",
       "<g id=\"edge1\" class=\"edge\"><title>0&#45;&gt;1</title>\r\n",
       "<path fill=\"none\" stroke=\"black\" d=\"M207.755,-222.907C202.766,-214.195 197.441,-204.897 192.285,-195.893\"/>\r\n",
       "<polygon fill=\"black\" stroke=\"black\" points=\"195.211,-193.959 187.204,-187.021 189.136,-197.438 195.211,-193.959\"/>\r\n",
       "<text text-anchor=\"middle\" x=\"180.648\" y=\"-207.446\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">True</text>\r\n",
       "</g>\r\n",
       "<!-- 4 -->\r\n",
       "<g id=\"node5\" class=\"node\"><title>4</title>\r\n",
       "<path fill=\"#9ccef2\" stroke=\"black\" d=\"M344,-187C344,-187 252,-187 252,-187 246,-187 240,-181 240,-175 240,-175 240,-116 240,-116 240,-110 246,-104 252,-104 252,-104 344,-104 344,-104 350,-104 356,-110 356,-116 356,-116 356,-175 356,-175 356,-181 350,-187 344,-187\"/>\r\n",
       "<text text-anchor=\"start\" x=\"256\" y=\"-171.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">Gender ≤ 0.5</text>\r\n",
       "<text text-anchor=\"start\" x=\"248\" y=\"-156.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 0.918</text>\r\n",
       "<text text-anchor=\"start\" x=\"258.5\" y=\"-141.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 3</text>\r\n",
       "<text text-anchor=\"start\" x=\"257.5\" y=\"-126.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [1, 2]</text>\r\n",
       "<text text-anchor=\"start\" x=\"269\" y=\"-111.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = Y</text>\r\n",
       "</g>\r\n",
       "<!-- 0&#45;&gt;4 -->\r\n",
       "<g id=\"edge4\" class=\"edge\"><title>0&#45;&gt;4</title>\r\n",
       "<path fill=\"none\" stroke=\"black\" d=\"M254.245,-222.907C259.234,-214.195 264.559,-204.897 269.715,-195.893\"/>\r\n",
       "<polygon fill=\"black\" stroke=\"black\" points=\"272.864,-197.438 274.796,-187.021 266.789,-193.959 272.864,-197.438\"/>\r\n",
       "<text text-anchor=\"middle\" x=\"281.352\" y=\"-207.446\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">False</text>\r\n",
       "</g>\r\n",
       "<!-- 2 -->\r\n",
       "<g id=\"node3\" class=\"node\"><title>2</title>\r\n",
       "<path fill=\"#e58139\" stroke=\"black\" d=\"M88,-68C88,-68 12,-68 12,-68 6,-68 0,-62 0,-56 0,-56 0,-12 0,-12 0,-6 6,-0 12,-0 12,-0 88,-0 88,-0 94,-0 100,-6 100,-12 100,-12 100,-56 100,-56 100,-62 94,-68 88,-68\"/>\r\n",
       "<text text-anchor=\"start\" x=\"8\" y=\"-52.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 0.0</text>\r\n",
       "<text text-anchor=\"start\" x=\"10.5\" y=\"-37.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 2</text>\r\n",
       "<text text-anchor=\"start\" x=\"9.5\" y=\"-22.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [2, 0]</text>\r\n",
       "<text text-anchor=\"start\" x=\"20.5\" y=\"-7.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = N</text>\r\n",
       "</g>\r\n",
       "<!-- 1&#45;&gt;2 -->\r\n",
       "<g id=\"edge2\" class=\"edge\"><title>1&#45;&gt;2</title>\r\n",
       "<path fill=\"none\" stroke=\"black\" d=\"M121.551,-103.726C111.865,-94.423 101.579,-84.5428 91.9157,-75.2612\"/>\r\n",
       "<polygon fill=\"black\" stroke=\"black\" points=\"94.3046,-72.7027 84.6681,-68.2996 89.4555,-77.7511 94.3046,-72.7027\"/>\r\n",
       "</g>\r\n",
       "<!-- 3 -->\r\n",
       "<g id=\"node4\" class=\"node\"><title>3</title>\r\n",
       "<path fill=\"#399de5\" stroke=\"black\" d=\"M206,-68C206,-68 130,-68 130,-68 124,-68 118,-62 118,-56 118,-56 118,-12 118,-12 118,-6 124,-0 130,-0 130,-0 206,-0 206,-0 212,-0 218,-6 218,-12 218,-12 218,-56 218,-56 218,-62 212,-68 206,-68\"/>\r\n",
       "<text text-anchor=\"start\" x=\"126\" y=\"-52.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 0.0</text>\r\n",
       "<text text-anchor=\"start\" x=\"128.5\" y=\"-37.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 1</text>\r\n",
       "<text text-anchor=\"start\" x=\"127.5\" y=\"-22.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [0, 1]</text>\r\n",
       "<text text-anchor=\"start\" x=\"139\" y=\"-7.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = Y</text>\r\n",
       "</g>\r\n",
       "<!-- 1&#45;&gt;3 -->\r\n",
       "<g id=\"edge3\" class=\"edge\"><title>1&#45;&gt;3</title>\r\n",
       "<path fill=\"none\" stroke=\"black\" d=\"M165.489,-103.726C165.789,-95.5175 166.106,-86.8595 166.409,-78.56\"/>\r\n",
       "<polygon fill=\"black\" stroke=\"black\" points=\"169.916,-78.4207 166.784,-68.2996 162.921,-78.1651 169.916,-78.4207\"/>\r\n",
       "</g>\r\n",
       "<!-- 5 -->\r\n",
       "<g id=\"node6\" class=\"node\"><title>5</title>\r\n",
       "<path fill=\"#399de5\" stroke=\"black\" d=\"M332,-68C332,-68 256,-68 256,-68 250,-68 244,-62 244,-56 244,-56 244,-12 244,-12 244,-6 250,-0 256,-0 256,-0 332,-0 332,-0 338,-0 344,-6 344,-12 344,-12 344,-56 344,-56 344,-62 338,-68 332,-68\"/>\r\n",
       "<text text-anchor=\"start\" x=\"252\" y=\"-52.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 0.0</text>\r\n",
       "<text text-anchor=\"start\" x=\"254.5\" y=\"-37.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 2</text>\r\n",
       "<text text-anchor=\"start\" x=\"253.5\" y=\"-22.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [0, 2]</text>\r\n",
       "<text text-anchor=\"start\" x=\"265\" y=\"-7.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = Y</text>\r\n",
       "</g>\r\n",
       "<!-- 4&#45;&gt;5 -->\r\n",
       "<g id=\"edge5\" class=\"edge\"><title>4&#45;&gt;5</title>\r\n",
       "<path fill=\"none\" stroke=\"black\" d=\"M296.511,-103.726C296.211,-95.5175 295.894,-86.8595 295.591,-78.56\"/>\r\n",
       "<polygon fill=\"black\" stroke=\"black\" points=\"299.079,-78.1651 295.216,-68.2996 292.084,-78.4207 299.079,-78.1651\"/>\r\n",
       "</g>\r\n",
       "<!-- 6 -->\r\n",
       "<g id=\"node7\" class=\"node\"><title>6</title>\r\n",
       "<path fill=\"#e58139\" stroke=\"black\" d=\"M450,-68C450,-68 374,-68 374,-68 368,-68 362,-62 362,-56 362,-56 362,-12 362,-12 362,-6 368,-0 374,-0 374,-0 450,-0 450,-0 456,-0 462,-6 462,-12 462,-12 462,-56 462,-56 462,-62 456,-68 450,-68\"/>\r\n",
       "<text text-anchor=\"start\" x=\"370\" y=\"-52.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">entropy = 0.0</text>\r\n",
       "<text text-anchor=\"start\" x=\"372.5\" y=\"-37.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">samples = 1</text>\r\n",
       "<text text-anchor=\"start\" x=\"371.5\" y=\"-22.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">value = [1, 0]</text>\r\n",
       "<text text-anchor=\"start\" x=\"382.5\" y=\"-7.8\" font-family=\"Helvetica,sans-Serif\" font-size=\"14.00\">class = N</text>\r\n",
       "</g>\r\n",
       "<!-- 4&#45;&gt;6 -->\r\n",
       "<g id=\"edge6\" class=\"edge\"><title>4&#45;&gt;6</title>\r\n",
       "<path fill=\"none\" stroke=\"black\" d=\"M340.449,-103.726C350.135,-94.423 360.421,-84.5428 370.084,-75.2612\"/>\r\n",
       "<polygon fill=\"black\" stroke=\"black\" points=\"372.544,-77.7511 377.332,-68.2996 367.695,-72.7027 372.544,-77.7511\"/>\r\n",
       "</g>\r\n",
       "</g>\r\n",
       "</svg>\r\n"
      ],
      "text/plain": [
       "<graphviz.files.Source at 0x1e896976d90>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import tree\n",
    "from sklearn import preprocessing\n",
    "\n",
    "#label encoding for changing string values to numerical\n",
    "label_encoder = preprocessing.LabelEncoder()\n",
    "for attribute in Attributes :\n",
    "    dataset[attribute]= label_encoder.fit_transform(dataset[attribute])  \n",
    "    \n",
    "#spliting train and test data\n",
    "train_data = dataset[Attributes[:-1]]\n",
    "test_data = dataset[Attributes[-1]]\n",
    "#print(train_data)\n",
    "#print(test_data)\n",
    "\n",
    "#train classifier\n",
    "\n",
    "clf = tree.DecisionTreeClassifier(criterion='entropy')\n",
    "clf=clf.fit(train_data,test_data)\n",
    "\n",
    "#draw tree\n",
    "\n",
    "import graphviz\n",
    "dot_data = tree.export_graphviz(clf, \n",
    "                                out_file=None,\n",
    "                                feature_names=Attributes[:-1],\n",
    "                                class_names=classes_name,\n",
    "                                filled=True, \n",
    "                                rounded=True,\n",
    "                                special_characters=True)  \n",
    "graph = graphviz.Source(dot_data)\n",
    "graph"
   ]
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
