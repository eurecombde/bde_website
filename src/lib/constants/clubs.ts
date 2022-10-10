export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, groupLink?: string, photo?: string, featured?: boolean };

const SPORT: Category = {name: "Sport", emoji: "🧗‍"};
const SOCIAL: Category = {name: "Social", emoji: "🍷"};
const ENTERTAINMENT: Category = {name: "Entertainment", emoji: "🎮"};
const EDUCATIONAL: Category = {name: "Educational", emoji: "📚"};

export const clubs: Club[] = [
    {name: "Climbing", category: SPORT, featured: true, groupLink: "https://www.facebook.com/groups/338295291434407/"},
    {name: "Basketball", category: SPORT, featured: true, groupLink: "https://www.facebook.com/groups/630853144645799/"},
    {name: "Wine & Beer", category: SOCIAL, featured: true, groupLink: "https://www.facebook.com/groups/1360827391047825/"},
    {name: "Board Games", category: SOCIAL},
    {name: "Skiing", category: SPORT},
    {name: "Football", category: SPORT, featured: true},
    {name: "Sunset (Art)", category: SOCIAL},
    {name: "International Food", category: SOCIAL, featured: true},
    {name: "DJing", category: ENTERTAINMENT, featured: true},
    {name: "Beach Volley", category: SPORT},
    {name: "Scuba Diving/Snorkling", category: SPORT},
    {name: "SAP", category: EDUCATIONAL},
    {name: "Sailing", category: SPORT},
];