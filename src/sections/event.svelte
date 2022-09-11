<script>
    export let event;
    export let index;

    const align = index % 2 === 0 ? 'left' : 'right';
    const alignInverse = index % 2 === 0 ? 'right' : 'left';
</script>

<div class="mb-8 flex justify-between items-center w-full {align}-timeline" class:flex-row-reverse={align==='left'}>
    <div class="order-1 w-5/12"></div>
    <div class="order-1 w-5/12 px-1 py-4 text-{alignInverse}">
        {#if event.start.date}
            <p class="mb-3 text-base text-300">{event.start.date}</p> <!--todo: style this (1-6 May, 2021)-->
        {:else if event.start.dateTime}
            <p class="mb-3 text-base text-300">{event.start.dateTime}</p> <!--todo: style this (1-6 May, 2021)-->
        {/if}

        <h4 class="mb-3 font-bold text-lg md:text-2xl">{event.summary}</h4>
        {#if event.location}
            <p class="text-sm md:text-base leading-snug text-gray-50 text-opacity-100"> <!--todo: style this-->
                {event.location}
            </p>
        {/if}
        {#if event.description}
            <p class="text-sm md:text-base leading-snug text-gray-50 text-opacity-100"> <!--todo: style this-->
                {event.description}
            </p>
        {/if}
    </div>
</div>
