<script>
    import Header from '$lib/sections/header.svelte';
    import Events from '$lib/sections/events.svelte';
    import {addToast, ToastType} from '$lib/components/toast/store'
    import Meta from '$lib/components/meta/meta.svelte';
    import {metaOf} from '$lib/components/meta/meta';

    const meta = metaOf({
        title: "Home", 
        image: {url:"/images/hero3.jpg", alt:"Students of EURECOM"}, 
        description: "See what the BDE is up to and what events we are organising."
    });

    /** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[] ,calendar: string, error: string}>>} */
    export let data;
    const {events, ical, error} = data;

    if (error) {
        addToast({type: ToastType.ERROR, message: error});
    }
</script>

<Meta {meta} /> 
<Header events={events}/>
<Events events={events} ical={ical}/>

<!--Photos from events-->
<!--Student Life: Resources about studying at eurecom, -->
<!--Getting around: tips on living in the area, transport, etc-->
<!--About the BDE-->
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
