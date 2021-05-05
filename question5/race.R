"""
Written By Ashot Melkonyan
code to make pie chart and bar plot for question 5
"""
getwd()
missingKids = read.csv("missingKids.csv", header = TRUE)

x <- as.data.frame(table(missingKids$race))
y <- sort(table(missingKids$race), decreasing = TRUE)
barplot(y)


x<-x[-c(11, 9, 8, 6, 3, 2, 1), ] 

x[nrow(x) + 1, ] = c("Other", 248)
x$Var1 <- as.character(x$Var1)
x$Freq <- as.numeric(as.character(x$Freq))
x$Var1[is.na(x$Var1)] <- "Other"
x <- x[order(x$Freq),]

pie_labels <- paste0(x$Var1, " = ", round(100 * x$Freq/sum(x$Freq), 2), "%")

pie(x$Freq, labels = pie_labels)





