
// When the user clicks on the button, scroll to the top of the document
function topFunctionOld() { 
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

function topFunction() {
  cframe = document.getElementById('content-frame');
  window.scrollTo(0, 0); 
  cframe.scrollTo(0, 0);
}