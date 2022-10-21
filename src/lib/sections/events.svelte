<script>
    import Event from '$lib/components/event.svelte';
    import {fly} from 'svelte/transition';
    import Clipboard from "svelte-clipboard";
    import {addToast, ToastType} from '$lib/components/toast/store'

    export let events = [], ical = '';

    function copySuccessfully() {
        addToast({type: ToastType.Success, message: 'iCal link copied to clipboard'});
    }

    function downloadStarted() {
        addToast({type: ToastType.Success, message: 'Download started'});
    }
</script>

{#if events.length > 0}
    <section id="events" in:fly={{y: 100 ,duration: 250 , delay:500}} out:fly={{y: 100 ,duration: 250}}>
        <div class="py-8">
            <div class="container mx-auto flex flex-col items-start lg:flex-row my-12 md:my-24">
                <div class="flex flex-col w-full lg:sticky md:top-36 lg:w-1/3 mt-2 md:mt-12 px-8">
                    <p class="text-300 uppercase tracking-loose dark:text-gray-400">Upcoming Events</p>
                    <p class="text-3xl md:text-4xl leading-normal md:leading-relaxed mb-2">Don't miss out</p>
                    {#if ical.length > 0}
                        <p class="text-sm md:text-base text-50 mb-4 dark:text-gray-400">
                            Download our calendar to follow all the <span class="underline decoration-blue-500">current events</span> events we have planned. Alternatively, you can subscribe to stay up to date with <span class="underline decoration-blue-500">future events</span> as well, using your favourite calendar app.
                        </p>
                        <div class="flex">
                        <a href={ical} on:click={downloadStarted} class="shrink ml-auto mr-2 bg-transparent ml-auto hover:text-black text-black-300 text-center rounded shadow hover:shadow-lg py-2 px-4 border border-black-300 hover:border-black hover:bg-white">
                                Current events
                            </a>

                            <Clipboard
                                    text={ical}
                                    let:copy
                                    on:copy={copySuccessfully}>
                            <button on:click={copy} class="mr-auto ml-2 mr-auto hover:text-black hover:bg-white text-center rounded shadow hover:shadow-lg py-2 px-4 border border-black-300 hover:border-black">
                                    Future events
                                </button>
                            </Clipboard>
                        </div>
                    {/if}
<!--                    <hr class="my-8"/>-->
<!--                    <form name="suggestion" netlify>-->
<!--                        <p class="text-sm md:text-base text-50 mb-4">-->
<!--                            If you have any great ideas for events you would like to see, please let us know!-->
<!--                        </p>-->
<!--                        <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-1">-->
<!--                            <div>-->
<!--                                <label class="text-gray-700 dark:text-gray-200" for="suggestion">Suggestion</label>-->
<!--                                <input id="suggestion" type="text" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">-->

<!--                            </div>-->
<!--                        </div>-->

<!--                        <div class="flex justify-end mt-6">-->
<!--                            <button type="submit" class="px-8 py-2.5 cursor-pointer leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">-->
<!--                                Send it!-->
<!--                            </button>-->
<!--                        </div>-->
<!--                    </form>-->
                </div>
                <div class="ml-0 lg:ml-12 lg:w-2/3 w-full lg:sticky">
                    <div class="container mx-auto w-full h-full">
                        <div class="relative wrap p-10 h-full">
                            <div class="absolute right-1/2 h-full">
                                <div class="absolute h-full border dark:border-white border-gray-800 border-2 rounded-lg"></div>
                            </div>
                            {#each events as event, index}
                                <Event event={event} index={index}/>
                            {/each}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
{/if}
