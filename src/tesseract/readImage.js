const Tesseract =  require('tesseract.js');

Tesseract.recognize(
  'testImage.jpg',
  'eng',
  { logger: m => console.log(m) }
).then(({ data: { text } }) => {
  console.log(text);
})