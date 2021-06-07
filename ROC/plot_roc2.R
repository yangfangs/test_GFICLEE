library(ggplot2)
theme_set(theme_bw())
#color
gg_color_hue <- function(n) {
  hues = seq(15, 375, length = n + 1)
  hcl(h = hues, l = 65, c = 100)[1:n]
}

cols = gg_color_hue(3)
cols = c(cols, "#000000")

read_data <- function(dataPath, dataName) {
  myData <- read.table(dataPath, header = T)

  tfprData <- as.data.frame(myData)[1:2]

  tfprData$group = rep(dataName, dim(tfprData)[1])
  return(tfprData)
}

read_data_p <- function(dataPath, dataName) {
  set.seed(123)
  myData <- read.table(dataPath, header = T)

  tfprData <- as.data.frame(myData)[, -2]
  # s_p <- sort(tfprData$precision,decreasing = TRUE)
  # tfprData$precision <- s_p
  tfprData <- tfprData[order(tfprData[, 2], decreasing = FALSE),]
  tfprData$group = rep(dataName, dim(tfprData)[1])
  return(tfprData)

}

plot_roc <- function(allData, title, label) {
  set.seed(1234)
  x <- runif(1000, 0, 1)
  random_data <- data.frame(tpr = x, fpr = x)
  ran <- data.frame(tpr = c(0, 1), fpr = c(0, 1))
  random_data <- rbind(random_data, ran)
  random_data$group = rep("Random", dim(random_data)[1])
  all_data <- rbind(allData, random_data)
  cols = gg_color_hue(length(unique(allData$group)))
  cols = c(cols, "#000000")
  g <- ggplot(all_data, aes(x = fpr, y = tpr, Group = group)) +
    geom_path(aes(color = group), size = 0.5) +
    scale_colour_manual(values = cols, labels = label) +
    labs(x = "False positive rate", y = "Ture positive rate", title = title)

  g
}


plot_se_sp <- function(allData, title) {
  set.seed(1234)
  x <- runif(1000, 0, 1)
  random_data <- data.frame(tpr = x, fpr = x)
  ran <- data.frame(tpr = c(0, 1), fpr = c(0, 1))
  random_data <- rbind(random_data, ran)
  random_data$group = rep("Random", dim(random_data)[1])
  all_data <- rbind(allData, random_data)
  cols <- gg_color_hue(length(unique(allData$group)))
  cols <- c(cols, "#000000")
  g <- ggplot(all_data, aes(x = 1 - fpr, y = tpr, group = group)) +
    geom_path(aes(color = group), size = 1.0) +
    scale_colour_manual(values = cols) +
    labs(x = "Specificity", y = "Sensitivity", title = title)

  # scale x
  g <- g + scale_x_continuous(limits = c(0.965, 1))
  # sclale y
  g <- g + scale_y_continuous(limits = c(0, 0.5))

  g
}

#fit data
fit_data <- function(input_data, data_name) {

  x <- input_data[, 1]
  y <- input_data[, 2]
  a <- max(na.omit(input_data[, 1] / input_data[, 2]))
  x_fit <- seq(0, input_data[, 2][2], 0.01)
  y_fit <- (x_fit * a) + runif(length(x_fit), 0, 0.01)
  y_fit[1] <- 0

  num <- length(y_fit[y_fit < input_data[, 1][1]])
  num2 <- length(x_fit[x_fit < input_data[, 2][1]])

  num_min = min(num, num2)

  y_fit <- y_fit[1:num_min]
  x_fit <- x_fit[1:num_min]


  tpr <- c(y_fit, input_data[, 1][-1])
  fpr <- c(x_fit, input_data[, 2][-1])
  group <- rep(data_name, length(c(y_fit, input_data[, 1][-1])))
  result_fit <- data.frame(tpr = tpr, fpr = fpr, group = group)
  return(result_fit)
}


#KEGG
data1 <- read_data('/home/yangfang/GFICLEE/test_kegg_clime_5_fold_backup/kegg_tpr_fpr_precision_clime.txt',
                   'CLIME')

data2 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_5_fold_backup/kegg_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')
data_MEGA_NJ <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_MEGA_NJ/kegg_tpr_fpr_precision_gficlee.txt",
                          "MEGA_NJ")
data_MEGA_ML <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_MEGA_ML/kegg_tpr_fpr_precision_gficlee.txt",
                          "MEGA_ML")
data_MEGA_MP <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_MEGA_MP/kegg_tpr_fpr_precision_gficlee.txt",
                          "MEGA_MP")
data_iqtree <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_iqtree/kegg_tpr_fpr_precision_gficlee.txt",
                          "IQ-TREE")
data_fasttree <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_fasttree/kegg_tpr_fpr_precision_gficlee.txt",
                          "FastTree")
data_random <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_random/kegg_tpr_fpr_precision_gficlee.txt",
                           "RandomTree")
data_random <- fit_data(data_random, "RandomTree")
animals30 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_animals30/kegg_tpr_fpr_precision_gficlee.txt",
                         "Subtree (80%)")
animals22 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_animals22/kegg_tpr_fpr_precision_gficlee.txt",
                       "Subtree (60%)")
animals15 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_animals15/kegg_tpr_fpr_precision_gficlee.txt",
                       "Subtree (40%)")
animals7 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_animals7/kegg_tpr_fpr_precision_gficlee.txt",
                       "Subtree (20%)")
