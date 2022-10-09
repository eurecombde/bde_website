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
        description: 'A guide to the best bars and clubs in the area.',
        // image: 'https://images.unsplash.com/photo-1517436073-3b8b4f3b5f9c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
        author: 'John Doe',
        date: '2020-01-01',
        tags: ['bars', 'clubs', 'nightlife'],
        content: `
        Dette kan bli bra
        eller hva tenker du?
        `
    }
];
