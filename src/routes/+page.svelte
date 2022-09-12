<script>
    import Header from '$lib/sections/header.svelte';
    import Events from '$lib/sections/events.svelte';
    import Places from '$lib/sections/places.svelte';
    import FAQ from '$lib/sections/faq.svelte';

    /** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[] ,calendar: string, error: string}>>} */
    export let data;
    const {events, ical, error} = data;
    console.log('page', events, ical);
</script>


<Header/>
<Events events={events} ical={ical}/>
<Places/>
<!--<Tips/>-->
<FAQ/>
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
