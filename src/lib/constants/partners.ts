import {glass, ticket, shirtsinbulk} from 'svelte-awesome/icons';

export type Partner = { name: string, logo: string, url?: string }

export const partners: Partner[] = [
    {name: "Amadeus", logo: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Amadeus_%28CRS%29_Logo.svg",},
    {name: "Red Bull", logo: "https://upload.wikimedia.org/wikipedia/en/f/f5/RedBullEnergyDrink.svg"},
];
export type Offer = { name: string, icon: any, description: string, url: string }

export const offers: Offer[] = [
    {name: "ISIC", icon: ticket, description: "Student Discounts", url: "https://www.isic.fr"},
    {
        name: "Red Bull",
        icon: glass,
        description:
            "We are working in collaboration with Red Bull to elevate our parties to the next level. " +
            "They provide bulks of beverages and equipment for reduced prices and in return we take pictures at our events with their cans.",
        url: "https://www.redbull.com"
    },
    {name: "Tailor made suits", icon: shirtsinbulk, description: "", url: ""},
];
