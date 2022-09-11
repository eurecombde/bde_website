<script>
    export let event, index;

    const align = index % 2 === 0 ? 'left' : 'right';
    const alignInverse = index % 2 === 1 ? 'left' : 'right';
</script>

<div class="mb-8 flex justify-between items-center w-full {align}-timeline" class:flex-row-reverse={align==='left'}>
    <div class="order-1 w-5/12"></div>
    <div class="order-1 w-5/12 px-1 py-4 text-{alignInverse}">
        <p class="mb-3 text-base text-300">1-6 May, 2021</p>
        <h4 class="mb-3 font-bold text-lg md:text-2xl">{event.summary}</h4>
        {#if event.location}
            <p class="text-sm md:text-base leading-snug text-gray-50 text-opacity-100"> <!--todo: style this-->
                {event.location}
            </p>
        {/if}
        {#if event.description}
            <p class="text-sm md:text-base leading-snug text-gray-50 text-opacity-100">
                {event.description}
            </p>
        {/if}
    </div>
</div>
