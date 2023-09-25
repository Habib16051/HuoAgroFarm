// /** @type {import('tailwindcss').Config} */

// module.exports = {
//   content: ["./**/*.{html,js}"],
//   theme: {
//     extend: {
//       spacing: {
//         "some key": { 1.5: "" },

//         colors: {
//           "color-primary": "#01051e",
//           "color-primary-light": "#020726",
//           "color-primary-dark": "#010417",
//           "color-secondary": "#ff7d3b",
//           "color-gray": "#333",
//           "color-white": "#fff",
//           "color-blob": "#A427DF",
//         },
//       },
//     },
//   },
//   plugins: [],

//   container: {
//     center: true,
//     padding: {
//       DEFAULT: "20px",
//       md: "50px",
//     },
//   },
// };


/** @type {import('tailwindcss').Config} */

const plugin = require('tailwindcss/plugin');

const rotateY = plugin(function ({ addUtilities }) {
  addUtilities ({
    '.rotate-y-180': {
      transform: "rotateY(180deg)"
    },
    '.-rotate-y-180': {
      transform: "rotateY(-180deg)"
    }
  })
})

module.exports = {
  content: ["./**/*.{html,js}", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      spacing:{
        "some key": {1.5: ""}
      },
      colors: {
        "color-primary": "#0D4D15",
        "color-primary-light": "#1E3923",
        "color-primary-dark": "#04300C",
        "color-secondary": "#2A6605",
        "color-gray": "#314425",
        "color-white": "#C7FDA6",
        "color-blob": "#A427DF",
      }
    },
    container: {
      center: true,
      padding: {
        DEFAULT: '20px',
        md: "50px"
      }
    }
  },
  plugins: [rotateY, require('flowbite/plugin')],
}