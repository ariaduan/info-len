import scipy
from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt
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
    if 300>=len(testData) >=50:
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
    if len(testData) >300: 
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

lst = ['2','3','4']

for num in lst:
    file1 = open('../corpora_and_texts_obtained/' + num + 'gm_for_gaussian_test','rb')
    file2 = open('../corpora_and_texts_obtained/' + num + 'gm_POS_for_gaussian_test','rb')
    fileout1 = open('../corpora_and_texts_obtained/' + num + 'gm_gaussian.csv','w',encoding = 'utf-8')
    fileout2 = open('../corpora_and_texts_obtained/' + num + 'gm_POS_gaussian.csv','w',encoding = 'utf-8')
    
    fileout1.write('word,d,p,h,func\n')
    fileout2.write('word,POS,d,p,h,func\n')
    for line in file1:
        line = line.decode('utf-8').split()
        x = line[1:]
        x = list(map(float, x))
        if len(x) < 3:
            continue
        d, p, h, func = check_normality(x)
        fileout1.write(line[0] + ',' + str(d) + ',' + str(p) + ',' + str(h) + ',' + func + '\n')
    for line in file2:
        line = line.decode('utf-8').split()
        x = line[2:]
        x = list(map(float, x))
        if len(x) < 3:
            continue
        d, p, h, func = check_normality(x)
        fileout2.write(line[0] + ',' + line[1] + ',' + str(d) + ',' + str(p) + ',' + str(h) + ',' + func + '\n')
    
    file1.close()
    file2.close()
    fileout1.close()
    fileout2.close()