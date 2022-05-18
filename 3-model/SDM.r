library(tidyverse)
library(spatialreg)
library(spdep)

compute_w <- function(data){
    # add spatial information
    x_coords <- list(
        "东莞" = 113.760234,
        "广州" = 113.280637,
        "佛山" = 113.122717
    )
    y_coords <- list(
        "东莞" = 23.048884,
        "广州" = 23.125178,
        "佛山" = 23.028762
    )
    xy <- data %>%
        transmute(
            x = as.numeric(x_coords[city]),
            y = as.numeric(y_coords[city])
        )
    xy <- SpatialPoints(xy)
    # neighbor
    k <- nrow(data) %/% 3 - 1
    nb <- knn2nb(knearneigh(xy, k = k))
    nb2listw(nb)
}

data <- read_csv("./selected.csv") %>% filter(年份>=2017)
vars <- data %>% select(-city, -score, -年份) %>% scale
score <- data$score
listW <- compute_w(data)


# moran
moran.test(score, listW)
# moran.plot(score, listW)

# sdm
v <- colnames(vars)
model_summary <- lapply(
    1:length(v),
    function(i){
        # cat(i)
        errorsarlm(score ~ as.numeric(vars[,i]),
                   listw = listW,
                   Durbin = T) %>%
            summary
    }
)

result <-  tibble()
for (i in 1:length(v)){
    result <- result %>%
        rbind(tibble(
            variable = v[i],
            intercept = model_summary[[i]]$coefficients[1],
            coef = model_summary[[i]]$coefficients[2],
            lag.coef = model_summary[[i]]$coefficients[3],
            Wald.statistic = model_summary[[i]]$Wald1$statistic,
            Wald.p.value = model_summary[[i]]$Wald1$p.value,
            LR.statistic = model_summary[[i]]$LR1$statistic,
            LR.p.value = model_summary[[i]]$LR1$p.value
        ))
}

result

