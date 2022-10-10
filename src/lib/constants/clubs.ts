export type Category = { name: string, emoji: string };
export type Club = { name: string, category: Category, groupLink?: string, photo?: string, featured?: boolean };

const SPORT: Category = {name: "Sport", emoji: "🧗‍"};
const SOCIAL: Category = {name: "Social", emoji: "🍷"};
const ENTERTAINMENT: Category = {name: "Entertainment", emoji: "🎮"};
const EDUCATIONAL: Category = {name: "Educational", emoji: "📚"};

export const clubs: Club[] = [
    {name: "Climbing", category: SPORT, featured: true, groupLink: "https://www.facebook.com/groups/338295291434407/", photo: "/images/clubs/climbing.jpg"},
    {name: "Basketball", category: SPORT, featured: true, groupLink: "https://www.facebook.com/groups/630853144645799/", photo: "https://scontent-mrs2-2.xx.fbcdn.net/v/t39.30808-6/277218931_4642730475854492_2665717225685857469_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8631f5&_nc_ohc=EhQ1RgNjypsAX8zrUEq&_nc_ht=scontent-mrs2-2.xx&oh=00_AT__HoQB6weFM_Optvmuxu6kb6AP4ikrHThdVsLSYs_jJg&oe=6349D766"},
    {name: "Wine & Beer", category: SOCIAL, featured: true, groupLink: "https://www.facebook.com/groups/1360827391047825/", photo: "https://scontent-mrs2-2.xx.fbcdn.net/v/t39.30808-6/275300950_5021262621300466_1593960362518288125_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8631f5&_nc_ohc=OIxD0mpkw0wAX-7NZPE&_nc_ht=scontent-mrs2-2.xx&oh=00_AT9ukZmIQAmY6s77dNLdPdXSyVvILIKTKbsGicQdGnDcjw&oe=6348FFF8"},
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
