<script>
    import Header from '$lib/sections/header.svelte';
    import Events from '$lib/sections/events.svelte';

    /** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[] ,calendar: string, error: string}>>} */
    export let data;
    const {events, ical, error} = data;
</script>

{#if error}
    <div class="m-10 flex justify-center">
        <div class="lg:w-1/2 p-4 text-red-700 border rounded border-red-900/10 bg-red-50 justify-center flex" role="alert">
            <strong class="text-sm font-medium">❗️ {error} ❗️</strong>
        </div>
    </div>
{/if}

<Header/>
<Events events={events} ical={ical}/>
<!--<Places/>-->
<!--<Tips/>-->
<!--<Team/>-->
<!--Photos from events-->
<!--Student Life: Resources about studying at eurecom, -->
<!--Getting around: tips on living in the area, transport, etc-->
<!--About the BDE-->
<!--Contact -->
<!--3D model of the school-->
<!--Indoor map of the school-->


<!--
Todo:
1. Possibility for adding graphics? Attachments!?
2. Link to location
3. What if location or description is undefined?
4. Add a link to the calendar iCal
5. Google Analytics
-->
