import pandas as pd 
import numpy as np
from matplotlib import pyplot
from scipy.stats import norm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns

class Univariate():
    def quanqual(dataset):
        qual = []
        quan = []
        for columnName in dataset.columns:
            if (dataset[columnName].dtype == 'O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
       
    def unidesc(dataset,quan):
        descriptive = pd.DataFrame(index = ["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%",
                                                     "Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max","Kurtosis","Skew","Var","STD"],columns = quan)
        for columnName in quan:
            descriptive[columnName]["Mean"] = dataset[columnName].mean()
            descriptive[columnName]["Median"] = dataset[columnName].median()
            descriptive[columnName]["Mode"] = dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"] = dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"] = dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"] = dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"] = np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"] = dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"] = descriptive[columnName]["Q3:75%"]- descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5Rule"] = 1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"] = descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5Rule"]
            descriptive[columnName]["Greater"] = descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5Rule"]
            descriptive[columnName]["Min"] = dataset.describe()[columnName]["min"]
            descriptive[columnName]["Max"] = dataset.describe()[columnName]["max"]
            descriptive[columnName]["Kurtosis"] = dataset[columnName].kurtosis()
            descriptive[columnName]["Skew"] = dataset[columnName].skew()
            descriptive[columnName]["Var"] = dataset[columnName].var()
            descriptive[columnName]["STD"] = dataset[columnName].std()
        return descriptive
        
    def findingoutlier(quan,descriptive):
        lesser = []
        greater = []
        for columnName in quan:
            if(descriptive[columnName]["Min"] <  descriptive[columnName]["Lesser"]):
                print("Lesser Outlier present in the column",columnName)
                lesser.append(columnName)
            if(descriptive[columnName]["Max"] >  descriptive[columnName]["Greater"]):
                print("Greater Outlier present in the column",columnName)
                greater.append(columnName)
        return lesser, greater
        
    def replacingoutlier(dataset,descriptive,lesser,greater):
        for columnName in lesser:
            dataset[columnName][dataset[columnName] < descriptive[columnName]["Lesser"]] =  descriptive[columnName]["Lesser"]
                    
        for columnName in greater:
            dataset[columnName][dataset[columnName] > descriptive[columnName]["Greater"]] =  descriptive[columnName]["Greater"]
        return dataset

    def freqTable(columnName,dataset):
        freqTable = pd.DataFrame(columns = ["Univariate","Frequency","RelativeFrequency","Cumsum"])
        freqTable["Univariate"] = dataset[columnName].value_counts().index
        freqTable["Frequency"] = dataset[columnName].value_counts().values
        freqTable["RelativeFrequency"] = freqTable["Frequency"]/103
        freqTable["Cumsum"] = freqTable["RelativeFrequency"].cumsum()
        return freqTable

    def get_pdf_probability(dataset,startrange,endrange):
        ax = sns.distplot(dataset,kde=True,kde_kws={'color':'blue'},color='Green')
        pyplot.axvline(startrange,color='Red')
        pyplot.axvline(endrange,color='Red')
        # generate a sample
        sample = dataset
        # calculate parameters
        sample_mean =sample.mean()
        sample_std = sample.std()
        print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))
        # define the distribution
        dist = norm(sample_mean, sample_std)
        
        # sample probabilities for a range of outcomes
        values = [value for value in range(startrange, endrange)]
        probabilities = [dist.pdf(value) for value in values]    
        prob=sum(probabilities)
        print("The area between range({},{}):{}".format(startrange,endrange,sum(probabilities)))
        return prob

    def stdNBgraph(dataset):
        # Coverted to standard Normal Distribution
        import seaborn as sns
        mean=dataset.mean()
        std=dataset.std()
    
        values=[i for i in dataset]
    
        z_score=[((j-mean)/std) for j in values]
    
        sns.distplot(z_score,kde=True)
    
        sum(z_score)/len(z_score)
        #z_score.std()

    def calc_vif(X):

        # Calculating VIF
        vif = pd.DataFrame()
        vif["variables"] = X.columns
        vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
        
        return(vif)