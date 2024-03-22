/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    container: {
      center: true,
      padding: '2rem'
    },
    extend: {}
  },
  daisyui: {
    themes: ['light', 'dark', 'cupcake', 'bumblebee']
  },
  plugins: [require('daisyui')]
}