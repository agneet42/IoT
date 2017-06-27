library(igraph)
library(dnet)
library(MASS)

nodes <- read.csv("C:\\Users\\Agneet\\Downloads\\spatio-temporal\\Nodes.csv", header=T, as.is=T)
links <- read.csv("C:\\Users\\Agneet\\Downloads\\spatio-temporal\\Edges.csv", header=F, as.is=T)

net <- graph_from_data_frame( d= links, vertices = nodes, directed = F) 
matr <- dRWR(g = net,normalise = "laplacian" ,restart=0.3)
# print(matr)
write.matrix(matr, file = "result.txt")

# visHeatmapAdv(matr, Rowv=FALSE, Colv=FALSE, colormap="wyr",KeyValueName="Affinity")











# plot(net, edge.arrow.size=.4,vertex.label = nodes$nodes1)