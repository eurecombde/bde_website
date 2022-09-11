import {CALENDAR_ID, SCOPES, SERVICE_ACCOUNT_EMAIL, SERVICE_ACCOUNT_PRIVATE_KEY} from '$env/static/private';
import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarEvent} from "../types/calendar-event";

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<{ events:CalendarEvent[] ,calendar: string, error: string}> {
    const auth = new Auth.JWT(SERVICE_ACCOUNT_EMAIL, undefined, SERVICE_ACCOUNT_PRIVATE_KEY, SCOPES);
    const calendar = Calendar({version: 'v3', auth});

    try {
        console.debug('Fetching calendar events from', CALENDAR_ID);
        const events = await calendar.events.list({
            calendarId: CALENDAR_ID,
            // timeMin: (new Date()).toISOString(), // From now to the future // todo: should this be from yesterday to show events that are happing now?
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });

        console.debug('Received events', events.data.items);

        if (!events.data.items) return {events: [], calendar: CALENDAR_ID, error: 'no items found'};
        return {events: events.data.items.map((event: any) => event as CalendarEvent), calendar: CALENDAR_ID, error: ''};
    } catch (err) {
        console.error('Google Calendar returned an error: ' + err);
        return {events: [], calendar: CALENDAR_ID, error: 'Google Calendar returned an error: ' + err}; // todo: +error.svelte & throw error(500,'fubar')
    }
}
