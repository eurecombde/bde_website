import {CALENDAR_ID, API_KEY} from '$env/static/private';

import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarEvent} from "$lib/types/calendar-event";

/** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[] ,calendar: string, error: string}>>} */
export async function load(): Promise<{ events: CalendarEvent[], error?: any }> {
    const auth = Auth.fromAPIKey(API_KEY);
    const calendar = Calendar({version: 'v3', auth});
    try {
        console.debug('+page.server#load', 'Fetching Google Calendar events from', CALENDAR_ID);
        const events = await calendar.events.list({
            calendarId: CALENDAR_ID,
            // timeMin: (new Date()).toISOString(), // From now to the future // todo: should this be from yesterday to show events that are happing now?
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });
        console.debug('+page.server#load', 'Received events', events.data.items);
        if (!events.data.items) return {events: [], error: 'No events found'};
        return {events: events.data.items.map((event: any) => event as CalendarEvent)};
    } catch (err) {
        console.error('+page.server#load', 'Google Calendar returned an error');
        console.error(err)
        return {events: [], error: err};
    }
}
