// import * as api from '$lib/api';
//
// /** @type {import('./$types').PageLoad} */
// export async function load({depends}) {
//     depends(`${api.base}/api/v1/calendar`);
//
//     return {
//         foo: api.client.get('/api/v1/calendar')
//     }
// }

import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";

const {CALENDAR_ID, SCOPES, SERVICE_ACCOUNT_EMAIL, SERVICE_ACCOUNT_PRIVATE_KEY} = {
    CALENDAR_ID: "https://www.googleapis.com/auth/calendar.readonly",
    SCOPES: "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCfmZ/Km0k0UQk0\nIB4FGF/xxwXFI4rNFaU4w5Cj6qVnUCj5SmhGOUbJXDUxu96duarRY9wZFkXLPmmb\nW1sXMNh5C+hqpA5M6iHf09qCztdGMWN4wM20OtemblwXduJ4quHSEyc/fTHgd7Jy\ns7KohdOI7omho4w+nPQ7YFqFsXRiMvpGobDWuNvEwVVEtLM03g2TXI7SAmxhsXW/\neYi5/NyCiaBD8c42qrlc9VEpjUlB4hNVwlnjwUzvv/WzdamGmhEm3CbOm/HcFI3p\n2cDENFfuxrMzVG9UWFZrSo6enciBzoV7iI64HB345WFpXUi0dihob5wbYa2Ec3Sg\nOIUG9qmtAgMBAAECggEAGzj+bvYWwfQykDAMPs0+DETowIwD8GBJSsncwYDUDq+3\nFXJyH8xEPTNbpWyIl7mkH8wbLjJE3Fp8c/HcszNzMQ5taccq40aqWX3OzzINuRzS\nfTXRwHSq9OntDlmKXo+zLfxzXNpzZ/iyuOraxfDxuHELi8UUNlfaNsiEGDrBAcCw\nMHuABrbBCI/xKi1/zQAw4w7Cd0nzsBIiCJ6kUcXfhMflMcVA2TCmcX/lGHNvLJJ+\nKLaAOoOlAsU2iBVSAN0ic2Z6pY1p9lWpwfH7wcZ2NAfMTPZ7IgyUhbTkWIJlIGwK\n/ikQwIjiwUvjSdL+rVuo1zfud5Weks9qktAH3IMjZwKBgQDU4xPT8Lbpf3hXn+Wd\n8iEAVCtKMsfy2320baelZkFPTN0uuFSqPQca0IeCfg8jEHZ0aDYNXIQQVK4vG0rv\nVMvxTooP29jRJOWxD64yosfluc2t69axwI2TAUlJKJOatUMWOkjMxiMBRZ5ixH1F\ns5cEzcOB+ji913oD7PQjCmALowKBgQC/6+/1plAurTAgXt19A5+L1qVC+NSz5gwi\nRAGpPYl7rOMktVdBTSL4JUwp1M5BH+WwmlVNo32Zh2dZq4KhmDRNSpw4LVSVda7a\n2IzSsMePBEYEm/Gp6oCP5yZnfpCd4ZY+8Lo5J5TYLQ/ndpjM+6pWBhVrhQqFG2Rs\n56aoq4HKbwKBgCxOtqm9x9QBO8LA/MFKy6ON4RSoTQU2uYr755B9H8qpbL90jeqA\nmSHzlMCMDAp4Oq8voVBWmQXtGfOj8oytUWT/u6xhTVb6HvQjF1ZimsgtS6mPFDga\no1ydP+uCDnZ8k2Hk75HvCwoQu05DJu+C2UOer7o1oemhFzwJ7SX92s+RAoGBAJHq\nbSeESiQi0ptZ5OXeclgcWsufagBY4FLRB75HphacrJnFMdDZN8QYf16yiBoliTmL\nLV349k5bDy2y43++u80j88AWXt+/eLC0weSSOTc4FY/9jHAWdaZzJNS8+nC/Cb9S\nwRMhT95H7HabybLXiHsc5v43SXdIC0NtoF1PAEALAoGAYiv+SkNG0GdOy/zJFGo0\nc25ZceLzlD/l3lolB2Ebna+OziMCQKtOsFmXVjAY2xdQkvh2nKEaUTXwRtt+V/rQ\nji6Y7xfx6Ey0g7OUIe5RszCrpsV1DOx7Atu+E8147mEzLqpM8cOihFKMmRtMp8AN\nSROAypcwn5gEM8UhosIhb0s=\n-----END PRIVATE KEY-----\n",
    SERVICE_ACCOUNT_EMAIL: "public-access@bde-website-362120.iam.gserviceaccount.com",
    SERVICE_ACCOUNT_PRIVATE_KEY: "robert@hjortsholm.com"
};

/** @type {import('./$types').PageLoad} */
export async function load() {
    const auth = new Auth.JWT(SERVICE_ACCOUNT_EMAIL, undefined, SERVICE_ACCOUNT_PRIVATE_KEY, SCOPES);
    const calendar = Calendar({version: 'v3', auth});
    console.debug('+page#load')
    try {
        console.debug('+page#load', 'Fetching calendar events from', CALENDAR_ID);
        const events = await calendar.events.list({
            calendarId: CALENDAR_ID,
            // timeMin: (new Date()).toISOString(), // From now to the future // todo: should this be from yesterday to show events that are happing now?
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });

        console.debug('+page#load', 'Received events', events.data.items);
    } catch (err) {
        console.error('+page#load', 'Google Calendar returned an error: ' + err);
    }
}
