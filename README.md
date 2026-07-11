# SCT_ML_2 - Customer Segmentation (K-Means Clustering)

## Task
Group mall customers into segments based on purchase history using K-means clustering.

## Approach
- Dataset: Kaggle "Mall Customer Segmentation Data" (Mall_Customers.csv)
- Features used: Annual Income (k$), Spending Score (1-100)
- Model: scikit-learn KMeans
- Optimal K selected using the Elbow Method (see elbow_plot.png)

## Results
- Optimal number of clusters: K = 5
- Visualized in customer_clusters.png

## Customer Segments Identified
1. **Low income, high spending** - budget-conscious but high spenders
2. **Low income, low spending** - cautious, budget-focused shoppers
3. **Medium income, medium spending** - average/typical customers
4. **High income, high spending** - most valuable customer segment
5. **High income, low spending** - high potential, currently underspending

## How to run
1. Ensure Mall_Customers.csv is in the same folder
2. Run: python customer_clustering.py
3. Outputs: elbow_plot.png and customer_clusters.png will be generated