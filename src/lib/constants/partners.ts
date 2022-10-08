import {glass, ticket, shirtsinbulk} from 'svelte-awesome/icons';

export type Partner = { name: string, logo: string, url?: string }

export const partners: Partner[] = [
    {name: "Amadeus", logo: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Amadeus_%28CRS%29_Logo.svg",},
];
export type Offer = { name: string, icon: any, description: string, url: string }

export const offers: Offer[] = [
    {name: "ISIC", icon: ticket, description: "Student Discounts", url: "https://www.isic.fr"},
    {name: "Tailor made suits", icon: shirtsinbulk, description: "", url: ""},
];
