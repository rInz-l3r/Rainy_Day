const Tesseract =  require('tesseract.js');

Tesseract.recognize(
  'image.jpg',
  'eng',
  { logger: m => console.log(m) }
).then(({ data: { text } }) => {
  console.log(text);
})