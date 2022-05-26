library(tidyverse)
library(bnlearn)

data <- read_csv("./data8.csv")
vars <- data %>%
    select(-city, -年份) %>%
    scale %>% as_tibble


# fit ---------------------------------------------------------------------

# Constraint-based
pc_res <- pc.stable(vars)
gs_res <- gs(vars)
hpc_res <- hpc(vars)
iamb_res <- iamb(vars)
mmpc_res <- mmpc(vars)

# Score-based
hc_res <- hc(vars)
tabu_res <- tabu(vars, optimized=T, score='bge')

# Hybrid
mmhc_res <- mmhc(vars)
h2pc_res <- h2pc(vars)

# result ------------------------------------------------------------------

res <- tabu_res
nodes <- c(res$nodes$score$nbr, "score")

# print(res$arcs)
# graphviz.plot(res)

adj <- matrix(0, length(nodes), length(nodes))
for (i in 1:length(nodes)){
    for (j in 1:length(nodes)){
        if (any( res$nodes[[nodes[i]]]$children == nodes[j] )){
            adj[i, j] = 1
        }
    }
}
colnames(adj) <- nodes
write.csv(adj, "dag.csv", row.names = FALSE)

write.csv(data[c("city", "年份", nodes)], "selected.csv", row.names = FALSE)
