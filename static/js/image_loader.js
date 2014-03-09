

if (typeof window.FileReader === 'undefined') {
  state.className = 'File API & FileReader unavailable';
} else {
  state.className = 'success';
  state.innerHTML = stateStr;
}
var main = document.getElementById('main');
var dropbox1 = document.getElementById('dropbox1');
var dropbox2 = document.getElementById('dropbox2');
var stateStr = 'Drag image file here asdaf';
var dropStr = 'Drop image file! asd fadf ';

dropbox1.ondragover = function () { this.className = 'hover'; state.innerHTML = dropStr; return false; };
dropbox1.ondragend = function () { this.className = 'nohover'; state.innerHTML = stateStr; return false; };
dropbox1.ondragleave = function (){ this.className = 'nohover'; state.innerHTML = stateStr; return false; };
dropbox2.ondragover = function () { this.className = 'hover'; state.innerHTML = dropStr; return false; };
dropbox2.ondragend = function () { this.className = 'nohover'; state.innerHTML = stateStr; return false; };
dropbox2.ondragleave = function (){ this.className = 'nohover'; state.innerHTML = stateStr; return false; };



main.ondrop = function (e) {
  this.className = 'drop';
  state.innerHTML = stateStr;
  e.preventDefault();

  /*var file = e.dataTransfer.files[0],
      reader = new FileReader();
  reader.onload = function (event) {
    console.log(event.target);
    dropbox.style.background = 'url(' + event.target.result + ') no-repeat center';
  */
  };
}