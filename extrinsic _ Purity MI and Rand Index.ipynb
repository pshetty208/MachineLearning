{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 3]\n",
      " [2 2]]\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "import itertools\n",
    "#for input check the notes\n",
    "\n",
    "matrix = np.array([[2,3],\n",
    "                   [2,2]])\n",
    "print(matrix)\n",
    "\n",
    "total = 0\n",
    "for every_class in matrix:\n",
    "    total = total + sum(every_class)\n",
    "print(total)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Calculate Purity "
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
      "Purity of class w 1 is = 3 / 5 = 0.6\n",
      "\t (5/9)*0.6 = 0.3333333333333333\n",
      "Purity of class w 2 is = 2 / 4 = 0.5\n",
      "\t (4/9)*0.5 = 0.2222222222222222\n",
      "Total Purity is :   + 0.3333333333333333 + 0.2222222222222222 = 0.5555555555555556\n"
     ]
    }
   ],
   "source": [
    "def cal_purity(matrix) :\n",
    "    i = 1\n",
    "    purity = 0\n",
    "    string = \"\"\n",
    "    for every_class in matrix:\n",
    "        purity_class = max(every_class)/sum(every_class)\n",
    "        print(\"Purity of class w\", i, \"is =\",max(every_class),\"/\",sum(every_class),\"=\", purity_class)\n",
    "        prob = sum(every_class)/total\n",
    "        purity = purity + prob*purity_class\n",
    "        cal = \"(\" + str(sum(every_class)) + \"/\" + str(total) + \")*\" + str(purity_class)\n",
    "        print(\"\\t\",cal, \"=\", prob*purity_class)\n",
    "        string = string + \" + \" + str(prob*purity_class)\n",
    "        i +=1\n",
    "    print(\"Total Purity is : \", string,\"=\",purity)\n",
    "\n",
    "cal_purity(matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Calculate Mutual Information"
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
      "2 * log10(( 2 * 9 )/( 5*4 )) = -0.09151498112135023\n",
      "3 * log10(( 3 * 9 )/( 5*5 )) = 0.10027126646084919\n",
      "2 * log10(( 2 * 9 )/( 4*4 )) = 0.10230504489476258\n",
      "2 * log10(( 2 * 9 )/( 4*5 )) = -0.09151498112135023\n",
      "0.0021718165681012566\n"
     ]
    }
   ],
   "source": [
    "def cal_MI(mat) :\n",
    "    MI = 0\n",
    "    for every_class in mat:\n",
    "        MI_class = 0\n",
    "        i = 0\n",
    "        for data in every_class :\n",
    "            total_o = sum(mat[:,i])\n",
    "            den = sum(every_class)*total_o\n",
    "            den_str = str(sum(every_class)) + \"*\" + str(total_o)\n",
    "            if (data == 0) :\n",
    "                continue\n",
    "            else : \n",
    "                cal = data * math.log10((data*total)/(den))\n",
    "                print(str(data), \"* log10((\",data,\"*\",total,\")/(\",den_str,\"))\",\"=\", cal)\n",
    "                MI_class = MI_class + cal \n",
    "            i += 1\n",
    "        MI = MI + MI_class\n",
    "    MI = MI * (1/total)\n",
    "    print(MI)\n",
    "\n",
    "cal_MI(matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Calculate Rand Index "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def TP_or_ss(mat) :\n",
    "    TP =0\n",
    "    for every_class in mat :\n",
    "        for data in every_class :\n",
    "            if (data == 0) :\n",
    "                continue\n",
    "            else : \n",
    "                p = itertools.combinations(range(data), 2)\n",
    "                count = 0\n",
    "                for item in p :\n",
    "                    count += 1\n",
    "                print(data,\"factorial 2 = \", count)\n",
    "            TP = TP + count\n",
    "    print(\"True Positive or SS is =\" ,TP)\n",
    "    return TP\n",
    "\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def TN_or_dd(mat):\n",
    "    TN = 0\n",
    "    for every_class in mat :\n",
    "        total_r = sum(every_class)\n",
    "        i = 0\n",
    "        for data in every_class :\n",
    "            if (data == 0) :\n",
    "                continue\n",
    "            else : \n",
    "                total_c = sum(mat[:,i])\n",
    "                count = total - (total_r + total_c - data)\n",
    "                print(str(data), \"*\", str(count), \"=\", count*data)\n",
    "                TN = TN + (count*data)\n",
    "            i += 1            \n",
    "    print(\"True Negative or Diff-diff is = \", TN)\n",
    "    return TN\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def ds(mat):\n",
    "    ds = 0\n",
    "    for every_class in mat :\n",
    "        cnt = 0\n",
    "        ds_c = 1\n",
    "        string = \"\"\n",
    "        for data in every_class :            \n",
    "            if (data != 0) :\n",
    "                cnt += 1\n",
    "                ds_c = ds_c * data\n",
    "                string = string + \"*\" + str(data)\n",
    "        if cnt <= 1 :\n",
    "            ds_c = 0\n",
    "        else :\n",
    "            print(string)\n",
    "        ds = ds + ds_c\n",
    "    print(\"DS is = \", ds)    \n",
    "    return ds\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sd(mat):\n",
    "    tran_mat = mat.transpose()\n",
    "    sd = 0\n",
    "    for every_class in tran_mat :\n",
    "        cnt = 0\n",
    "        sd_c = 1\n",
    "        string = \"\"\n",
    "        for data in every_class :\n",
    "            if (data == 0) :\n",
    "                no = 1\n",
    "            else :\n",
    "                cnt += 1\n",
    "                sd_c = sd_c * data\n",
    "                string = string + \"*\" + str(data)\n",
    "        if cnt <= 1 :\n",
    "            sd_c = 0\n",
    "        else :\n",
    "            print(string)\n",
    "        sd = sd + sd_c\n",
    "    print(\"SD is = \", sd)  \n",
    "    return sd\n"
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
      "2 factorial 2 =  1\n",
      "3 factorial 2 =  3\n",
      "2 factorial 2 =  1\n",
      "2 factorial 2 =  1\n",
      "True Positive or SS is = 6\n",
      "---------------\n",
      "2 * 2 = 4\n",
      "3 * 2 = 6\n",
      "2 * 3 = 6\n",
      "2 * 2 = 4\n",
      "True Negative or Diff-diff is =  20\n",
      "---------------\n",
      "*2*3\n",
      "*2*2\n",
      "DS is =  10\n",
      "---------------\n",
      "*2*2\n",
      "*3*2\n",
      "SD is =  10\n",
      "---------------\n"
     ]
    }
   ],
   "source": [
    "ss = TP_or_ss(matrix)\n",
    "print(\"---------------\")\n",
    "dd = TN_or_dd(matrix) \n",
    "print(\"---------------\")\n",
    "ds = ds(matrix)\n",
    "print(\"---------------\")\n",
    "sd = sd(matrix)\n",
    "print(\"---------------\")"
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
      "Rand Index is 26 / 46 = 0.5652173913043478\n"
     ]
    }
   ],
   "source": [
    "Rand_Index = (ss+dd)/(ss+dd+ds+sd)\n",
    "\n",
    "print(\"Rand Index is\", str(ss+dd), \"/\", str(ss+dd+ds+sd), \"=\", Rand_Index)"
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
