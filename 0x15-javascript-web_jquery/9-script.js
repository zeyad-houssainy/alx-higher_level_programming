const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
$.getJSON(url, (content) => {
  $("DIV#hello").text(`${content["hello"]}`);
  //   $("DIV#hello").text(`${content.hello}`); you can use these two
});
