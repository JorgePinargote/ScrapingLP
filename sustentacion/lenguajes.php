<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>    
	<label>Scraping OK!</label>
    <?php
        ini_set('max_execution_time', 240);
        require 'simple_html_dom.php';
        //Codigo del analisis a Computrabajo
        //Hay que poner una variable para el empleo a buscar, aqui por defecto le puse contador. 
        
        $html = file_get_html('https://www.computrabajo.com.ec/ofertas-de-trabajo/?q=arquitecto'); 
        $oferta1div = $html->find('div[class=bRS]');
        
        $nombre_archivo='computrabajo.csv';
        $archivo = fopen($nombre_archivo, "a");

        foreach ($oferta1div as $oft) {
            $descripcion = $oft->find('div[class=iO]',0);
            $h2 = $descripcion->find('h2[class=tO]',0);
            $link = $h2->find('a[class=js-o-link]',0);
            
            //Analisis de la descripcion de los trabajos
            $linkdes = 'https://www.computrabajo.com.ec'.$link->href;
            $htmldes = file_get_html($linkdes);
            $seccion = $htmldes->find('section[class=box_r]',0);

            $ul = $seccion->find('ul li p');

            $trabajo = $ul[0];
            $empresa = $ul[1];
            $localizacion = $ul[2];
            $jornada = $ul[3];
            $tipo =  $ul[4];
            $salario = $ul[5];

            $trpro = str_replace(",",";",trim($trabajo->plaintext)); //cadena de trabajo, procesado. 
            $empro =  str_replace(",",";",trim($empresa->plaintext));
            $locpro = str_replace(",",";",trim($localizacion->plaintext));
            $jorpro = str_replace(",",";",trim($jornada->plaintext));
            $tipro = str_replace(",",";",trim($tipo->plaintext)); 
            $salpro = str_replace(",",";",trim($salario->plaintext));
            
            if(count($ul) == 6){
                fwrite($archivo,  $trpro.','.$empro.
                ','.$locpro.','.$jorpro .','. $tipro .','.$salpro."\r\n");
            }

        }
        
        fclose($archivo);
        
        //Codigo del analisis a Multitrabajo
        $htmlmul = file_get_html('https://www.multitrabajos.com/empleos-busqueda-programador.html'); 
        $ofertasmul = $htmlmul->find('div[class=aviso]');

        $nombre_archivo1='multitrabajo.csv';
        $archivo1 = fopen($nombre_archivo1, "a");

        foreach ($ofertasmul as $ofm) {
           $descmul = file_get_html('https://www.multitrabajos.com'.$ofm->id); 
           $header = $descmul->find('div[class=aviso_header]',0);
           $title = $header->find('h1[class=aviso_title]',0);
           $enterprise = $header->find('a h2',0);
           $specs = $descmul->find('div[class=aviso_specs]',0);
           $data = $specs->find('div[class=z-group]');

           $lugar = $data[0]->children(1);
           $tipo = $data[3]->children(1);
           $paga =  $data[2]->children(1);


           $titlepro = str_replace(",",";",trim($title->plaintext)); //cadena de trabajo, procesado. 

           $emp = $enterprise->plaintext;
           if($enterprise==NULL) $emp = "Confidencial";

           $entpro =  str_replace(",",";",trim($emp));
           $lugarpro = str_replace(",",";",trim($lugar->plaintext));
           $tipopro = str_replace(",",";",trim($tipo->plaintext));
           $salariopro = str_replace(",",";",trim($paga->plaintext)); 

           fwrite($archivo1,  $titlepro.','.$entpro.','.$lugarpro .','. $tipopro .','.$salariopro."\r\n");
           
        }

        fclose($archivo1);

    ?>

  <script>
      $(document).ready(function(){
          alert("Scraping OK!");
      });
    </script>

    
</body>
</html>