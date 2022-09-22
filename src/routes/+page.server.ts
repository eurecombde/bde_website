import {CALENDAR_ID, API_KEY} from '$env/static/private';

import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarEvent} from "$lib/types/calendar-event";

/** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[], ical: string, error: string}>>} */
export async function load(): Promise<{ events: CalendarEvent[], ical: string, error?: any }> {
    const ical = `https://calendar.google.com/calendar/ical/${CALENDAR_ID.replace("@", "%40")}/public/basic.ics`
    const auth = Auth.fromAPIKey(API_KEY);
    const calendar = Calendar({version: 'v3', auth: auth});

    const today = new Date();
    today.setHours(0);

    try {
        const events = await calendar.events.list({
            calendarId: CALENDAR_ID,
            timeMin: today.toISOString(), // todo: should this be from yesterday to show events that are happing now?
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });
        if (!events.data.items) return {events: [], ical, error: 'No events found'};
        return {events: events.data.items.map((event: any) => event as CalendarEvent), ical};
    } catch (error) {
        console.error('+page.server#load', '|', 'Google Calendar returned an error');
        console.error(error)
        return {events: [], ical, error: "We failed to fetch the events"};
    }
}
