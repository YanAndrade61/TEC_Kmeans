from kmeans import kmeans
import pandas as pd

def main():
    
    data = pd.read_csv("s02.txt")
    data = data.iloc[:,:10].to_numpy()
    
    model = kmeans(data,4)
    model.simulate()
    model.view_clusters()

main()