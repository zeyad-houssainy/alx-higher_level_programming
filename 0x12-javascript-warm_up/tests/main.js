// const myHeading = document.querySelector("h1");
// myHeading.textContent = "Hello World !!";
// console.log("hi i'm the best in Javascript") //this will appear in console only
// console.log("My name is zeyad haha")

//test #1
// const newButton = document.createElement("button")
// newButton.classList.add("buttonClass")
// newButton.textContent("click me")
// newButton.setAttribute("ID, buttonID")
// newButton.innerHTML = "Click me"
// const main = document.querySelector("body")
// main.append(newButton)


// test #2
// const main2 = document.querySelector("body")
// const paragraphText = `Hey i'm Zeyad`
// const newParagraph = document.createElement("p")
// newParagraph.textContent = paragraphText
// main2.prepend(newParagraph)


// test #3
var divElement = document.querySelector("div")
var paragraph = document.createElement("p")
paragraph.textContent = "Hey hey i'm zeyad"
divElement.append(paragraph)

// adding paragraph insde the <body> hktbha awel 7aga 
var bodyElement = document.querySelector("body")
var newButton = document.createElement("button")
bodyElement.prepend(newButton)
newButton.innerText = "Change color for the square below"
newButton.classList.add("changeColorButton")

// add a square and change its color
var squareSection = document.createElement("section")
squareSection.style.cssText = 
    "width: 50%; height: 50px; border: solid black; background-color: yellow";
bodyElement.prepend(squareSection)

const randomNumber = (number) => {
    return Math.floor(Math.random() * (number + 1));
}
const randomColor = () => {
    document.squareSection.style.backgroundColor = `background-color: rgb(${}, ${}, ${})`
}

const buttonTrigger = document.querySelector(".changeColorButton")
buttonTrigger.addEventListener(click, randomColor)



