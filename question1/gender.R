"""
written by suzy black 
question 1 
intermediate report
"""

getwd()
setwd("downloads")
data <- read.csv('../missingKids.csv')

## Read data in R 
missingKids <- read.csv("missingKids.csv")
missingKids = scan("missingKids.csv")
str(missingKids)

str(missingKids$sex)

table(missingKids$sex)

hist(missingKids$sex)
summary(missingKids$sex)
fivenum(missingKids$sex)
female <- 2947
male <- 2070
unknown <- 5

boxplot(female, male, unknown, names = c("Female", "Male", "Unknown"), main = "Missing Children by Sex", ylab = "Number of Missing Children")

pie(female, male, unknown, main = "Missing Children by Sex", ylab = "Number of Missing Children")


count <- c(female, male, unknown)
boxplot(count, main = "Missing Children by Sex", ylab = "Number of Missing Children")
pie (count, labels = paste0(count, "%"))

pie_labels <- paste0(count, " = ", round(100 * count/sum(count), 2), "%")
pie(count, labels = pie_labels, main = "Missing Children by Sex")

table(missingKids$race)

## Pie chart
count <- c(2947, 2070, 5)
sex <- c("Female","Male","Unknown")
pie_labels <- paste0(sex, " (",round(100 * count/sum(count), 2), "%)")
pie(count, labels = pie_labels, main = "Missing Children by Sex")


## Simulate data
n <- 20
mydata <- data.frame(
  sex = factor(sample(sex,n,replace=TRUE)),
  age = sample(5:25,n,replace=TRUE), 
  race = c("white","black","asian","other"))

## Two-way frequency table
freq <- table(missingKids[,c("sex","race")])
freq


