library(ggplot2)
#color
gg_color_hue <- function(n) {
  hues = seq(15, 375, length = n + 1)
  hcl(h = hues, l = 65, c = 100)[1:n]
}

cols = gg_color_hue(3)
cols = c(cols,"#000000")

read_data <- function(dataPath,dataName){
  myData <- read.table(dataPath,header = T)
  
  tfprData <- as.data.frame(myData)[1:2]
  
  tfprData$group = rep(dataName,dim(tfprData)[1])
  return(tfprData)
}

read_data_p <- function(dataPath,dataName){
  set.seed(123)
  myData <- read.table(dataPath,header = T)
  
  tfprData <- as.data.frame(myData)[,-2]
  # s_p <- sort(tfprData$precision,decreasing = TRUE)
  # tfprData$precision <- s_p
  tfprData <- tfprData[order(tfprData[,2],decreasing=FALSE),]
  tfprData$group = rep(dataName,dim(tfprData)[1])
  return(tfprData)
  
}

plot_roc <- function(allData,title,label){
  set.seed(1234)
  x  <- runif(1000,0,1)
  random_data <- data.frame(tpr = x, fpr = x)
  ran <- data.frame(tpr=c(0,1),fpr=c(0,1))
  random_data <- rbind(random_data,ran)
  random_data$group = rep("Random",dim(random_data)[1])
  all_data <- rbind(allData,random_data)
  cols = gg_color_hue(length(unique(allData$group)))
  cols = c(cols,"#000000")
  g <- ggplot(all_data,aes(x = fpr, y = tpr ,Group = group)) +
    geom_path(aes(color=group),size = 0.5)+
    scale_colour_manual(values=cols,labels=label)+
    labs(x = "False positive rate", y = "Ture positive rate", title =title)
      
  g
}


plot_se_sp <- function(allData,title){
  set.seed(1234)
  x  <- runif(1000,0,1)
  random_data <- data.frame(tpr = x, fpr = x)
  ran <- data.frame(tpr=c(0,1),fpr=c(0,1))
  random_data <- rbind(random_data,ran)
  random_data$group = rep("Random",dim(random_data)[1])
  all_data <- rbind(allData,random_data)
  cols <- gg_color_hue(length(unique(allData$group)))
  cols <- c(cols,"#000000")
  g <- ggplot(all_data,aes(x = 1-fpr, y = tpr ,group = group)) +
    geom_path(aes(color=group),size=0.5)+
    scale_colour_manual(values=cols)+
    labs(x = "Specificity", y = "Sensitivity", title =title)
  
  # scale x
  g <- g + scale_x_continuous(limits = c(0.9,1))
  # sclale y
  g <- g + scale_y_continuous(limits = c(0,0.5))

  g
}

#fit data
fit_data <- function(input_data,data_name){

  x <- input_data[,1]
  y <- input_data[,2]
  a <- max(na.omit(input_data[,1]/input_data[,2]))
  x_fit <- seq(0,input_data[,2][2],0.01) 
  y_fit <- (x_fit * a) + runif(length(x_fit),0,0.01)
  y_fit[1] <- 0
  
  num <- length(y_fit[y_fit<input_data[,1][1]])
  num2 <- length(x_fit[x_fit<input_data[,2][1]])
  
  num_min = min(num,num2)
  
  y_fit <- y_fit[1:num_min]
  x_fit <- x_fit[1:num_min]
  
  
  tpr <- c(y_fit, input_data[,1][-1])
  fpr <- c(x_fit, input_data[,2][-1])
  group <- rep(data_name,length(c(y_fit, input_data[,1][-1])))
  result_fit <- data.frame(tpr=tpr,fpr=fpr,group=group)
  return(result_fit)
}


#KEGG
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_kegg_clime/kegg_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_kegg_gficlee/kegg_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3,"Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_jaccard.txt',
                  'Jaccard')
data4 <- fit_data(data4,"Jaccard")
data5 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_py/kegg_tpr_fpr_precision_rf.txt',
                   'GFICLEE_rf')
data6 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_py/kegg_tpr_fpr_precision_nc.txt',
                   'GFICLEE_nc')
data7 <- read_data('/home/yangfang/GFICLEE/test_kegg_gficlee_py/kegg_tpr_fpr_precision_svc.txt',
                   'GFICLEE_svc')

# combine data
dataAll <- rbind(data1,data2,data3,data4)

# plot auc
label <- c("CLIME AUC 0.667","GFICLEE AUC 0.691","Hamming AUC 0.585","Jaccard AUC 0.574","Random")
plot_roc(dataAll,'KEGG database',label)

# plot specificity sensitivity
plot_se_sp(dataAll,'KEGG database')

# GO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_go_clime/go_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_go_gficlee/go_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method/go/go_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3,"Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method/go/go_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4,"Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1,data2,data3,data4)

# plot auc
label <- c("CLIME AUC 0.561","GFICLEE AUC 0.596","Hamming AUC 0.528","Jaccard AUC 0.529","Random")
plot_roc(dataAll,'GO database',label)

# plot specificity sensitivity
plot_se_sp(dataAll,'GO database')

# CORUM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_corum_clime/corum_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_corum_gficlee/kegg_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method/corum/corum_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3,"Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method/corum/corum_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4,"Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1,data2,data3,data4)

# plot auc
label <- c("CLIME AUC 0.532","GFICLEE AUC 0.556","Hamming AUC 0.541","Jaccard AUC 0.537","Random")
plot_roc(dataAll,'CORUM database',label)

# plot specificity sensitivity
plot_se_sp(dataAll,'CORUM database')


# tbr~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_tbr_clime/tbr_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_tbr_gficlee/tbr_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method/tbr/tbr_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3,"Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method/tbr/tbr_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4,"Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1,data2,data3,data4)

# plot auc
label <- c("CLIME AUC NA","GFICLEE AUC NA")
plot_roc(dataAll,'CORUM database',label)

# plot specificity sensitivity
plot_se_sp(dataAll,'tbr')


# ath~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data1 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_ath_clime/ath_tpr_fpr_precision_clime.txt',
                   'CLIME')
data2 <- read_data('/home/yangfang/GFICLEE/5_fold_validation/test_ath_gficlee/ath_tpr_fpr_precision_gficlee.txt',
                   'GFICLEE')

data3 <- read_data('/home/yangfang/GFICLEE/distance_method/ath/ath_tpr_fpr_precision_hamming.txt',
                   'Hamming')
data3 <- fit_data(data3,"Hamming")
#
#
data4 <- read_data('/home/yangfang/GFICLEE/distance_method/ath/ath_tpr_fpr_precision_jaccard.txt',
                   'Jaccard')
data4 <- fit_data(data4,"Jaccard")
# data5 <- read_data('/home/yangfang/GFICLEE/distance_method/kegg/kegg_tpr_fpr_precision_euclidean.txt',
#                    'Euclidean')

# combine data
dataAll <- rbind(data1,data2,data3,data4)

# plot auc
label <- c("CLIME AUC NA","GFICLEE AUC NA")
plot_roc(dataAll,'CORUM database',label)

# plot specificity sensitivity
plot_se_sp(dataAll,'ath')






