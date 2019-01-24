# Set Working Directory
#setwd("../../CltControl/Desktop/lenguajes/avance3Visualizacion-API_Google");
#setwd("../Desktop/Programming Languages/lenguajes/avance2Pre-Procesamiento")
setwd("../Desktop/Programming Languages/lenguajes/sustentacion")

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
ggplot(empresa, aes(x=nombre, y=n_ofertas)) + 
  geom_bar(stat = "identity", position = "stack") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  labs(title = "Numero de Ofertas por empresa")

# Grafico de pastel
porcentajes <- round(horario$n_ofertas/sum(horario$n_ofertas) * 100)
horario$empresa <- paste(horario$empresa, porcentajes) # add percents to labels 
horario$empresa <- paste(horario$empresa,"%",sep="") # ad % to labels 

pie(horario$n_ofertas, labels = horario$empresa, col=rainbow(length(horario$empresa)), main="Porcentajes de Ofertas por horarios")

dev.off()
