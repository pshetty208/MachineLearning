{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### For CSV file:\n",
    "1. In Transition CSV, the transition is row wise. \n",
    "d_transition_prob = {'Unnamed: 0': ['H', 'L'], \n",
    "    H': [H|H, H|L], \n",
    "    L' : [L|H,L|L]}"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "import math\n",
    "emission_prob = pd.read_csv(\"emission.csv\", header = 0)\n",
    "start_prob = pd.read_csv(\"start.csv\", header = 0)\n",
    "transition_prob = pd.read_csv(\"transition.csv\", header = 0)\n",
    "order = ['Dizzy','Cold','Cold','Normal']\n",
    "\n",
    "print(emission_prob)\n",
    "print(start_prob)\n",
    "print(transition_prob)\n"
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
      "0       Warm  0.7      0.3\n",
      "1       Cold  0.3      0.7\n",
      "   Warm  Cold\n",
      "0   0.8   0.2\n",
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
    "d_emission_prob = {'Unnamed: 0': ['Warm', 'Cold'], \n",
    "                 'Run': [0.7, 0.3], \n",
    "                 'Netflix' : [0.3,0.7]}\n",
    "emission_prob = pd.DataFrame(data=d_emission_prob)\n",
    "\n",
    "d_start_prob = {'Warm': [0.8], \n",
    "                 'Cold': [0.2]}\n",
    "start_prob = pd.DataFrame(data=d_start_prob)\n",
    "\n",
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
      "{'Run and Warm': 0.7, 'Run and Cold': 0.3, 'Netflix and Warm': 0.3, 'Netflix and Cold': 0.7}\n"
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
      "{'Warm': 0.8, 'Cold': 0.2}\n"
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
      "\t 1 . Warm = -1.4271163556401458\n",
      "\t 2 . Cold = -1.9661128563728327\n",
      "\n",
      "\n",
      "3 . Warm = -1.4271163556401458\n",
      "4 . Cold = -1.9661128563728327\n",
      "*******************************\n",
      "\n",
      "For State 2 : Netflix\n",
      "\tFor class Warm\n",
      "\t 5 . Warm to Warm  i.e. P( Warm|Warm ) = -1.4271163556401458 + log( 0.8 )+ log( 0.3 ) =  -2.8542327112802917\n",
      "\t 6 . Cold to Warm  i.e. P( Warm|Cold ) = -1.9661128563728327 + log( 0.2 )+ log( 0.3 ) =  -4.779523573132869\n",
      "\tFor class Cold\n",
      "\t 7 . Warm to Cold  i.e. P( Cold|Warm ) = -1.4271163556401458 + log( 0.2 )+ log( 0.7 ) =  -3.3932292120129786\n",
      "\t 8 . Cold to Cold  i.e. P( Cold|Cold ) = -1.9661128563728327 + log( 0.8 )+ log( 0.7 ) =  -2.545931351625775\n",
      "9 . Warm = -2.8542327112802917\n",
      "10 . Cold = -2.545931351625775\n",
      "*******************************\n",
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
    "    prob = math.log(start_dict[every_class]) + math.log(emission_dict[key_name])\n",
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
    "            prob = previous_state[every_class2] + math.log(emission_dict[key_2]) + math.log(transition_dict[key_1])\n",
    "            print(\"\\t\", p, \".\", every_class2 ,\"to\", every_class1,\" i.e. P(\",key_1,\") =\", previous_state[every_class2] ,\"+ log(\",transition_dict[key_1],\")+ log(\", emission_dict[key_2],\") = \", prob)\n",
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
