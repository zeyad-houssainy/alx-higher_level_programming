const headerElement = $("header")
const divElement = $("div")
divElement.on("click", function(){
    const currentClass = headerElement.attr("class")
    headerElement.toggleClass("red green")
})