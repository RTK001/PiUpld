
var hideOrUnhide = function (elementName, type) {
  var Elem = document.getElementById(elementName);

  if (Elem.style.display == "none")
  {Elem.style.display = type;
  }
  else {Elem.style.display = "none";}
}


var getSelected = function(selectionName) {
  return PiUpld_selections[selectionName].Selected
}

var PiUpld_selections = {};

var setupSelection = function(selectionName, elementIdsArray) {

  PiUpld_selections[selectionName] = {};
  PiUpld_selections[selectionName].Elements = [];
  PiUpld_selections[selectionName].Selected = [];

  for (i = 0; i<elementIdsArray.length; i++)
  {
    elem = document.getElementById(elementIdsArray[i]);
    PiUpld_selections[selectionName].Elements[i] = elem;
    elem.onclick = function () {makeSelectedOnClick(this.id, selectionName)};
  }
}

var makeSelectedOnClick = function (selectedID, selectionName) {
  for (element in PiUpld_selections[selectionName].Elements)
  {
    elem = PiUpld_selections[selectionName].Elements[element];
    if (elem.id == selectedID)
    {
      if (elem.className == "Selected")
        {elem.className = "DeSelected";}
      else
        {elem.className = "Selected";}
      PiUpld_selections[selectionName].Selected = elem;

    }
    else {
      elem.className = "DeSelected";
    }
  }
}

var reloadiFrame = function (frameID) {
  document.getElementById(frameID).contentWindow.location.reload();
}
