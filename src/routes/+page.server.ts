import {CALENDAR_ID, SCOPES, GOOGLE_API_CRED} from '$env/static/private';

import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarEvent} from "../types/calendar-event";

/** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[] ,calendar: string, error: string}>>} */
export async function load(): Promise<{ events:CalendarEvent[] ,calendar: string, error: string}> {
    const auth = Auth.fromJSON(JSON.parse(GOOGLE_API_CRED));
    const calendar = Calendar({version: 'v3', auth});
    try {
        const message = await auth.request({url: 'https://www.googleapis.com/calendar/v3/calendars/' + CALENDAR_ID + '/events'});
        console.log('message',message);

        console.debug('+page.server#load','Fetching calendar events from', CALENDAR_ID);
        const events = await calendar.events.list({
            calendarId: CALENDAR_ID,
            // timeMin: (new Date()).toISOString(), // From now to the future // todo: should this be from yesterday to show events that are happing now?
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });

        console.debug('+page.server#load','Received events', events.data.items);

        if (!events.data.items) return {events: [], calendar: CALENDAR_ID + ', ' + SCOPES , error: 'no items found'};
        return {events: events.data.items.map((event: any) => event as CalendarEvent), calendar: CALENDAR_ID+', '+ SCOPES, error: ''};
    } catch (err) {
        console.error('+page.server#load','Google Calendar returned an error: '+err);
        console.error(err)
        return {events: [], calendar: CALENDAR_ID + ', ' + SCOPES, error: 'Google Calendar returned an error: ' + err}; // todo: +error.svelte & throw error(500,'fubar')
    }



    return {events: [], calendar: CALENDAR_ID + ', ' + SCOPES, error: ''};

}
