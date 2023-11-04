{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dunn  Index and Silhouette Coefficient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#cluster 1 - datapoints\n",
    "c1 = [(0.129032,0.25),\n",
    "      (0.838710,0.12),\n",
    "      (0.387097,0.0),\n",
    "      (1,0.40)]\n",
    "\n",
    "#cluster 2 - datapoints\n",
    "c2 = [(0.225806,0.50),    \n",
    "      (0.516129,0.24),\n",
    "      (0.935484,0.7),\n",
    "      (0,0.65),\n",
    "      (0.032258,1)]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def distance(p2):\n",
    "    p1_1 = 0.574\n",
    "    p1_2 = 0.336\n",
    "    dist = (p2[0]-p1_1)**2+(p2[1]-p1_2)**2\n",
    "    print(dist)\n",
    "    return dist\n",
    "\n",
    "def distance1(p2):\n",
    "    p1_1 = 0.602\n",
    "    p1_2 = 0.483\n",
    "    dist = (p2[0]-p1_1)**2+(p2[1]-p1_2)**2\n",
    "    print(dist)\n",
    "    return dist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0.129032, 0.25)\n",
      "0.20539252102399994\n",
      "(0.83871, 0.12)\n",
      "0.1167273841\n",
      "(0.387097, 0.0)\n",
      "0.147828731409\n",
      "(1, 0.4)\n",
      "0.18557200000000001\n",
      "(0.129032, 0.25)\n",
      "0.27798772902399993\n",
      "(0.83871, 0.12)\n",
      "0.18780062409999998\n",
      "(0.387097, 0.0)\n",
      "0.279472299409\n",
      "(1, 0.4)\n",
      "0.16529300000000002\n"
     ]
    }
   ],
   "source": [
    "for p in c1 :\n",
    "    print(p)\n",
    "    distance(p)\n",
    "\n",
    "for p in c1 :\n",
    "    print(p)\n",
    "    distance1(p)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "def intra_distance(c):\n",
    "    e = 0.0\n",
    "    dist_intra = []\n",
    "    for i in range(len(c)-1):\n",
    "        for j in range(i+1,len(c)):\n",
    "            e += pow((float(c[i][0])-float(c[j][0])),2)  #euclidean distance\n",
    "            e += pow((float(c[i][1])-float(c[j][1])),2)\n",
    "            e = np.sqrt(e)\n",
    "            dist_intra.append(e)\n",
    "            print(\"Distance between points (\",c[i][0],\",\",c[i][1],\") & (\",c[j][0],\",\",c[j][1],\") is :\",e)\n",
    "            e = 0.0\n",
    "    print(\"-----------------------------------------------\")\n",
    "    return dist_intra\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def inter_distance(c1,c2):\n",
    "    dist = 0.0\n",
    "    dist_inter = []\n",
    "    for point1 in c1:\n",
    "        for point2 in c2:\n",
    "            dist += pow((float(point1[0])-float(point2[0])),2)  #euclidean distance\n",
    "            dist += pow((float(point1[1])-float(point2[1])),2)\n",
    "            dist = np.sqrt(dist)\n",
    "            print(\"Distance between points\",point1,\"&\",point2,\" is :\",dist)\n",
    "            dist_inter.append(dist)\n",
    "            dist = 0.0 \n",
    "    print(\"-----------------------------------------------\")\n",
    "    return dist_inter"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dunn Index"
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
      "Distance between points (0.129032, 0.25) & (0.225806, 0.5)  is : 0.2680768678495032\n",
      "Distance between points (0.129032, 0.25) & (0.516129, 0.24)  is : 0.3872261450483424\n",
      "Distance between points (0.129032, 0.25) & (0.935484, 0.7)  is : 0.9235068101015822\n",
      "Distance between points (0.129032, 0.25) & (0, 0.65)  is : 0.4202966298032855\n",
      "Distance between points (0.129032, 0.25) & (0.032258, 1)  is : 0.7562176982033678\n",
      "Distance between points (0.83871, 0.12) & (0.225806, 0.5)  is : 0.7211458335288361\n",
      "Distance between points (0.83871, 0.12) & (0.516129, 0.24)  is : 0.3441780085377333\n",
      "Distance between points (0.83871, 0.12) & (0.935484, 0.7)  is : 0.5880180329513713\n",
      "Distance between points (0.83871, 0.12) & (0, 0.65)  is : 0.9921363132654706\n",
      "Distance between points (0.83871, 0.12) & (0.032258, 1)  is : 1.193635131982969\n",
      "Distance between points (0.387097, 0.0) & (0.225806, 0.5)  is : 0.5253710942571926\n",
      "Distance between points (0.387097, 0.0) & (0.516129, 0.24)  is : 0.27248716854927313\n",
      "Distance between points (0.387097, 0.0) & (0.935484, 0.7)  is : 0.8892290491032104\n",
      "Distance between points (0.387097, 0.0) & (0, 0.65)  is : 0.7565342605652436\n",
      "Distance between points (0.387097, 0.0) & (0.032258, 1)  is : 1.0610894005318308\n",
      "Distance between points (1, 0.4) & (0.225806, 0.5)  is : 0.7806256142582051\n",
      "Distance between points (1, 0.4) & (0.516129, 0.24)  is : 0.5096382488010491\n",
      "Distance between points (1, 0.4) & (0.935484, 0.7)  is : 0.30685878552845763\n",
      "Distance between points (1, 0.4) & (0, 0.65)  is : 1.0307764064044151\n",
      "Distance between points (1, 0.4) & (0.032258, 1)  is : 1.1386503320001273\n",
      "-----------------------------------------------\n",
      "Distance between points (0.225806, 0.5) & (0.129032, 0.25)  is : 0.2680768678495032\n",
      "Distance between points (0.225806, 0.5) & (0.83871, 0.12)  is : 0.7211458335288361\n",
      "Distance between points (0.225806, 0.5) & (0.387097, 0.0)  is : 0.5253710942571926\n",
      "Distance between points (0.225806, 0.5) & (1, 0.4)  is : 0.7806256142582051\n",
      "Distance between points (0.516129, 0.24) & (0.129032, 0.25)  is : 0.3872261450483424\n",
      "Distance between points (0.516129, 0.24) & (0.83871, 0.12)  is : 0.3441780085377333\n",
      "Distance between points (0.516129, 0.24) & (0.387097, 0.0)  is : 0.27248716854927313\n",
      "Distance between points (0.516129, 0.24) & (1, 0.4)  is : 0.5096382488010491\n",
      "Distance between points (0.935484, 0.7) & (0.129032, 0.25)  is : 0.9235068101015822\n",
      "Distance between points (0.935484, 0.7) & (0.83871, 0.12)  is : 0.5880180329513713\n",
      "Distance between points (0.935484, 0.7) & (0.387097, 0.0)  is : 0.8892290491032104\n",
      "Distance between points (0.935484, 0.7) & (1, 0.4)  is : 0.30685878552845763\n",
      "Distance between points (0, 0.65) & (0.129032, 0.25)  is : 0.4202966298032855\n",
      "Distance between points (0, 0.65) & (0.83871, 0.12)  is : 0.9921363132654706\n",
      "Distance between points (0, 0.65) & (0.387097, 0.0)  is : 0.7565342605652436\n",
      "Distance between points (0, 0.65) & (1, 0.4)  is : 1.0307764064044151\n",
      "Distance between points (0.032258, 1) & (0.129032, 0.25)  is : 0.7562176982033678\n",
      "Distance between points (0.032258, 1) & (0.83871, 0.12)  is : 1.193635131982969\n",
      "Distance between points (0.032258, 1) & (0.387097, 0.0)  is : 1.0610894005318308\n",
      "Distance between points (0.032258, 1) & (1, 0.4)  is : 1.1386503320001273\n",
      "-----------------------------------------------\n",
      "min value: 0.2680768678495032\n",
      "Distance between points ( 0.129032 , 0.25 ) & ( 0.83871 , 0.12 ) is : 0.7214865651444938\n",
      "Distance between points ( 0.129032 , 0.25 ) & ( 0.387097 , 0.0 ) is : 0.35930146705099886\n",
      "Distance between points ( 0.129032 , 0.25 ) & ( 1 , 0.4 ) is : 0.8837902788693707\n",
      "Distance between points ( 0.83871 , 0.12 ) & ( 0.387097 , 0.0 ) is : 0.4672839626704515\n",
      "Distance between points ( 0.83871 , 0.12 ) & ( 1 , 0.4 ) is : 0.32313227028571445\n",
      "Distance between points ( 0.387097 , 0.0 ) & ( 1 , 0.4 ) is : 0.7318811976058682\n",
      "-----------------------------------------------\n",
      "Distance between points ( 0.225806 , 0.5 ) & ( 0.516129 , 0.24 ) is : 0.3897273974575049\n",
      "Distance between points ( 0.225806 , 0.5 ) & ( 0.935484 , 0.7 ) is : 0.7373214113831227\n",
      "Distance between points ( 0.225806 , 0.5 ) & ( 0 , 0.65 ) is : 0.27108734687550434\n",
      "Distance between points ( 0.225806 , 0.5 ) & ( 0.032258 , 1 ) is : 0.5361537356990064\n",
      "Distance between points ( 0.516129 , 0.24 ) & ( 0.935484 , 0.7 ) is : 0.6224617386032655\n",
      "Distance between points ( 0.516129 , 0.24 ) & ( 0 , 0.65 ) is : 0.6591579056955927\n",
      "Distance between points ( 0.516129 , 0.24 ) & ( 0.032258 , 1 ) is : 0.9009612337059791\n",
      "Distance between points ( 0.935484 , 0.7 ) & ( 0 , 0.65 ) is : 0.9368192537816459\n",
      "Distance between points ( 0.935484 , 0.7 ) & ( 0.032258 , 1 ) is : 0.9517442971071589\n",
      "Distance between points ( 0 , 0.65 ) & ( 0.032258 , 1 ) is : 0.35148339728072503\n",
      "-----------------------------------------------\n",
      "max value: 0.9517442971071589\n",
      "Dunn Index: 0.28166900360141567\n"
     ]
    }
   ],
   "source": [
    "dist_inter = inter_distance(c1,c2) + inter_distance(c2,c1)\n",
    "print(\"min value:\",min(dist_inter))\n",
    "\n",
    "dist_intra = intra_distance(c1) + intra_distance(c2) #cluster1\n",
    "print(\"max value:\",max(dist_intra))\n",
    "print(\"Dunn Index:\",min(dist_inter)/max(dist_intra))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Silhouette coefficient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def distance_point(point, c):\n",
    "    e = 0.0\n",
    "    dist_intra = []\n",
    "    for point1 in c:\n",
    "        e += pow((float(point[0])-float(point1[0])),2)  #euclidean distance\n",
    "        e += pow((float(point[1])-float(point1[1])),2)\n",
    "        e = np.sqrt(e)\n",
    "        dist_intra.append(e)\n",
    "#        print(\"\\tDistance between points\",point,\"&\",point1,\" is :\",e)\n",
    "        e = 0.0\n",
    "#    print(\"\\t-----------------------------------------------\")\n",
    "    return dist_intra\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def silhouette(cluster1, cluster2, cluster3) :\n",
    "    print(\"Silhouette coefficient objects of cluster\", cluster1)\n",
    "    for point in cluster1:\n",
    "        b_i = []\n",
    "        print(\"For point\", point)\n",
    "        c1_copy = cluster1.copy()\n",
    "        c1_copy.remove(point)\n",
    "        a_i = np.mean(distance_point(point,c1_copy))\n",
    "        print(\"Mean of cluster distance from point\", point,\"is mean(a_i) = \",a_i)\n",
    "        b_i_c2 = np.mean(distance_point(point,cluster2))\n",
    "        print(\"Mean distance from point\", point, \"to cluster\", cluster2 ,\"(d(i,cluster))\",b_i_c2)\n",
    "        b_i.append(b_i_c2)\n",
    "        b_i_c3 = np.mean(distance_point(point,cluster3))\n",
    "        print(\"Mean distance from point\", point, \"to cluster\", cluster3 ,\"(d(i,cluster))\",b_i_c3)\n",
    "        b_i.append(b_i_c3)\n",
    "        print(\"Minimum mean\",min(b_i))\n",
    "        sillhoutte = (min(b_i) - a_i)/(max(min(b_i),a_i))\n",
    "        print(\"sillhoutte:\",sillhoutte)\n",
    "        print(\"-----------------------------------------------\")\n",
    "    print(\"****************************************\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Silhouette coefficient objects of cluster [(5.5, 2), (6.5, 3)]\n",
      "For point (5.5, 2)\n",
      "Mean of cluster distance from point (5.5, 2) is mean(a_i) =  1.4142135623730951\n",
      "Mean distance from point (5.5, 2) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 3.55431431762634\n",
      "Mean distance from point (5.5, 2) to cluster [(2.5, 4), (4, 4.5), (5, 4.5), (4.5, 3.5)] (d(i,cluster)) 2.718328154353756\n",
      "Minimum mean 2.718328154353756\n",
      "sillhoutte: 0.4797487712776516\n",
      "-----------------------------------------------\n",
      "For point (6.5, 3)\n",
      "Mean of cluster distance from point (6.5, 3) is mean(a_i) =  1.4142135623730951\n",
      "Mean distance from point (6.5, 3) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 4.760741201993035\n",
      "Mean distance from point (6.5, 3) to cluster [(2.5, 4), (4, 4.5), (5, 4.5), (4.5, 3.5)] (d(i,cluster)) 2.805363682352196\n",
      "Minimum mean 2.805363682352196\n",
      "sillhoutte: 0.49588940240812973\n",
      "-----------------------------------------------\n",
      "****************************************\n",
      "Silhouette coefficient objects of cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)]\n",
      "For point (1, 1.5)\n",
      "Mean of cluster distance from point (1, 1.5) is mean(a_i) =  1.4120226591665965\n",
      "Mean distance from point (1, 1.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 1.0590169943749475\n",
      "Mean distance from point (1, 1.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 1.0590169943749475\n",
      "Minimum mean 1.0590169943749475\n",
      "sillhoutte: -0.24999999999999997\n",
      "-----------------------------------------------\n",
      "For point (2, 2)\n",
      "Mean of cluster distance from point (2, 2) is mean(a_i) =  1.0786893258332633\n",
      "Mean distance from point (2, 2) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 0.8090169943749475\n",
      "Mean distance from point (2, 2) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 0.8090169943749475\n",
      "Minimum mean 0.8090169943749475\n",
      "sillhoutte: -0.25\n",
      "-----------------------------------------------\n",
      "For point (3, 1.5)\n",
      "Mean of cluster distance from point (3, 1.5) is mean(a_i) =  1.4120226591665965\n",
      "Mean distance from point (3, 1.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 1.0590169943749475\n",
      "Mean distance from point (3, 1.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 1.0590169943749475\n",
      "Minimum mean 1.0590169943749475\n",
      "sillhoutte: -0.24999999999999997\n",
      "-----------------------------------------------\n",
      "For point (2, 1)\n",
      "Mean of cluster distance from point (2, 1) is mean(a_i) =  1.0786893258332633\n",
      "Mean distance from point (2, 1) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 0.8090169943749475\n",
      "Mean distance from point (2, 1) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 0.8090169943749475\n",
      "Minimum mean 0.8090169943749475\n",
      "sillhoutte: -0.25\n",
      "-----------------------------------------------\n",
      "****************************************\n",
      "Silhouette coefficient objects of cluster [(2.5, 4), (4, 4.5), (5, 4.5), (4.5, 3.5)]\n",
      "For point (2.5, 4)\n",
      "Mean of cluster distance from point (2.5, 4) is mean(a_i) =  2.064067133229804\n",
      "Mean distance from point (2.5, 4) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 2.6419799455442456\n",
      "Mean distance from point (2.5, 4) to cluster [(5.5, 2), (6.5, 3)] (d(i,cluster)) 3.8643284505408246\n",
      "Minimum mean 2.6419799455442456\n",
      "sillhoutte: 0.21874231607590494\n",
      "-----------------------------------------------\n",
      "For point (4, 4.5)\n",
      "Mean of cluster distance from point (4, 4.5) is mean(a_i) =  1.2330576062780283\n",
      "Mean distance from point (4, 4.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 3.6594023350383407\n",
      "Mean distance from point (4, 4.5) to cluster [(5.5, 2), (6.5, 3)] (d(i,cluster)) 2.9154759474226504\n",
      "Minimum mean 2.9154759474226504\n",
      "sillhoutte: 0.5770647302482189\n",
      "-----------------------------------------------\n",
      "For point (5, 4.5)\n",
      "Mean of cluster distance from point (5, 4.5) is mean(a_i) =  1.5558479151820956\n",
      "Mean distance from point (5, 4.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 4.28011208551594\n",
      "Mean distance from point (5, 4.5) to cluster [(5.5, 2), (6.5, 3)] (d(i,cluster)) 2.3354150501780175\n",
      "Minimum mean 2.3354150501780175\n",
      "sillhoutte: 0.33380239411255797\n",
      "-----------------------------------------------\n",
      "For point (4.5, 3.5)\n",
      "Mean of cluster distance from point (4.5, 3.5) is mean(a_i) =  1.4325402634362068\n",
      "Mean distance from point (4.5, 3.5) to cluster [(1, 1.5), (2, 2), (3, 1.5), (2, 1)] (d(i,cluster)) 3.2455346818761655\n",
      "Mean distance from point (4.5, 3.5) to cluster [(5.5, 2), (6.5, 3)] (d(i,cluster)) 1.9321642252704123\n",
      "Minimum mean 1.9321642252704123\n",
      "sillhoutte: 0.2585825548883049\n",
      "-----------------------------------------------\n",
      "****************************************\n"
     ]
    }
   ],
   "source": [
    "silhouette(c1, c2, c3)\n",
    "silhouette(c2, c1, c3)\n",
    "silhouette(c3, c2, c1)"
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
