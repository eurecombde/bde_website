export enum ChangeFrequency {
    DAILY = 'daily',
    WEEKLY = 'weekly',
    MONTHLY = 'monthly',
    YEARLY = 'yearly',
    NEVER = 'never'
};
export type Section = { name: string, tag: string, priorty?: number, changefequency?: ChangeFrequency };
export type Page = { name: string, path: string, emoji?: string, sections?: Section[], priorty?: number, changefequency?: ChangeFrequency };
export const domain = 'bde.eurecom.fr';
export const routes: Page[] = [
    {
        name: 'Home', path: '/', priorty: 1, changefequency: ChangeFrequency.DAILY, sections: [
            { name: 'Upcoming events', tag: '#events', priorty: 1, changefequency: ChangeFrequency.DAILY, },
        ]
    },
    // {
    //     name: 'Student Life', emoji: '🏖️',  path: '/student-life', sections: [
    //         {name: 'Student Guides', tag: '#guides'},
    //         {name: 'Deals & Partners', tag: '#tips'},
    //         {name: 'Frequent questions', tag: '#faq'}
    //         {name: 'Places in the area', tag: '#places'},
    //     ]
    // },
    {
        name: 'Clubs', path: '/clubs', priorty: 1, changefequency: ChangeFrequency.DAILY, emoji: '🍷', sections: [
            { name: 'All', tag: '#all', priorty: 1, changefequency: ChangeFrequency.DAILY, },
            // todo: Add all other categories here
        ]
    },
    {
        name: 'About', path: '/about', priorty: 0.5, changefequency: ChangeFrequency.MONTHLY, emoji: '🏢', sections: [
            { name: 'The team', tag: '#team', priorty: 0.4, changefequency: ChangeFrequency.MONTHLY, },
            { name: 'Partners', tag: '#partners', priorty: 0.2, changefequency: ChangeFrequency.MONTHLY, },
            { name: 'Contact us', tag: '#contact', priorty: 0.4, changefequency: ChangeFrequency.NEVER, }
        ]
    },
];
