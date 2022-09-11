export type CalendarEvent = {
    readonly kind: string;
    readonly etag: string;
    readonly id: string;
    readonly status: string;
    readonly htmlLink: string;
    readonly created: string;
    readonly updated?: string;
    readonly summary: string;
    readonly description?: string;
    readonly location?: string;
    readonly creator: { email: string, self: boolean };
    readonly organizer: { email: string, self: boolean };
    readonly start: { dateTime: string };
    readonly end?: { dateTime: string };
    readonly iCalUID?: string;
    readonly sequence?: number;
    readonly reminders?: { useDefault: boolean };
    readonly eventType?: string;
}
