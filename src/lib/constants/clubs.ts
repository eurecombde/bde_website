export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, facebook?: string, whatsapp?: string, photo?: string, featured?: boolean, president: string, vicePresident?: string };

const SPORT: Category = {name: "Sport", emoji: "🧗‍"};
const SOCIAL: Category = {name: "Social", emoji: "🍷"};
const ENTERTAINMENT: Category = {name: "Entertainment", emoji: "🎮"};
const EDUCATIONAL: Category = {name: "Educational", emoji: "📚"};

export const clubs: Club[] = [
    {
        president: "Zachari Thiry",
        name: "Climbing",
        category: SPORT,
        featured: true,
        facebook: "https://www.facebook.com/groups/338295291434407/",
        photo: "/images/clubs/climbing.jpg",
    },
    {
        president: "Dario Ferrero",
        vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
        name: "Basketball",
        category: SPORT,
        featured: true,
        facebook: "https://www.facebook.com/groups/630853144645799/",
        whatsapp: "https://chat.whatsapp.com/KkWIvKknHEu3Vm89TvRM7t",
        photo: "/images/clubs/basketball.jpg",
    },
    {
        president: "Baptiste Masson",
        vicePresident: "Enguerran de Larocque Latour",
        name: "Hiking / Promenade",
        category: SPORT,
    },
    {
        president: "Rajiv Philip Venkatraman Mohan Doss Ravi",
        vicePresident: "Marwa Essalehi",
        name: "Tennis",
        category: SPORT,
    },
    {
        president: "Julie Schult",
        vicePresident: "Marco Klepatzky",
        name: "Swimming",
        category: SPORT,
    },
    {
        president: "Dario Ferrero",
        vicePresident: "Emerson Cardoso",
        name: "Wine / Beer Tasting",
        category: SOCIAL,
        featured: true,
        facebook: "https://www.facebook.com/groups/1360827391047825/",
        photo: "/images/clubs/wineandbeertasting.jpg",
    },
    {
        president: "Emerson Cardoso",
        vicePresident: "Marwa Essalehi",
        name: "Board Games",
        category: SOCIAL
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
        category: SOCIAL
    },
    {
        president: "Fredrik Sveen",
        vicePresident: "Marwa Essalehi",
        name: "International Food",
        category: SOCIAL,
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
    },
    {
        president: "Anis Amor",
        vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
        name: "Scuba Diving/Snorkling",
        category: SPORT
    },
    {
        president: "Malek Sfaxi",
        vicePresident: "Marwa Essalehi",
        name: "SAP",
        category: EDUCATIONAL
    },
    {
        president: "Emerson Cardoso",
        vicePresident: "Leonardo Zadkiel Mosqueda Hernández",
        name: "Movies / Series",
        category: ENTERTAINMENT
    },
    {
        president: "Gaëtan Plisson",
        vicePresident: "Zachari Thiry",
        name: "Sailing",
        category: SPORT
    },
];
