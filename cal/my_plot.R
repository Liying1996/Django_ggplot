library(ggplot2)

args <- commandArgs(trailingOnly=TRUE)

draw <- function(file, name){
        data <- read.table(file, header = F)
        colnames(data) <- c('x', 'y')
        png(filename=paste('/Users/yingli/PycharmProjects/drawggplot/cal/static/', name, '.png', sep = ''))
#        plot(data)
		theme_set(theme_classic())
		print(ggplot(data, aes(x = x, y = y)) + geom_point(color = '#5A5AAD'))
        dev.off()
}
draw(args[1], args[2])
