<script>
    import Event from './event.svelte';

    export let events;
</script>


<section>
    <div class="py-8">
        <div class="container mx-auto flex flex-col items-start md:flex-row my-12 md:my-24">
            <div class="flex flex-col w-full sticky md:top-36 lg:w-1/3 mt-2 md:mt-12 px-8">
                <p class="ml-2 text-300 uppercase tracking-loose">Upcoming Events</p>
                <!--                <p class="ml-2 text-yellow-300 uppercase tracking-loose">Working Process</p>-->
                <p class="text-3xl md:text-4xl leading-normal md:leading-relaxed mb-2">We are organising</p>
                <p class="text-sm md:text-base text-50 mb-4">
                    <!--                <p class="text-sm md:text-base text-gray-50 mb-4">-->
                    Here are the upcoming events we are organising.
                </p>
                <a href="/ical" class="bg-transparent mr-auto text-black-300 hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-black-300 hover:border-black hover:bg-black">
                    <!--                <a href="/ical" class="bg-transparent mr-auto hover:bg-yellow-300 text-yellow-300 hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-yellow-300 hover:border-transparent">-->
                    Keep me up to date
                </a>
            </div>
            <div class="ml-0 md:ml-12 lg:w-2/3 sticky">
                <div class="container mx-auto w-full h-full">
                    <div class="relative wrap overflow-hidden p-10 h-full">
                        <!--                        <div class="border-2-2 border-yellow-555 absolute h-full border" style="right: 50%; border: 2px solid #FFC100; border-radius: 1%;"></div>-->
                        <!--                        <div class="border-2-2 border-yellow-555 absolute h-full border" style="left: 50%; border: 2px solid #FFC100; border-radius: 1%;"></div>-->
                        <div class="border-2-2 border-yellow-555 absolute h-full border" style="right: 50%; border: 2px solid #333; border-radius: 1%;"></div>
                        <div class="border-2-2 border-yellow-555 absolute h-full border" style="left: 50%; border: 2px solid #333; border-radius: 1%;"></div>

                        {#each events as event, index}
                            <Event event={event} index={index}/>
                        {/each}
                    </div>
                    <img class="mx-auto -mt-36 md:-mt-36" src="https://user-images.githubusercontent.com/54521023/116968861-ef21a000-acd2-11eb-95ac-a34b5b490265.png"/>
                </div>
            </div>
        </div>
    </div>
</section>
