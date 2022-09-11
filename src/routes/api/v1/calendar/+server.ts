import {CALENDAR_ID, SCOPES, SERVICE_ACCOUNT_EMAIL, SERVICE_ACCOUNT_PRIVATE_KEY} from '$env/static/private';
import {auth as Auth, calendar as Calendar} from "@googleapis/calendar";
import type {CalendarEvent} from "../../../../types/calendar-event";
import {json} from "@sveltejs/kit";

/** @type {import('./$types').RequestHandler} */
export async function GET() {
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

        if (!events.data.items) return json({events: [], calendar: CALENDAR_ID + ', ' + SCOPES + ', ' + SERVICE_ACCOUNT_EMAIL + ', ' + SERVICE_ACCOUNT_PRIVATE_KEY, error: 'no items found'});
        return json({events: events.data.items.map((event: any) => event as CalendarEvent), calendar: CALENDAR_ID + ', ' + SCOPES + ', ' + SERVICE_ACCOUNT_EMAIL + ', ' + SERVICE_ACCOUNT_PRIVATE_KEY, error: ''});
    } catch (err) {
        console.error('Google Calendar returned an error: ' + err);
        return json({events: [], calendar: CALENDAR_ID + ', ' + SCOPES + ', ' + SERVICE_ACCOUNT_EMAIL + ', ' + SERVICE_ACCOUNT_PRIVATE_KEY, error: 'Google Calendar returned an error: ' + err}); // todo: +error.svelte & throw error(500,'fubar')
    }


    // return new Response(String("Hello world!"));
}