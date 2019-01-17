<?php
    declare(encoding='UTF-8');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    
    <?php
        ini_set('max_execution_time', 240);
        require 'simple_html_dom.php';
        $tag = "month";
	//Hola
        //$html = file_get_html('https://es.stackoverflow.com/?tags='.$tag); //lenguajes
        $html = file_get_html('https://es.stackoverflow.com/?tab='.$tag); //tabs

        $respuestas = $html->find('div[class=question-summary]');

        $nombre_archivo= $tag.'.csv';
        $archivo = fopen($nombre_archivo, "a");

        foreach($respuestas as $res) {
            $summary = $res->find('div[class=summary]',0);
            $titulo = $summary->find('h3',0);
            echo $titulo->plaintext; 

            $cp = $res->find('div[class=cp]',0);
            $votes = $cp->children(0)->children(0);
            $respuestas =  $cp->children(1)->children(0);
            $vistas =  $cp->children(2)->children(0);
            echo $votes->outertext;
            echo $respuestas->outertext;
            echo $vistas->outertext;
            
            
            $tituloutf = preg_replace_callback("/(&#[0-9]+;)/", function($m) { return mb_convert_encoding($m[1], "ISO-8859-1", "HTML-ENTITIES"); }, $titulo->plaintext);
            $titsincoma = str_replace(",",";",$tituloutf);
            $texto = $titsincoma . ','. $votes->plaintext.','.$respuestas->plaintext.','.$vistas->plaintext ."\r\n";

            fwrite($archivo,$texto);
         
        }

        fclose($archivo);


        /*
        $container = $html->find('div[id=MainContainer]',0);
        $parrilla = $container->find('section[class=parrilla_oferta]',0);
        $ofertas = $parrilla->find('div[class=gO]',0);
        $oferta1div = $ofertas->find('div[class=bRS]');
        
        $nombre_archivo='archivo.csv';
        $archivo = fopen($nombre_archivo, "a");

        foreach ($oferta1div as $oft) {
            $descripcion = $oft->find('div[class=iO]',0);
            $h2 = $descripcion->find('h2[class=tO]',0);
            $link = $h2->find('a[class=js-o-link]',0);
            //echo $link->href . "<br>";
            
            //Analisis de la descripcion de los trabajos
            $linkdes = 'https://www.computrabajo.com.ec'.$link->href;
            $htmldes = file_get_html($linkdes);
            $containerdes = $htmldes->find('div[id=MainContainer]',0);
            $articulo = $containerdes->find('article[class=fl]',0);
            $seccion = $articulo->find('section[class=box_r]',0);

            $ul = $seccion->find('ul li p');

            $trabajo = $ul[0];
            $empresa = $ul[1];
            $localizacion = $ul[2];
            $jornada = $ul[3];
            $tipo =  $ul[4];
            $salario = $ul[5];

            fwrite($archivo, $trabajo->plaintext .','.$empresa->plaintext.
            ','.$localizacion->plaintext .','. $jornada->plaintext.','.$tipo->plaintext.','.$salario->plaintext);

            echo $trabajo->outertext;
            echo $empresa->plaintext;
            echo $localizacion->outertext;
            echo $jornada->outertext;
            echo $tipo->outertext;
            echo $salario->outertext;*/

        //}           

       //fclose($archivo);

    ?>

</body>
</html>
