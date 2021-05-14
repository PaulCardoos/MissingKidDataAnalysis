"""
code written by Denae Griffith
"""


library(readxl)
getwd()
setwd("C:\Users\griff\Desktop\MissingKidsintheUS.xls")

myData<- read_excel("C:\\users\\griff\\Desktop\\MissingKidsintheUS.xlsx")
myData
# as a data frame
df <- data.frame(myData)
colnames(df)[1]<- "state"
library(ggplot2)
library(usmap)
head(myData)
plot_usmap(data = df, values = "Missing.Kids")