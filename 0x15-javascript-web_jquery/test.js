// change header background color to gray
document.querySelector("header").style.backgroundColor = "gray";

// change footer background color to black and font to white
var footer = document.querySelector("footer");
footer.style.backgroundColor = "black";
footer.style.color = "white";
$("footer").css({"background-color": "black", "color": "white"})

// add a new paragraph to the div
document.addEventListener("DOMContentLoaded", function() {
    var divElement = document.querySelector("div");
    var newParagraph = document.createElement("p");
    newParagraph.textContent = "This is a new paragraph";
    divElement.appendChild(newParagraph);
    $("div").css("background-color", "red");
    $("div").css("border", "solid black");
    $("div").hide(300).show(200)
}); // use this to make sure the DOM is fully loaded before you start working with it

