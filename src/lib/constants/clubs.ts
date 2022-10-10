export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, groupLink?: string, photo?: string, featured?: boolean };

const SPORT: Category = {name: "Sport", emoji: "🧗‍"};
const SOCIAL: Category = {name: "Social", emoji: "🍷"};
const ENTERTAINMENT: Category = {name: "Entertainment", emoji: "🎮"};
const EDUCATIONAL: Category = {name: "Educational", emoji: "👨‍💻"};

export const clubs: Club[] = [
    {name: "Climbing", category: SPORT, featured: true},
    {name: "Basketball", category: SPORT, featured: true},
    {name: "Wine & Beer", category: SOCIAL, featured: true},
    {name: "Board Games", category: SOCIAL, featured: false},
    {name: "Skiing", category: SPORT, featured: false},
    {name: "Football", category: SPORT, featured: true},
    {name: "Sunset (Art)", category: SOCIAL, featured: false},
    {name: "International Food", category: SOCIAL, featured: true},
    {name: "DJing", category: ENTERTAINMENT, featured: true},
    {name: "Beach Volley", category: SPORT, featured: false},
    {name: "Scuba Diving/Snorkling", category: SPORT, featured: false},
    {name: "SAP", category: EDUCATIONAL, featured: false},
    {name: "Sailing", category: SPORT, featured: false},
];