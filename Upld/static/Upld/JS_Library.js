
var hideOrUnhide = function (elementName, type) {
  var Elem = document.getElementById(elementName);

  if (Elem.style.display == "none")
  {Elem.style.display = type;
  }
  else {Elem.style.display = "none";}

}
