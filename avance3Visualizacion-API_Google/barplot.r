# Set Working Directory
#setwd("../../CltControl/Desktop/lenguajes/avance3Visualizacion-API_Google");
#setwd("../Desktop/Programming Languages/lenguajes/avance2Pre-Procesamiento")
setwd("../Desktop/Programming Languages/lenguajes/avance3Visualizacion-API_Google")


# Read from csv file
empresa <- read.csv2("ofertas_por_empresa.csv", sep = ",", header = FALSE)
horario <- read.csv2("ofertas_por_horario.csv", sep = ",", header = FALSE)

# Convert to a dataframe and add column names
colnames(empresa) <- c("nombre", "n_ofertas")
colnames(horario) <- c("empresa", "n_ofertas")

# Ordeno ascendentemente el dataset y le digo que prevalezca el orden al graficar
empresa <- empresa[order(empresa$n_ofertas, decreasing = TRUE),]
empresa$nombre <- factor(empresa$nombre, levels = empresa$nombre)

# Importo la liberia para graficar
library("ggplot2")

# Inicializo el dispositivo grafico para svg
svg(filename="Rplot%03d.svg", width=7, height=7, pointsize=12)
# Grafico el barplot
ggplot(empresa, aes(x=nombre, y=n_ofertas)) + geom_bar(stat = "identity", position = "stack") + theme(axis.text.x = element_text(angle = 90, hjust = 1))

# Grafico de pastel
pie(horario$n_ofertas, labels = horario$empresa, main="Pie Chart of Job Schedules")

dev.off()

ggplot(empresa, aes(x=nombre, y=n_ofertas, fill=nombre)) + 
  geom_bar(stat = "identity", position = "stack") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  theme(plot.title = element_text(size = rel(2)) )+
  labs(x = NULL, y = "Number of Available Jobs in units",
       fill = NULL)  
