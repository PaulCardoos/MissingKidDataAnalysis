"""
Written By Ashot Melkonyan
code to make pie chart and bar plot for question 5
"""

getwd()
missingKids = read.csv("missingKids.csv", header = TRUE)

x <- as.data.frame(table(missingKids$race))
y <- sort(table(missingKids$race), decreasing = TRUE)
barplot(y)

# Setting the data frame x for a pie chart

x<-x[-c(11, 9, 8, 6, 3, 2, 1), ] 
x$Var1 <- as.character(x$Var1)
x[nrow(x) + 1, ] = c("Other", 248)
x$Freq <- as.numeric(as.character(x$Freq))
x$Var1[is.na(x$Var1)] <- "Other"
x <- x[order(x$Freq),]

pie_labels <- paste0(x$Var1, " = ", round(100 * x$Freq/sum(x$Freq), 2), "%")

pie(x$Freq, labels = pie_labels)

#setting the data to compare to general population
comparision <- as.data.frame(table(missingKids$race))
comparision<- comparision[-c(11, 9, 6, 1), ] 
comparision <- comparision[order(-comparision$Freq),]

hisp_from_white.hisp <- 50/(36.42/24.13 + 1)
white_from_white.hisp <- 50 - hisp_from_white.hisp

comparision[1, 2] <- comparision[1, 2] + round(white_from_white.hisp)
comparision[3, 2] <- comparision[3, 2] + round(hisp_from_white.hisp)

comparision # counts of missing kids by race (1=White, 2=Black, 3=Hispanic, 4=Biracial, 5=Asian, 6=Am. Ind, 7=Pacific Isl.)
# Setting the null hypothesis
p = c(.501,.251,.141,.041,.051, 0.011, 0.004) # corresponding proportions of kids by race in the general population 

# Hypothesis test and results
test = chisq.test(comparision$Freq, p=p)
test

test$observed

round(test$expected)

round(test$residuals,2)





