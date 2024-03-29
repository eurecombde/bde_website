export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, facebook?: string, instagram?: string, whatsapp?: string, photo?: string, president: string, vicePresident?: string };

const SPORT: Category = { name: "Sport", emoji: "🧗‍" };
const SOCIAL: Category = { name: "Social", emoji: "🍷" };
const ENTERTAINMENT: Category = { name: "Entertainment", emoji: "🎮" };
const EDUCATIONAL: Category = { name: "Educational", emoji: "📚" };

export const clubs: Club[] = [
  {
    name: "EUREClimb 🧗",
    president: "Zachari Thiry",
    category: SPORT,
    facebook: "https://www.facebook.com/groups/338295291434407/",
    photo: "/images/clubs/climbing.jpg"
  },
  {
    name: "BasketBall 🏀",
    president: "Dario Ferrero",
    vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
    category: SPORT,
    facebook: "https://www.facebook.com/groups/630853144645799/",
    whatsapp: "https://chat.whatsapp.com/KkWIvKknHEu3Vm89TvRM7t",
    photo: "/images/clubs/basketball.jpg"
  },
  {
    name: "EureHik 🥾",
    president: "Baptiste Masson",
    vicePresident: "Enguerran de Larocque Latour",
    category: SPORT,
    whatsapp: "https://chat.whatsapp.com/LUX7JH9BpEfDvb598sEOyG"
  },
  {
    name: "Tennis 😎",
    president: "Rajiv Philip Venkatraman Mohan Doss Ravi",
    vicePresident: "Marwa Essalehi",
    category: SPORT,
    whatsapp: "https://chat.whatsapp.com/JitLAVkrv9X6x4wfCqzw5q",
  },
  {
    name: "EURESwim",
    president: "Julie Schult",
    vicePresident: "Marco Klepatzky",
    category: SPORT,
    photo: "/images/clubs/swimming.jpg",
    whatsapp: "https://chat.whatsapp.com/Hde618dU9C5FoNCw7Zt6Df",
    facebook: "https://www.facebook.com/groups/448112157213407/"
  },
  {
    name: "TastEUR",
    president: "Dario Ferrero",
    vicePresident: "Emerson Cardoso",
    category: SOCIAL,
    facebook: "https://www.facebook.com/groups/1360827391047825/",
    photo: "/images/clubs/wineandbeertasting.jpg"
  },
  {
    name: "EURObOARD Club 🃏🎲♣️",
    president: "Emerson Cardoso",
    category: SOCIAL,
    whatsapp: "https://chat.whatsapp.com/CyfjC3TWSOvF7cjOcEHvAk",
    photo: "/images/clubs/boardgames.jpg",
  },
  {
    name: "Skiing",
    president: "Zachari Thiry",
    vicePresident: "Benjamin Salon",
    category: SPORT,
    whatsapp: "https://chat.whatsapp.com/BeA7KVXDeRjBLNNKtixbos",
  },
  {
    name: "Football",
    president: "Mohd Aamir",
    category: SPORT,
    facebook: "https://www.facebook.com/groups/242499421236490/",
  },
  {
    name: "Sunset Club",
    president: "Alberto Sánchez Pérez",
    category: SOCIAL,
    whatsapp: "https://chat.whatsapp.com/KwWbOWORxINBpLm2HXBd1V"
  },
  {
    name: "EureFood",
    president: "Fredrik Sveen",
    vicePresident: "Marwa Essalehi",
    category: SOCIAL,
    photo: "/images/clubs/internationalfood.jpg",
    whatsapp: "https://chat.whatsapp.com/Iw4EYYBEcXK1lD8CEFJnI9",
    facebook: "https://www.facebook.com/groups/1283501492485473/",
  },
   {
    name: "EuROCKom",
    president: "Lou Marze",
    vicePresident: "Guillaume Ung",
    category: ENTERTAINMENT,
    photo: "/images/clubs/music.jpg",
    whatsapp: "https://chat.whatsapp.com/CY9EiqSeTpQAgHWQIyGnuu",
    instagram: "https://instagram.com/eu_rock_om?igshid=YmMyMTA2M2Y=",
  },
  {
    name: "EURESound",
    president: "Marco Klepatzky",
    vicePresident: "Julie Schult",
    category: ENTERTAINMENT,
    facebook: "https://www.facebook.com/groups/388572802698498/",
    photo: "https://images.unsplash.com/photo-1485030056468-3820ff9e6e90?ixlib=rb-4.0.3&dl=modesta-zemgulyte-wMkqe4JCaAw-unsplash.jpg&q=80&fm=jpg&crop=entropy&cs=tinysrgb",
  },
  {
    name: "Beach Volley",
    president: "Anis Amor",
    vicePresident: "Enguerran de Larocque Latour",
    category: SPORT,
    photo: "/images/clubs/beachvolley.jpg",
    whatsapp: "https://www.youtube.com/watch?v=lH1m5zOImJU",
  },
  {
    name: "Scuba Diving/Snorkling",
    president: "Anis Amor",
    vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
    category: SPORT,
    photo: "/images/clubs/scubadiving.jpg",
    whatsapp: "https://www.youtube.com/watch?v=lH1m5zOImJU",
  },
  {
    name: "SAP Club",
    president: "Malek Sfaxi",
    category: EDUCATIONAL,
    photo: "/images/clubs/sap-temp.jpg",
    whatsapp: "https://chat.whatsapp.com/BPZBoNaIeMLBAoMvCyFOcC",
    facebook: "https://www.facebook.com/groups/811759806816033/",
  },
  {
    name: "CINEURO Club 🍿🎥 ",
    president: "Emerson Cardoso",
    vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
    category: ENTERTAINMENT,
    photo: "/images/clubs/moviesseries.jpg",
    whatsapp: "https://chat.whatsapp.com/IWgSjoHMHY54ha5wLfcQVd",
  },
  {
    name: "Sailing",
    president: "Gaëtan Plisson",
    vicePresident: "Zachari Thiry",
    category: SPORT,
    whatsapp: "https://www.youtube.com/watch?v=lH1m5zOImJU",
  }
];
