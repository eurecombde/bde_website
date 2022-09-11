<script>
    import Events from '../sections/events.svelte';
    import Header from '../sections/header.svelte';

    /** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[] ,calendar: string, error: string}>>} */
    export let data;
    console.log(data)
    const {events, calendar, error} = data;
</script>


<Header/>
{calendar} <br>
{error} <br>
<Events events={events}/>
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
