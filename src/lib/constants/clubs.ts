export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, groupLink?: string, photo?: string, featured?: boolean };

const SPORT: Category = {name: "Sport", emoji: "🧗‍"};
const SOCIAL: Category = {name: "Social", emoji: "🍷"};
const ENTERTAINMENT: Category = {name: "Entertainment", emoji: "🎮"};
export const clubs: Club[] = [
    {name: "Climbing", category: SPORT, featured: true},
    {name: "Basketball", category: SPORT, featured: true},
    {name: "Wine tasting", category: SOCIAL, featured: true},
    {name: "Board Games", category: SOCIAL, featured: false},
];
