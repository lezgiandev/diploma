/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {
      colors: {
        navbar: {
          main: '#262626',
          text: '#FFFFFF',
          colored: '#6366f1',
          exit: '#EF4444'
        },
        footer: {
          main: '#262626',
          heading: '#FFFFFF',
          content: '#A3A3A3',
          hover: '#6366f1',
          border: '#FFFFFF'
        },
        font: {
          colored: '#6366f1',
          main: '#e0e7ff'
        },
        background: {
          one: '#171717',
          two: '#262626',
          three: '#404040'
        },
        button: {
          main: '#6366f1',
          mainhover: '#4338ca',
          text: '#FFFFFF',
          cancel: '#ef4444',
          cancelhover: '#b91c1c',
        },
      },
      fontFamily: {
        great: ['Aremat', 'serif'],
        main: ['Nunito', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
