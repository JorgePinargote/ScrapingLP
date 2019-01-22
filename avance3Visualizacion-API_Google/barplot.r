# Set Working Directory
setwd("../../CltControl/Desktop/lenguajes/avance3Visualizacion-API_Google");

# Read from csv file
ofertas <- read.csv2("pre-processing.csv", sep = ",", header = FALSE)

# Convert to a dataframe and add column names
ofertas <- data.frame(ofertas)
colnames(ofertas) <- c("Provincia", "n_ofertas")

# Ordeno ascendentemente el dataset y le digo que prevalezca el orden al graficar
ofertas <- ofertas[order(ofertas$n_ofertas, decreasing = TRUE),]
ofertas$Provincia <- factor(ofertas$Provincia, levels = ofertas$Provincia)

# Grafico el barplot
ggplot(ofertas, aes(x=Provincia, y=n_ofertas)) + geom_bar(stat = "identity")

# Grafico de pastel
pie(ofertas$n_ofertas, labels = ofertas$Provincia, main="Pie Chart of Jobs")
