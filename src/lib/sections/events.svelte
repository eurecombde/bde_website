<script>
    import Event from '$lib/components/event.svelte';

    export let events, ical;

    console.log('events',events, ical);
</script>


<section id="events">
    <div class="py-8">
        <div class="container mx-auto flex flex-col items-start md:flex-row my-12 md:my-24">
            <div class="flex flex-col w-full sticky md:top-36 lg:w-1/3 mt-2 md:mt-12 px-8">
                <p class=" text-300 uppercase tracking-loose">Upcoming Events</p>
                <p class="text-3xl md:text-4xl leading-normal md:leading-relaxed mb-2">Don't miss out</p>
                <p class="text-sm md:text-base text-50 mb-4">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nunc ut
                    aliquam tincidunt, nisl elit fermentum massa, nec luctus nunc ante ut dui.
                </p>
                <a href={ical} class="bg-transparent mr-auto text-black-300 hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-black-300 hover:border-black hover:bg-black">
                    Keep me up to date
                </a>
                <hr class="my-8"/>
                <form>
                    <p class="text-sm md:text-base text-50 mb-4">
                        If you have any great ideas for events you would like to see, please let us know!
                    </p>
                    <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-1">
                        <div>
                            <label class="text-gray-700 dark:text-gray-200" for="suggestion">Suggestion</label>
                            <input id="suggestion" type="text" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                        </div>
                    </div>

                    <div class="flex justify-end mt-6">
                        <button class="px-8 py-2.5 leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">Send it!</button>
                    </div>
                </form>
            </div>
            <div class="ml-0 md:ml-12 lg:w-2/3 sticky">
                <div class="container mx-auto w-full h-full">
                    <div class="relative wrap overflow-hidden p-10 h-full">
                        <div class="border-2-2 border-yellow-555 absolute h-full border" style="right: 50%; border: 2px solid #333; border-radius: 1%;"></div>
                        <div class="border-2-2 border-yellow-555 absolute h-full border" style="left: 50%; border: 2px solid #333; border-radius: 1%;"></div>

                        {#each events as event, index}
                            <Event event={event} index={index}/>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
