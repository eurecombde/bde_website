import {linkedinSquare, githubSquare, facebookSquare, instagram} from 'svelte-awesome/icons';

export const contact = {
    brand: 'BEDrock',
    university: 'EURECOM',
    tagline: 'EURECOM student association since 2021',
    address:
        'Eurecom\n' +
        'CS 50193 - 450 Route des Chappes\n' +
        'F-06904 Biot Sophia Antipolis',
    phone: '+33 (0)493008221',
    emails: [
        'bde@eurecom.fr',
        'bureau.bde@eurecom.fr',
    ],
    eurecom: 'https://www.eurecom.fr/en/student-life/student-association',
    socials: [
        {name: 'Facebook', url: 'https://www.eurecom.fr/en/student-life/student-association', icon: facebookSquare},
        {name: 'Instagram', url: 'https://www.eurecom.fr/en/student-life/student-association', icon: instagram},
    ]
}

export const team = [
    {
        name: "Lorenzo Pisanò",
        role: "BDS President",
        socials: []
    },
    {
        name: "Robert Moller",
        role: "BDE President",
        photo: "https://avatars.githubusercontent.com/u/33206528?v=4",
        socials: [
            {
                name: "LinkedIn",
                link: "https://www.linkedin.com/in/roberthmoller/",
                icon: linkedinSquare
            },
            {
                name: "GitHub",
                link: "https://github.com/roberthmoller/",
                icon: githubSquare
            },
        ]
    },
    {
        name: "Eloïse Coupin",
        role: "BDE/S Treasurer",
        socials: []
    },
    {
        name: "Clara Leonet",
        role: "BDE Secretary",
        socials: []
    },
    {
        name: "Lucas Georget",
        role: "BDS Secretary",
        socials: []
    },
    {
        name: "Zachari Thiry",
        role: "BDE/S Events & Logistics",
        socials: []
    },
    {
        name: "I will add more late",
        role: "BDE/S Officers",
        socials: []
    },
];
