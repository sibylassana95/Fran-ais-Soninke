/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Tous les fichiers HTML dans les templates de Django
    './static/js/**/*.js',    // Les fichiers JS dans ton dossier static
    './node_modules/flowbite/**/*.js', // Les fichiers JS de Flowbite
  ],
  darkMode: 'class', // Mode sombre activé par une classe
  theme: {
    extend: {
      colors: {
        primary: {
          "50": "#eff6ff",
          "100": "#dbeafe",
          "200": "#bfdbfe",
          "300": "#93c5fd",
          "400": "#60a5fa",
          "500": "#3b82f6",
          "600": "#2563eb",
          "700": "#1d4ed8",
          "800": "#1e40af",
          "900": "#1e3a8a"
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin'), // Plugin pour Flowbite
  ],
};
