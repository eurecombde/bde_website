<script>
    import {CALENDAR_ID} from '$env/static/private';
    import Events from '../sections/events.svelte';
    import Header from '../sections/header.svelte';

    /** @type {import('./$types').PageServerLoad} */
    export let data;
</script>


<Header/>
<Events events={Object.values(data)}/>
{CALENDAR_ID}
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
