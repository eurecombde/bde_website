import {CLUB_CALENDAR_ID, API_KEY} from '$env/static/private';

import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarDate, CalendarEvent} from "$lib/types/calendar-event";
import {asDate} from "$lib/types/calendar-event";

/** @type {import('./$types').PageServerLoad<Promise<{ weekEvents: { name: string, events: CalendarEvent[] }, ical: string, error: string}>>} */
export async function load(): Promise<{ ical: string; weekEvents: { date: Date; name: string; events: CalendarEvent[] }[]; error?: string }> {
    const ical = `https://calendar.google.com/calendar/ical/${CLUB_CALENDAR_ID.replace("@", "%40")}/public/basic.ics`
    const auth = Auth.fromAPIKey(API_KEY);
    const calendar = Calendar({version: 'v3', auth: auth});

    const today = new Date();
    today.setHours(0);
    const nextWeek = new Date(today.getFullYear(), today.getMonth(), today.getDate() + 6);
    const weekdays = [0, 1, 2, 3, 4, 5, 6]
        .map((days) => new Date(today.getFullYear(), today.getMonth(), today.getDate() + days))
        .map((date) => ({name: date.toLocaleDateString('en-US', {weekday: 'long'}), events: [], date}));

    try {
        const response = await calendar.events.list({
            calendarId: CLUB_CALENDAR_ID,
            timeMin: today.toISOString(), // todo: should be start of the current week // today
            timeMax: nextWeek.toISOString(), // todo: should be 7 days from now
            singleEvents: true,
            orderBy: 'startTime',
        });
        if (!response.data.items) return {weekEvents: weekdays, ical, error: 'No events found'};
        const events = response.data.items.map((event: any) => event as CalendarEvent);

        const weekEvents = weekdays.map((weekday) => ({
            ...weekday, events: events.filter((event) => asDate(event.start).getDate() == weekday.date.getDate())
        }));

        return {weekEvents, ical};
    } catch (error) {
        console.error('+page.server#load', '|', 'Google Calendar returned an error');
        console.error(error)
        return {weekEvents: [], ical, error: "We failed to fetch the events"};
    }

}


