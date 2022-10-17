export type CalendarDate = { date?: string, dateTime?: string, timeZone?: string };

export function asDate(calendarDate: CalendarDate) {
    return new Date(calendarDate?.date ?? calendarDate?.dateTime ?? "");
}

export function asDateTime(calendarDate: CalendarDate) {
    return new Date(calendarDate?.dateTime ?? "");
}


export type CalendarEvent = {
    readonly kind: string;
    readonly etag: string;
    readonly id: string;
    readonly status: string;
    readonly htmlLink: string;
    readonly created: string;
    readonly updated: string;
    readonly summary: string;
    readonly description?: string;
    readonly location?: string;
    readonly creator: { email: string, self: boolean };
    readonly organizer: { email: string, self: boolean };
    readonly start: CalendarDate;
    readonly end: CalendarDate;
    readonly iCalUID: string;
    readonly sequence: number;
    readonly reminders: { useDefault: boolean };
    readonly eventType: string;
}
