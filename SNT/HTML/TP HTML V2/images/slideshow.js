/*
  Simple slide show manuel ou automatique,
  dans la fenetre courante ou en popup, selon vos besoins...
  Creation 18/06/2008 Amelie Vanbockstael
  Mise a jour 20/04/2010
  Testé avec Chrome4, Firefox3.5, IE6, IE7, Opera10.5
*/

//adresse des images
myPix = new Array("images/image1.jpg","images/image2.jpg","images/image3.jpg","images/image4.jpg")

//changement manuel
thisPic = 0
imgCt = myPix.length - 1
function chgSlide(direction) {
  if (document.images) {
     thisPic = thisPic + direction
     if (thisPic > imgCt) {
        thisPic = 0
     }
     if (thisPic < 0) {
        thisPic = imgCt
     }
     document.Puzzle.src = myPix[thisPic]
  }
}

//changement automatique
//vitesse de defilement en milliseconds
speed = 3000;
i = 0;
function autoSlideShow(imgname) {
  if (document.images)
  {
    document.getElementById(imgname).src = myPix[i];
    i++;
    if (i > myPix.length-1) i = 0;
    b=imgname;
    objet_timer = setTimeout('autoSlideShow(b)',speed);
  }
}

//arreter le defilement
function arret() {
	clearTimeout(objet_timer);
}


//prechargement des images de Dreamweaver
function preload() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
  var i,j=d.MM_p.length,a=preload.arguments; for(i=0; i<a.length; i++)
  if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

