/** @type {import('tailwindcss').Config} */

export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '1rem',
        lg: '2rem',
        xl: '2rem',
        '2xl': '2rem'
      }
    },
    fontFamily: {
      'body': ['Geologica']
    },
    extend: {}
  },
  daisyui: {
    themes: ['light', 'dark', 'cupcake', 'bumblebee']
  },
  plugins: [require('daisyui')]
}