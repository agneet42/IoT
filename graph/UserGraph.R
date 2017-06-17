library(igraph)

nodes <- read.csv("C:\\Users\\Agneet\\Downloads\\graph\\nodes.csv", header=T, as.is=T)
links <- read.csv("C:\\Users\\Agneet\\Downloads\\graph\\edges.csv", header=F, as.is=T)

net <- graph_from_data_frame( d= links, vertices = nodes, directed = F) 
plot(net, edge.arrow.size=.4,vertex.label = nodes$nodes42)

