// Fungsi untuk memuat file bahasa
function loadLanguageFile(language) {
	console.log(`Loading language file for ${language}`);
  return fetch(`/static/${language}.json`)
    .then(response => response.json())
    .then(data => data)
    .catch(error => console.error('Error loading language file:', error));
}

// Fungsi untuk mengganti bahasa
function changeLanguage(language) {
	console.log(`Changing language to ${language}`);
  loadLanguageFile(language)
    .then(data => {
      document.getElementById('helloText').innerText = data.hello;
      document.getElementById('welcomeText').innerText = data.welcome;
    });
}

document.getElementById('changeToEnglish').addEventListener('click', function() {
  changeLanguage('en');
});

document.getElementById('changeToBahasa').addEventListener('click', function() {
  changeLanguage('id');
});

document.addEventListener('DOMContentLoaded', function() {
  changeLanguage('en');
});