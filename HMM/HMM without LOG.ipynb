{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### For CSV file:\n",
    "1. In Transition CSV, the transition is row wise. Eg row1 is Healthy then column1,row 1 is P(H|H) and column2,row 1 is P(H|F)"
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
      "  Unnamed: 0  Run  Netflix\n",
      "0       Warm  0.6      0.4\n",
      "1       Cold  0.4      0.6\n",
      "   Warm  Cold\n",
      "0   0.5   0.5\n",
      "  Unnamed: 0  Warm  Cold\n",
      "0       Warm   0.8   0.2\n",
      "1       Cold   0.2   0.8\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import math\n",
    "#emission_prob = pd.read_csv(\"emission.csv\", header = 0)\n",
    "#start_prob = pd.read_csv(\"start.csv\", header = 0)\n",
    "#transition_prob = pd.read_csv(\"transition.csv\", header = 0)\n",
    "order = ['Netflix','Netflix']\n",
    "\n",
    "\n",
    "#Write 1st row as transitions and 1st column as states\n",
    "d_emission_prob = {'Unnamed: 0': ['Warm', 'Cold'], \n",
    "                 'Run': [0.6, 0.4], \n",
    "                 'Netflix' : [0.4,0.6]}\n",
    "emission_prob = pd.DataFrame(data=d_emission_prob)\n",
    "\n",
    "#Write in order given in question, eg 1st is Warm and 2nd is Cold\n",
    "d_start_prob = {'Warm': [0.5], \n",
    "                 'Cold': [0.5]}\n",
    "start_prob = pd.DataFrame(data=d_start_prob)\n",
    "\n",
    "#d_transition_prob = {'Unnamed: 0': ['H', 'L'], \n",
    "#                 'H': [H|H, H|L], \n",
    "#                 'L' : [L|H,L|L]}\n",
    "d_transition_prob = {'Unnamed: 0': ['Warm', 'Cold'], \n",
    "                 'Warm': [0.8, 0.2], \n",
    "                 'Cold' : [0.2,0.8]}\n",
    "transition_prob = pd.DataFrame(data=d_transition_prob)\n",
    "\n",
    "print(emission_prob)\n",
    "print(start_prob)\n",
    "print(transition_prob)\n"
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
      "['Unnamed: 0', 'Run', 'Netflix']\n",
      "['Warm', 'Cold']\n",
      "['Run', 'Netflix']\n"
     ]
    }
   ],
   "source": [
    "column_names = list(emission_prob.columns)\n",
    "print(column_names)\n",
    "classes = list(emission_prob[column_names[0]])\n",
    "print(classes)\n",
    "States = list(column_names[1:])\n",
    "print(States)"
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
      "{'Run and Warm': 0.6, 'Run and Cold': 0.4, 'Netflix and Warm': 0.4, 'Netflix and Cold': 0.6}\n"
     ]
    }
   ],
   "source": [
    "emission_dict = dict()\n",
    "for columns in column_names[1:]:\n",
    "#    print(emission_prob[columns])\n",
    "    i=0\n",
    "    for every_prob in emission_prob[columns]:\n",
    "#        print(classes[i])\n",
    "        key_name = columns + \" and \" + classes[i]\n",
    "#        print(key_name)\n",
    "        emission_dict[key_name] = every_prob\n",
    "#        print(emission_dict)\n",
    "        i +=1\n",
    "print(emission_dict)"
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
      "{'Warm|Warm': 0.8, 'Warm|Cold': 0.2, 'Cold|Warm': 0.2, 'Cold|Cold': 0.8}\n"
     ]
    }
   ],
   "source": [
    "classes_tran = list(transition_prob[column_names[0]])\n",
    "#print(classes_tran)\n",
    "transition_dict = dict()\n",
    "for every_class in classes:\n",
    "#    print(emission_prob[columns])\n",
    "    i=0\n",
    "    for every_prob in transition_prob[every_class]:\n",
    "#        print(classes_tran[i])\n",
    "#        print(every_class)\n",
    "#        print(transition_prob[i,0])\n",
    "        key_name = every_class + \"|\" + classes_tran[i]\n",
    "#        print(key_name)\n",
    "#        print(every_prob)\n",
    "        transition_dict[key_name] = every_prob\n",
    "#        print(transition_dict)\n",
    "        i +=1\n",
    "print(transition_dict)"
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
      "{'Warm': 0.5, 'Cold': 0.5}\n"
     ]
    }
   ],
   "source": [
    "start_dict = dict()\n",
    "for every_class in start_prob:    \n",
    "    for every_prob in start_prob[every_class]:\n",
    "        start_dict[every_class] = every_prob\n",
    "print(start_dict)"
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
      "For State 1 : Netflix\n",
      "\t 1 . Warm = 0.2\n",
      "\t 2 . Cold = 0.3\n",
      "\n",
      "\n",
      "3 . Warm = 0.2\n",
      "4 . Cold = 0.3\n",
      "*******************************\n",
      "\n",
      "For State 2 : Netflix\n",
      "\tFor class Warm\n",
      "\t 5 . Warm Warm = 0.06400000000000002\n",
      "\t 6 . Cold Warm = 0.024\n",
      "\tFor class Cold\n",
      "\t 7 . Warm Cold = 0.024\n",
      "\t 8 . Cold Cold = 0.144\n",
      "9 . Warm = 0.06400000000000002\n",
      "10 . Cold = 0.144\n",
      "*******************************\n",
      "0.144\n",
      "{'Order List 1': 'WarmWarm', 'Order List 2': 'ColdCold'}\n"
     ]
    }
   ],
   "source": [
    "order_dict = dict()\n",
    "p=1\n",
    "state_prob = dict()\n",
    "print(\"For State 1 :\", order[0])\n",
    "for every_class in start_dict.keys():\n",
    "    key_name = order[0] + \" and \" + every_class\n",
    "    prob = start_dict[every_class] * emission_dict[key_name]\n",
    "    state_prob[every_class] = prob\n",
    "    print(\"\\t\", p, \".\", every_class,\"=\", prob)\n",
    "    p +=1\n",
    "    \n",
    "print(\"\\n\")\n",
    "for state in state_prob.keys() :\n",
    "    print(p, \".\", state,\"=\", state_prob[state])\n",
    "    p +=1\n",
    "    \n",
    "i = 0\n",
    "previous_state = dict()\n",
    "print(\"*******************************\")\n",
    "for state in order[1:]:\n",
    "    if(i==0) :\n",
    "        previous_state = state_prob.copy()\n",
    "    else:\n",
    "        previous_state = previous_state1.copy()\n",
    "    previous_state1 = dict()\n",
    "    print(\"\\nFor State\",i+2,\":\",state)\n",
    "    n =1\n",
    "    for every_class1 in start_dict.keys():\n",
    "        print(\"\\tFor class\", every_class1)\n",
    "        maximum_prob = dict()\n",
    "        for every_class2 in start_dict.keys():\n",
    "            key_1 = every_class1 + \"|\" + every_class2\n",
    "            key_2 = state + \" and \" + every_class1\n",
    "            prob = previous_state[every_class2] * emission_dict[key_2] * transition_dict[key_1]\n",
    "            print(\"\\t\", p, \".\", every_class2 , every_class1,\"=\", prob)\n",
    "            p +=1\n",
    "            maximum_prob[every_class2] = prob\n",
    "        max_key = max(maximum_prob, key=maximum_prob.get) \n",
    "        previous_state1[every_class1] = maximum_prob[max_key]\n",
    "        key_name = \"Order List \" + str(n)\n",
    "        isPresent = key_name in order_dict\n",
    "        if(isPresent == False):\n",
    "            probable =  max_key + every_class1\n",
    "            order_dict[key_name] = probable\n",
    "        else :\n",
    "            probable =  max_key\n",
    "            order_dict[key_name] = order_dict[key_name] + probable\n",
    "        n += 1\n",
    "    for state in previous_state1.keys() :\n",
    "        print( p, \".\", state,\"=\", previous_state1[state])\n",
    "        p +=1\n",
    "    i +=1 \n",
    "    print(\"*******************************\")\n",
    "max_key = max(previous_state1, key=previous_state1.get) \n",
    "print(previous_state1[max_key])\n",
    "print(order_dict)\n"
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
