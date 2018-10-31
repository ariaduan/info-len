import scipy
from scipy.stats import f
import numpy as np
import scipy.stats as stats
# additional packages
from statsmodels.stats.diagnostic import lillifors

#https://www.cnblogs.com/webRobot/p/6760839.html
'''
group1=[2,3,7,2,6]
group2=[10,8,7,5,10]
group3=[10,13,14,13,15]
list_groups=[group1,group2,group3]
list_total=group1+group2+group3
#对所有样本组进行正态性检验
def NormalTest(list_groups):
    for group in list_groups:
        #正态性检验
        status=check_normality(group1)
        if status==False :
            return False
             
     
#对所有样本组进行正态性检验   
NormalTest(list_groups)
'''
#正态分布测试
def check_normality(testData):

	#样本数大于3小于20用Shapiro-Wilk算法检验正态分布性   
    if 3 <= len(testData) <= 20:
    	#print('shapiro')
    	d, p_value= stats.shapiro(testData)
    	if p_value<0.05:
    		#print "use lillifors:"
    		#print "data are not normal distributed"
    		return  (d, p_value, 0, 'shapiro')
    	else:
    		#print "use lillifors:"
    		#print "data are normal distributed"
    		return (d, p_value, 1, 'shapiro')

	#样本数大于20小于50用normaltest算法检验正态分布性   
    if 20 < len(testData) < 50:
    	#print('normaltest')
    	d, p_value= stats.normaltest(testData)
    	if p_value<0.05:
    		#print "use lillifors:"
    		#print "data are not normal distributed"
    		return  (d, p_value, 0, 'normaltest')
    	else:
    		#print "use lillifors:"
    		#print "data are normal distributed"
    		return (d, p_value, 1, 'normaltest')

    #样本数大于50小于300用lillifors算法检验正态分布性   
    if 300 >= len(testData) >=50:
    	#print('lillifors')
    	d, p_value= lillifors(testData)
    	if p_value<0.05:
    		#print "use lillifors:"
    		#print "data are not normal distributed"
    		return  (d, p_value, 0, 'lillifors')
    	else:
    		#print "use lillifors:"
    		#print "data are normal distributed"
    		return (d, p_value, 1, 'lillifors')
    
    #样本数大于300用kstest算法检验正态分布性 
    if len(testData) > 300: 
    	#print('kstest')
    	d, p_value= stats.kstest(testData,'norm')
    	if p_value<0.05:
    		#print "use kstest:"
    		#print "data are not normal distributed"
    		return  (d, p_value, 0, 'kstest')
    	else:
    		#print "use kstest:"
    		#print "data are normal distributed"
    		return (d, p_value, 1, 'kstest')
