export type Section = { name: string, tag: string };
export type Page = { name: string, path: string, sections?: Section[] };

export const routes: Page[] = [
    {
        name: 'Home', path: '/', sections: [
            {name: 'Upcoming events', tag: '#events'},
            {name: 'Places in the are', tag: '#places'},
            {name: 'Deals & Partners', tag: '#partners'},
            {name: 'Frequent questions', tag: '#faq'}
        ]
    },
    {
        name: 'Student Life', path: '/student-life', sections: [
            {name: 'Bars', tag: '#events'},
            {name: 'What to expect', tag: '#expectations'}
        ]
    },
    {
        name: 'Get in touch', path: '/get-in-touch', sections: [
            {name: 'Our team', tag: '#team'},
            {name: 'Contact us', tag: '#contact'}
        ]
    },
];
