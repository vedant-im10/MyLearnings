data("USArrests")

info <- "Dataset shows the statistics of Arrests of US states in 1973"

graphInfo <- "
Select the Graph to display information
1. BarPlot
2. Histogram
3. Piechart
4. LineGraphs
5. Scatterplots
6. Exit
"
cat(info)
cat(graphInfo)

repeat{
  cat(graphInfo)
  
  switch(
    var <- as.integer(readline(prompt = "Enter Choice: ")),
    barplot(USArrests$Murder),
    hist(USArrests$Assault),
    pie(USArrests$UrbanPop, radius = 1.2),
    plot(USArrests$Rape, type = "o"),
    plot(USArrests$UrbanPop),
    break
  )
}

