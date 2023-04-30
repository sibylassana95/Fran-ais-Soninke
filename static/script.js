

//dark mode
tailwind.config = {
darkMode: 'class',
theme: {
extend: {
colors: {
  primary: {"50":"#eff6ff","100":"#dbeafe","200":"#bfdbfe","300":"#93c5fd","400":"#60a5fa","500":"#3b82f6","600":"#2563eb","700":"#1d4ed8","800":"#1e40af","900":"#1e3a8a"}
}
},
fontFamily: {
'body': [
'Inter', 
'ui-sans-serif', 
'system-ui', 
'-apple-system', 
'system-ui', 
'Segoe UI', 
'Roboto', 
'Helvetica Neue', 
'Arial', 
'Noto Sans', 
'sans-serif', 
'Apple Color Emoji', 
'Segoe UI Emoji', 
'Segoe UI Symbol', 
'Noto Color Emoji'
],
'sans': [
'Inter', 
'ui-sans-serif', 
'system-ui', 
'-apple-system', 
'system-ui', 
'Segoe UI', 
'Roboto', 
'Helvetica Neue', 
'Arial', 
'Noto Sans', 
'sans-serif', 
'Apple Color Emoji', 
'Segoe UI Emoji', 
'Segoe UI Symbol', 
'Noto Color Emoji'
]
}
}
}
// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
document.documentElement.classList.add('dark');
} else {
document.documentElement.classList.remove('dark')
}
var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
themeToggleLightIcon.classList.remove('hidden');
} else {
themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

// toggle icons inside button
themeToggleDarkIcon.classList.toggle('hidden');
themeToggleLightIcon.classList.toggle('hidden');

// if set via local storage previously
if (localStorage.getItem('color-theme')) {
if (localStorage.getItem('color-theme') === 'light') {
    document.documentElement.classList.add('dark');
    localStorage.setItem('color-theme', 'dark');
} else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('color-theme', 'light');
}

// if NOT set via local storage previously
} else {
if (document.documentElement.classList.contains('dark')) {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('color-theme', 'light');
} else {
    document.documentElement.classList.add('dark');
    localStorage.setItem('color-theme', 'dark');
}
}

});


