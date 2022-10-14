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
        photo: "https://scontent-mrs2-2.xx.fbcdn.net/v/t39.30808-6/277218931_4642730475854492_2665717225685857469_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8631f5&_nc_ohc=EhQ1RgNjypsAX8zrUEq&_nc_ht=scontent-mrs2-2.xx&oh=00_AT__HoQB6weFM_Optvmuxu6kb6AP4ikrHThdVsLSYs_jJg&oe=6349D766"
    },
    {
        president: "Baptiste Masson",
        vicePresident: "Enguerran de Larocque Latour",
        name: "Hiking / Promenade",
        category: SPORT,
        featured: true,
    },
    {
        president: "Rajiv Philip Venkatraman Mohan Doss Ravi",
        vicePresident: "Marwa Essalehi",
        name: "Tennis",
        category: SPORT,
        featured: true,
    },
    {
        president: "Julie Schult",
        vicePresident: "Marco Klepatzky",
        name: "Swimming",
        category: SPORT,
        featured: true,
    },
    {
        president: "Dario Ferrero",
        vicePresident: "Emerson Cardoso",
        name: "Wine / Beer Tasting",
        category: SOCIAL,
        featured: true,
        facebook: "https://www.facebook.com/groups/1360827391047825/",
        photo: "https://scontent-mrs2-2.xx.fbcdn.net/v/t39.30808-6/275300950_5021262621300466_1593960362518288125_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8631f5&_nc_ohc=OIxD0mpkw0wAX-7NZPE&_nc_ht=scontent-mrs2-2.xx&oh=00_AT9ukZmIQAmY6s77dNLdPdXSyVvILIKTKbsGicQdGnDcjw&oe=6348FFF8"
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
        featured: true
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
        category: SPORT
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
