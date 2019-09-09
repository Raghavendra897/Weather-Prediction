# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:13:09 2019

@author: Raghavendra J P
"""
import csv,requests,os
from bs4 import BeautifulSoup


if 'datasets' not in os.listdir(os.getcwd()):
    os.mkdir('datasets')

url='https://karki23.github.io/Weather-Data/assignment.html'
html=requests.get(url).text
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())
links=soup.find_all('a')
#print(soup)
suffix=[]
for link in links:
    suffix.append(link.get('href'))
#print(suffix)
for suf in suffix:
    lurl='https://karki23.github.io/Weather-Data/' + suf
    #print(url)
    fn=str(os.getcwd())+'\\'+'datasets'+'\\'+suf.replace('.html','')+'.csv'
    lhtml=requests.get(lurl).text
    lsoup=BeautifulSoup(lhtml,'lxml')
    i=0
    d=[]
    for mytable in lsoup.find_all('table'):
        for trs in mytable.find_all('tr'):
            ths=trs.find_all('th')
            tds = trs.find_all('td')
            l=[]
            if i==0:
                for elem in ths:
                    l.append(elem.text.strip())
            i=i+1
            for elem in tds:
                l.append(elem.text.strip())
            d.append(l)

        
        with open(fn, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(d)
        csvFile.close()

#convert the downloaded data to only numbers data
#N=1
#s=2
#E=3
#W=4
#NE=5
#NW=6
#SE=7
#SW=8

#remove first row and first two columns

if 'traindata' not in os.listdir(os.getcwd()):
    os.mkdir('traindata')
input_folder='datasets'
for filename in os.listdir(str(os.getcwd())+'\\'+input_folder):
    input_filename=(str(os.getcwd())+'\\'+input_folder+'\\'+str(filename))
    begin = 2
    end = 24
    output_filename=str(os.getcwd())+'\\'+'traindata'+'\\'+'m'+filename
    l=[]
    with open(input_filename, "r") as file_in:
        with open(output_filename, "w",newline='') as file_out:
            writer = csv.writer(file_out)
            for row in csv.reader(file_in):
                l.append(row[begin:end])
            del l[0]
            train=[]
            for j in l:
                a=[float(i.replace('nan','0').replace('Yes','1').replace('No','0').replace('NE','5').replace('NW','6').replace('SE','7').replace('SW','8').replace('N','1').replace('S','2').replace('E','3').replace('W','4').replace('[','').replace(']','')) for i in j]
                train.append(a)
            for i in train:
                writer.writerow(i)
            file_out.close()
    file_in.close()
#save all the data of all cities into onefile
data=[]
with open ('finaltrain.csv',"w",newline='') as file_out:
    writer = csv.writer(file_out)
    for filename in os.listdir(os.getcwd()+'\\'+'traindata'):
        input_filename=(str(os.getcwd())+'\\'+'traindata'+'\\'+str(filename))
        l=[]
        with open(input_filename, "r") as file_in:
            for row in csv.reader(file_in):
                    l.append(row)
        for j in l:
            a=[float(i) for i in j]
            data.append(a)           
    for i in train:
        writer.writerow(i)           
    
    
