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
        //Codigo del analisis a Computrabajo
        //Hay que poner una variable para el empleo a buscar, aqui por defecto le puse contador. 
        $html = file_get_html('https://www.computrabajo.com.ec/ofertas-de-trabajo/?q=contador'); 

        $container = $html->find('div[id=MainContainer]',0);
        $parrilla = $container->find('section[class=parrilla_oferta]',0);
        $ofertas = $parrilla->find('div[class=gO]',0);
        $oferta1div = $ofertas->find('div[class=bRS]');
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
            echo $seccion->outertext;

        }           



    ?>



    
</body>
</html>