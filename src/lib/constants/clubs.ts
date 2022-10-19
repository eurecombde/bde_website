export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, facebook?: string, whatsapp?: string, photo?: string, featured?: boolean, president: string, vicePresident?: string };

const SPORT: Category = { name: "Sport", emoji: "🧗‍" };
const SOCIAL: Category = { name: "Social", emoji: "🍷" };
const ENTERTAINMENT: Category = { name: "Entertainment", emoji: "🎮" };
const EDUCATIONAL: Category = { name: "Educational", emoji: "📚" };

export const clubs: Club[] = [
  {
    president: "Zachari Thiry",
    name: "Climbing",
    category: SPORT,
    featured: true,
    facebook: "https://www.facebook.com/groups/338295291434407/",
    photo: "/images/clubs/climbing.jpg"
  },
  {
    president: "Dario Ferrero",
    vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
    name: "Basketball",
    category: SPORT,
    featured: true,
    facebook: "https://www.facebook.com/groups/630853144645799/",
    whatsapp: "https://chat.whatsapp.com/KkWIvKknHEu3Vm89TvRM7t",
    photo: "/images/clubs/basketball.jpg"
  },
  {
    president: "Baptiste Masson",
    vicePresident: "Enguerran de Larocque Latour",
    name: "Hiking / Promenade",
    category: SPORT,
    whatsapp: "https://chat.whatsapp.com/LUX7JH9BpEfDvb598sEOyG"
  },
  {
    president: "Rajiv Philip Venkatraman Mohan Doss Ravi",
    vicePresident: "Marwa Essalehi",
    name: "Tennis",
    category: SPORT,
    whatsapp: "https://chat.whatsapp.com/JitLAVkrv9X6x4wfCqzw5q",

  },
  {
    president: "Julie Schult",
    vicePresident: "Marco Klepatzky",
    name: "Swimming",
    category: SPORT,
    photo: "/images/clubs/swimming.jpg",
    whatsapp: "https://chat.whatsapp.com/Hde618dU9C5FoNCw7Zt6Df",
    facebook: "https://www.facebook.com/groups/448112157213407/?ref=share"
  },
  {
    president: "Dario Ferrero",
    vicePresident: "Emerson Cardoso",
    name: "Wine / Beer Tasting",
    category: SOCIAL,
    featured: true,
    facebook: "https://www.facebook.com/groups/1360827391047825/",
    photo: "/images/clubs/wineandbeertasting.jpg"
  },
  {
    president: "Emerson Cardoso",
    vicePresident: "Marwa Essalehi",
    name: "Board Games",
    category: SOCIAL,
    whatsapp: "https://chat.whatsapp.com/CyfjC3TWSOvF7cjOcEHvAk",
    photo: "/images/clubs/boardgames.jpg",
  },
  {
    president: "Clara Léonet",
    vicePresident: "Zachari Thiry",
    name: "Skiing",
    category: SPORT
  },
  {
    president: "Mohd Aamir",
    name: "Football",
    category: SPORT,
    featured: true
  },
  {
    president: "Alberto Sánchez Pérez",
    vicePresident: "Marwa Essalehi",
    name: "Sunset (Art) Club",
    category: SOCIAL,
    whatsapp: "https://chat.whatsapp.com/KwWbOWORxINBpLm2HXBd1V"
  },
  {
    president: "Fredrik Sveen",
    vicePresident: "Marwa Essalehi",
    name: "International Food",
    category: SOCIAL
  },
  {
    president: "Marco Klepatzky",
    vicePresident: "Julie Schult",
    name: "DJing",
    category: ENTERTAINMENT,
    featured: true
  },
  {
    president: "Anis Amor",
    vicePresident: "Enguerran de Larocque Latour",
    name: "Beach Volley",
    category: SPORT,
    featured: true,
    photo: "/images/clubs/beachvolley.jpg",
  },
  {
    president: "Anis Amor",
    vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
    name: "Scuba Diving/Snorkling",
    category: SPORT,
    photo: "/images/clubs/scubadiving.jpg"
  },
  {
    president: "Malek Sfaxi",
    vicePresident: "Marwa Essalehi",
    name: "SAP",
    category: EDUCATIONAL,
    photo: "/images/clubs/sap.png",
    whatsapp: "https://chat.whatsapp.com/BPZBoNaIeMLBAoMvCyFOcC",
    facebook: "https://www.facebook.com/groups/811759806816033/?ref=share",
  },
  {
    president: "Emerson Cardoso",
    vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
    name: "Movies / Series",
    category: ENTERTAINMENT,
    photo: "/images/clubs/moviesseries.jpg",
    whatsapp: "https://chat.whatsapp.com/IWgSjoHMHY54ha5wLfcQVd",
  },
  {
    president: "Gaëtan Plisson",
    vicePresident: "Zachari Thiry",
    name: "Sailing",
    category: SPORT
  }
];
