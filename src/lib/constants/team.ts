import { linkedinSquare, githubSquare, facebookSquare, instagram } from "svelte-awesome/icons";

export const contact = {
  brand: "Broken BED",
  university: "EURECOM",
  tagline: "EURECOM student association since 2021",
  address:
    "BDE EURECOM\n" +
    "CS 50193 - 450 Route des Chappes\n" +
    "F-06904 Biot Sophia Antipolis",
  phone: "+33 (0)493008221",
  emails: [
    "bde@eurecom.fr",
    "bureau.bde@eurecom.fr"
  ],
  eurecom: "https://www.eurecom.fr/en/student-life/student-association",
  socials: [
    { name: "Facebook", url: "https://www.facebook.com/groups/718500665824140", icon: facebookSquare },
    { name: "Instagram", url: "https://www.instagram.com/eurecom_bde", icon: instagram }
  ]
};

export const team = [
  {
    name: "Victoire",
    role: "BDE President",
    socials: [],
    photo: "/images/BDE2023Members/Victoire.JPG"
  },
  {
    name: "Barth",
    role: "Vice-président",
    socials: [],
    photo: "/images/BDE2023Members/Barth.JPG"
  },
  {
    name: "Davesne Gabin",
    role: "Treasurer",
    photo: "/images/BDE2023Members/Gabin.JPG",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/gabin-davesne-1a8424266/",
        icon: linkedinSquare
      }]
  },
  {
    name: "Sahra",
    role: "BDE Secretary",
    socials: [],
    photo: "/images/BDE2023Members/Sahra.JPG",
  },
  {
    name: "Alan",
    role: "BDE Secretary",
    photo: "/images/BDE2023Members/Alan.JPG",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/abdea",
        icon: linkedinSquare
      }]
  },
  {
    name: "Anni",
    role: "Events Member",
    photo: "/images/BDE2023Members/Anni.JPG",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/anni-ranta-lassila/",
        icon: linkedinSquare
      }]
  },


  {
    name: "Cindy",
    role: "Communications Member",
    photo: "/images/BDE2023Members/Cindy.jpg",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/cindy-do-637343244/",
        icon: linkedinSquare
      }]
  },
  {
    name: "Emilie",
    role: "WES Responsible",
    socials: [],
    photo: "/images/BDE2023Members/Emilie.JPG",
  },
  {
    name: "Lenia Malki",
    role: "Communications Member & Website Responsible",
    photo: "/images/BDE2023Members/Lenia.jpg",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/lenia-malki/",
        icon: linkedinSquare
      }]
  },
  {
    name: "Lina",
    role: "Events Responsible",
    photo: "/images/BDE2023Members/Lina.JPG",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/lina-chiadmi-EURECOMstudent/",
        icon: linkedinSquare
      }]
  },
  {
    name: "Madleen",
    role: "Business Officer - PromoTrip Responsible",
    socials: [],
    photo: "/images/BDE2023Members/Madleen.JPG",
  },
  {
    name: "Marwa B",
    role: "Communications Responsible - Club Officer",
    photo: "/images/BDE2023Members/MarwaB.jpg",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/marwa-boulaich-811439261",
        icon: linkedinSquare
      }]
  },
  {
    name: "Marwa E",
    socials: [],
    role: "Communications Member",
  },
  {
    name: "Meriem",
    role: "Events Member",
    photo: "/images/BDE2023Members/Meriem.JPG",
    socials: [{
        name: "LinkedIn",
        link: "https://www.linkedin.com/in/meriem-driss-383452254",
        icon: linkedinSquare
      }]
  }
];