animals38 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_animals38/kegg_tpr_fpr_precision_gficlee.txt",
                      "Subtree (38 Animals)")
plants16 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_plants16/kegg_tpr_fpr_precision_gficlee.txt",
                       "Subtree (16 Plants)")
fungi56 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_fungi56/kegg_tpr_fpr_precision_gficlee.txt",
                      "Subtree (56 Fungi)")
protists29 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_protists29/kegg_tpr_fpr_precision_gficlee.txt",
                     "Subtree (29 Protists)")
matrixe2 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_matrixe2/kegg_tpr_fpr_precision_gficlee.txt",
                     "Matrix_e2")
matrixe4 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_matrixe4/kegg_tpr_fpr_precision_gficlee.txt",
                        "Matrix_e4")
matrixe5 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_matrixe5/kegg_tpr_fpr_precision_gficlee.txt",
                      "Matrix_e5")
protists29 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_protists29/kegg_tpr_fpr_precision_gficlee.txt",
                        "Subtree (29 Protists)")
protists29 <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_protists29/kegg_tpr_fpr_precision_gficlee.txt",
                        "Subtree (29 Protists)")

S0.01_0.001G <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_0.01s_0.001g/kegg_tpr_fpr_precision_gficlee.txt",
                        "0.01S_0.001G")
S0.01_0.003G <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_0.01s_0.003g/kegg_tpr_fpr_precision_gficlee.txt",
                        "0.01S_0.003G")
S0.01_0.005G <- read_data("/home/yangfang/GFICLEE/test_kegg_gficlee_0.01s_0.005g/kegg_tpr_fpr_precision_gficlee.txt",
                        "0.01S_0.005G")
data3 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/kegg/kegg_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3, "Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/kegg/kegg_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4, "Jaccard")
data5 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_py/kegg_tpr_fpr_precision_rf.txt',
                   'GFICLEE_rf')
data6 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_py/kegg_tpr_fpr_precision_nc.txt',
                   'GFICLEE_nc')
data7 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_py/kegg_tpr_fpr_precision_svc.txt',
                   'GFICLEE_svc')

# combine data
# dataAll <- rbind(data2, data_MEGA_NJ, data_MEGA_ML,data_fasttree,data_iqtree,data_random)
# dataAll <- rbind(data2, animals30,animals22,animals15,animals7,animals38,plants16,fungi56,protists29)
# dataAll <- rbind(data2,animals38,plants16,fungi56,protists29)
# dataAll <- rbind(data2,matrixe2,matrixe4,matrixe5)
dataAll <- rbind(data2,S0.01_0.001G,S0.01_0.003G,S0.01_0.005G)

# plot auc
# label <- c("CLIME AUC 0.662", "GFICLEE AUC 0.713", "Hamming AUC 0.559", "Jaccard AUC 0.562", "Random")
# label <- c("CLIME", "MEGA_NJ", "MEGA_ML", "IQ-TREE","FastTree" ,"Random")
# label <- c("CLIME", "IQ-TREE","FastTree" ,"Random")
# plot_roc(dataAll, 'KEGG database', label)


# plot specificity sensitivity
plot_se_sp(dataAll, 'KEGG database')

setwd("/home/yangfang/GFICLEE/Revision/PhyPro/")

pdf(paste0("different_differente_each", "_AUC.pdf"), height = 8.08, width = 10.43)
print(plot_se_sp(dataAll, 'KEGG database'))
dev.off()
# GO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_go_clime/go_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_go_gficlee/go_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/go/go_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3, "Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/go/go_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4, "Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1, data2, data3, data4)

# plot auc
label <- c("CLIME AUC 0.564", "GFICLEE AUC 0.594", "Hamming AUC 0.561", "Jaccard AUC 0.570", "Random")
plot_roc(dataAll, 'GO database', label)

# plot specificity sensitivity
plot_se_sp(dataAll, 'GO database')

# CORUM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_corum_clime/corum_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_corum_gficlee/kegg_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method_2_fold/corum_backup/corum_tpr_fpr_precision_hamming.txt',
                   'Hamming')
# data3 <- fit_data(data3,"Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method_2_fold/corum_backup/corum_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4, "Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1, data2, data3, data4)

# plot auc
label <- c("CLIME AUC 0.531", "GFICLEE AUC 0.550", "Hamming AUC 0.584", "Jaccard AUC 0.584", "Random")
plot_roc(dataAll, 'CORUM database', label)

# plot specificity sensitivity
plot_se_sp(dataAll, 'CORUM database')


# tbr~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_tbr_clime/tbr_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_tbr_gficlee/tbr_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/tbr/tbr_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3, "Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/tbr/tbr_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4, "Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1, data2, data3, data4)

# plot auc
label <- c("CLIME AUC 0.615", "GFICLEE AUC 0.641", "Hamming AUC 0.568", "Jaccard AUC 0.563", "Random")
plot_roc(dataAll, 'tbr kegg database', label)

# plot specificity sensitivity
plot_se_sp(dataAll, 'tbr')


# ath~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_ath_clime/ath_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_ath_gficlee/ath_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/ath/ath_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3, "Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method_5_fold/ath/ath_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4, "Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1, data2, data3, data4)

# plot auc
label <- c("CLIME AUC 0.770", "GFICLEE AUC 0.794", "Hamming AUC 0.676", "Jaccard AUC 0.667", "Random")
plot_roc(dataAll, 'ath kegg database', label)

# plot specificity sensitivity
plot_se_sp(dataAll, 'ath')






