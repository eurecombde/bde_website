
export type OpenGraphMeta = {
    title: string,
    description: string,
    locale: string,
    icon: string,
    image: {
        url: string,
        alt: string,
    },
    url: string,
    domain: string,
    type: string,
}

export const defaultMeta: OpenGraphMeta = {
    title: "EURECOM BDE",
    description: "EURECOM Student Union - BDE",
    locale: "en_FR",
    icon: "/favicon.png",
    image: {
        url: "/images/hero1.jpg",
        alt: "Photo of the members in the EURECOM BDE",
    },
    url: "https://bde.eurecom.fr",
    domain: "bde.eurecom.fr",
    type: "website",
}

export function metaOf(meta: Partial<OpenGraphMeta>): OpenGraphMeta {
    return Object.assign({}, defaultMeta, meta);
}
