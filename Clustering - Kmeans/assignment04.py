{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 04"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "Submitted by : Group - Kay Members:\n",
    "\n",
    "Charu Gupta (220202389)\n",
    "Priya Yadav (220200937)\n",
    "Venkatesh Hariharapura Shivashankar (220200713)\n",
    "Vibha Iyer (220200717)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load modules\n",
    "import csv\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Import"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Radius (cm)  Weight (grams) Fruit (class)\n",
      "0         65.0           325.0         Lemon\n",
      "1         68.0           350.0         Apple\n",
      "2         87.0           312.0         Lemon\n",
      "3         77.0           324.0         Apple\n",
      "4         73.0           300.0         Lemon\n",
      "5         90.0           370.0         Apple\n",
      "6         61.0           365.0         Apple\n",
      "7         62.0           400.0         Apple\n",
      "8         92.0           340.0         Lemon\n",
      "   Radius (cm)  Weight (grams) Fruit (class)\n",
      "0     0.129032            0.25         Lemon\n",
      "1     0.225806            0.50         Apple\n",
      "2     0.838710            0.12         Lemon\n",
      "3     0.516129            0.24         Apple\n",
      "4     0.387097            0.00         Lemon\n",
      "5     0.935484            0.70         Apple\n",
      "6     0.000000            0.65         Apple\n",
      "7     0.032258            1.00         Apple\n",
      "8     1.000000            0.40         Lemon\n"
     ]
    }
   ],
   "source": [
    "# Load data from CSV file\n",
    "df = pd.DataFrame()\n",
    "df = pd.read_csv('data.csv', dtype={'Radius (cm)': float, 'Weight (grams)': float})\n",
    "print(df)\n",
    "\n",
    "# Replace zero values with median value within class \n",
    "df = df.groupby(['Fruit (class)']) # sort by class\n",
    "proc_df = pd.DataFrame() # create a new dataframe to collect results\n",
    "for key, group in df: # go over groups\n",
    "    group = group.replace(0, group.median(axis=0)) # replace missing values with median\n",
    "    proc_df = pd.concat([proc_df, group]) # concatenate groups into new dataframe\n",
    "df = proc_df.sort_index() # overwrite original dataframe with results\n",
    "\n",
    "# Normalize\n",
    "radius = df['Radius (cm)']\n",
    "df['Radius (cm)'] = (radius-radius.min())/(radius.max()-radius.min())\n",
    "weight = df['Weight (grams)']\n",
    "df['Weight (grams)'] = (weight-weight.min())/(weight.max()-weight.min())\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Radius values\n",
    "radius = list(df['Radius (cm)'])\n",
    "print(radius)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Weight values\n",
    "weight = list(df['Weight (grams)'])\n",
    "print(weight)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Classes\n",
    "classes = list(df['Fruit (class)'])\n",
    "print(classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Combine radius, weight, and class to tuples (we have to keep the class for later plotting)\n",
    "tuples = list(zip(radius, weight, classes))\n",
    "print(tuples)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Clustering"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Squared Euclidean distance (use this as delta function)\n",
    "def distance(p1,p2):\n",
    "    dist = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2\n",
    "    return dist\n",
    "\n",
    "# Takes points as list of tuples and a threshold.\n",
    "# Example call: do_cluster([(2,1,'Apple'),(6,3,'Lemon'),(1,1.5,'Apple'),(2,2,'Pear')], 7)\n",
    "def do_cluster(tuples, threshold):\n",
    "    clusters = [[],[]] \n",
    "    #Initialising first object of tuple as centroid and rest as 0 \n",
    "    clusterCentroid=[[tuples[0][0],tuples[0][1]],[0,0]]\n",
    "    clusterCentroidNew=[]\n",
    "    #Putting first object from tuple in first cluster\n",
    "    clusters[0].append(tuples[0])\n",
    "    clusterNew=[]\n",
    "    #0th object is already put in cluster\n",
    "    for i in range(1,len(tuples)):\n",
    "        if(distance(tuples[i],clusterCentroid[0])<=threshold):\n",
    "            #appending particular object to first cluster\n",
    "            clusters[0].append(tuples[i])\n",
    "            lenCluster=len(clusters[0])\n",
    "            #updating centroid for first cluster\n",
    "            clusterCentroid[0]=[((tuples[i][0]/lenCluster) + (((lenCluster-1)/lenCluster)*clusterCentroid[0][0])),\n",
    "                             ((tuples[i][1]/lenCluster) + (((lenCluster-1)/lenCluster)*clusterCentroid[0][1]))]\n",
    "        else:\n",
    "            if(len(clusters[1])==0):\n",
    "                #putting object to second cluster if seconf cluster  is empty and initialising centroid for second cluster\n",
    "                clusterCentroid[1]=[tuples[i][0],tuples[i][1]]\n",
    "                clusters[1].append(tuples[i])\n",
    "            else:\n",
    "                if(distance(tuples[i],clusterCentroid[1])<=threshold):\n",
    "                    clusters[1].append(tuples[i])\n",
    "                    lenCluster=len(clusters[1])\n",
    "                    #updating cluster centroid for second cluster\n",
    "                    clusterCentroid[1]=[((tuples[i][0]/lenCluster)) + ((lenCluster-1)/lenCluster)*clusterCentroid[1][0],\n",
    "                             ((tuples[i][1]/lenCluster) + (((lenCluster-1)/lenCluster)*clusterCentroid[1][1]))]\n",
    "                else:\n",
    "                    clusterNew.append(tuples[i])\n",
    "                    #Updating cluster centroid for objects which doesnt fit in any cluster\n",
    "                    clusterCentroidNew=[tuples[i][0],tuples[i][1]]\n",
    "                    clusterCentroid.append(clusterCentroidNew)\n",
    "    clusters.append(clusterNew)\n",
    "    return clusters # e.g., [[(2, 1, 'Apple'), (1, 1.5, 'Apple'), (2, 2, 'Pear')], [(6, 3, 'Lemon')]]\n",
    "\n",
    "# Call to cluster\n",
    "\n",
    "clusters = do_cluster(tuples, 0.33) # distance threshold, aka Delta, is set to 0.33\n",
    "print(clusters)\n",
    "\n",
    "# Hint: Final clusters should look like the following:\n",
    "# [[(0.06451612903225798, 0.15037593984962405, 'Lemon'), (0.16129032258064516, 0.13533834586466165, 'Lemon'), ..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Plotting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange'] # provide some colors for the clusters\n",
    "marker = {'Lemon': '*', 'Apple': 'o', 'Pear': 'x'} # different marker for each class\n",
    "i = 0\n",
    "for c in clusters:\n",
    "    tpls = list(zip(*c))\n",
    "    x = tpls[0]\n",
    "    y = tpls[1]\n",
    "    cls = tpls[2]\n",
    "    c = colors[i%len(colors)]\n",
    "    m = [marker[cl] for cl in cls]\n",
    "    for _x, _y, _m in zip(x, y, m):\n",
    "        plt.scatter(_x, _y, c=c, marker=_m)\n",
    "    i += 1\n",
    "plt.xlabel(\"Radius\")\n",
    "plt.ylabel(\"Weight\")\n",
    "plt.show()"
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
 "nbformat_minor": 2
}
