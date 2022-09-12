export type Section = { name: string, tag: string };
export type Page = { name: string, path: string, emoji?: string, sections?: Section[] };

export const routes: Page[] = [
    {
        name: 'Home', path: '/' ,sections: [
            {name: 'Upcoming events', tag: '#events'},
            {name: 'Places in the area', tag: '#places'},
        ]
    },
    {
        name: 'Student Life', emoji: '🏖️',  path: '/student-life', sections: [
            {name: 'Student Guides', tag: '#guides'},
            {name: 'Deals & Partners', tag: '#tips'},
            {name: 'Frequent questions', tag: '#faq'}

        ]
    },
    {
        name: 'Clubs', path: '/clubs', emoji: '🍷',sections: [
            {name: 'All', tag: '#all'},
            {name: 'Featured', tag: '#featured'}
        ]
    },
    {
        name: 'Get in touch', path: '/get-in-touch', emoji: '📮',sections: [
            {name: 'Our team', tag: '#team'},
            {name: 'Contact us', tag: '#contact'}
        ]
    },
];
