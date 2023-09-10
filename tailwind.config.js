/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/templates/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
    "./src/**/forms.py",
  ],
  theme: {
    extend: {
      colors: {
        'interval-green-dark': "#2D3320",
        'interval-grenn-light': "#909E4F",

      }
    },
  },
  plugins: [
      require('flowbite/plugin')
  ]
};


/*
- Green: #6A8A6F
#35503D
*/
