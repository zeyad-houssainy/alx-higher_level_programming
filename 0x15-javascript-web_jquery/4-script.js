const headerElement = $('header');
const divElement = $('div');
divElement.on('click', function () {
  headerElement.toggleClass('red green');
});
