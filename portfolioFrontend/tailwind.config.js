/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        background: '#0b0c10',
        primary: '#66fcf1',
        secondary: '#c5c6c7',
        background: '#111111',
      },
      fontFamily: {
        heading: ['HeadingFont', 'sans-serif'],
        techno: ['TechnoFont', 'sans-serif'],
        techno2: ['TechnoFont2', 'sans-serif'],
      }
    },
  },
  plugins: [
    require("daisyui"),
    require("tailwindcss-animated"),
  ],
  daisyui: {
    themes: [
      "dark",
    ]
  }
}
