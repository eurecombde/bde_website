import {CALENDAR_ID, SCOPES, SERVICE_ACCOUNT_EMAIL, SERVICE_ACCOUNT_PRIVATE_KEY} from '$env/static/private';
import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarEvent} from "../types/calendar-event";

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<CalendarEvent[]> {
    const auth = new Auth.JWT(SERVICE_ACCOUNT_EMAIL, undefined, SERVICE_ACCOUNT_PRIVATE_KEY, SCOPES);
    const calendar = Calendar({version: 'v3', auth});

    try {
        const events = await calendar.events.list({
            calendarId: CALENDAR_ID,
            // timeMin: (new Date()).toISOString(), // From now to the future // todo: should this be from yesterday to show events that are happing now?
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });

        if (!events.data.items) return [];
        return events.data.items.map((event: any) => event as CalendarEvent);
    } catch (err) {
        console.error('The API returned an error: ' + err);
        return []; // todo: +error.svelte & throw error(500,'fubar')
    }
}
