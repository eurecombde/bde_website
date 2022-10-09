export type Guide = {
    name: string,
    slug: string,
    description: string,
    image?: string,
    tags: string[],
    content: string,
    author: string,
    date: string,
};
export const guides: Guide[] = [
    {
        name: 'Bars and Clubs',
        slug: 'bars-and-clubs',
        description: 'The best bars and clubs in the area.',
        // image: 'https://images.unsplash.com/photo-1517436073-3b8b4f3b5f9c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
        author: 'TBC',
        date: '2020-01-01',
        tags: ['bars', 'clubs', 'nightlife'],
        content: `
        Dette kan bli bra
        eller hva tenker du?
        `
    },

    {
        name: 'Getting to around the area',
        slug: 'transport',
        description: 'How to get around the area.',
        // image: 'https://images.unsplash.com/photo-1517436073-3b8b4f3b5f9c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
        author: 'TBC',
        date: '2022-01-01',
        tags: ['transport', 'buses', 'trains'],
        content: `
        How to get around Antibes and the surrounding area by public transport?
         
        `
    }
];
