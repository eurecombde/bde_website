<script>
    import {GOOGLE_MAPS_QUERY} from '$lib/constants/links';

    export let event;
    export let index;

    const align = index % 2 === 0 ? 'left' : 'right';
    const textAlign = index % 2 === 0 ? 'text-right' : 'text-left';

    const startDate = new Date(event.start.date ?? event.start.dateTime);
    const endDate = new Date(event.end.date ?? event.end.dateTime);
    const duration = endDate.getDate() - startDate.getDate();

    const dateRange = duration > 0 ? `${startDate.getDate()} - ${endDate.getDate()}` : startDate.getDate();
    const localeDate = `${dateRange} ${startDate.toLocaleDateString('en', {month: 'short', year: 'numeric'})}`;
</script>

<div class="mb-8 flex justify-between items-center w-full {align}-timeline" class:flex-row-reverse={align==='left'}>
    <div class="order-1 w-5/12"></div>
    <div class="order-1 w-5/12 px-1 py-4 {textAlign}">
        <p class="mb-3 text-base text-300">{localeDate}</p>
        <h4 class=" font-bold text-lg md:text-2xl">{event.summary}</h4>
        {#if event.location}
            <a href="{GOOGLE_MAPS_QUERY}{event.location}">
                <p class="text-sm md:text-base leading-snug text-gray-500 hover:text-blue-500 mb-3 flex w-full {align} -timeline" class:flex-row-reverse={align === 'left'}>
                    <span>@</span>
                    <span class="mx-1">{event.location.split(',')[0]}</span>
                </p>

            </a>
        {/if}
        {#if event.description}
            <p class="text-sm md:text-base leading-snug"> <!--todo: style this-->
                {event.description}
            </p>
        {/if}
    </div>
</div>
