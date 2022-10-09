<script>
    import FAQ from '$lib/sections/faq.svelte';
    import Tips from '$lib/sections/tips.svelte';

    import {fade} from 'svelte/transition';
    // import Places from '$lib/sections/places.svelte';
    import {guides} from '$lib/constants/student-guides';

    const activeGuide = guides[0];
    const otherGuides = guides.slice(1);

</script>

<section in:fade out:fade>
    <div class="container px-6 py-10 mx-auto">
        <!--        <Info>This page is under development</Info>-->

        <h1 class="text-2xl font-semibold text-gray-800 lg:text-4xl dark:text-white">Student Guides</h1>

        <!--Headline-->
        <div class="mt-8 xl:mt-16 lg:flex lg:-mx-6 lg:flex">
            <div class="lg:w-3/4 lg:px-6">
                {#if activeGuide.image}
                    <img class="object-cover object-center w-full h-80 xl:h-[28rem] rounded-xl" src={activeGuide.image} alt="">
                {:else}
                    <img class="object-cover object-center w-full h-80 xl:h-[28rem] rounded-xl" src="{activeGuide.image}" alt="">
                {/if}
                <div>
                    <p class="mt-6 text-sm text-blue-500 uppercase">{activeGuide.tags.join(", ")}</p>

                    <h1 class="max-w-lg mt-4 text-4xl font-semibold leading-tight text-gray-800 dark:text-white">
                        {activeGuide.name}
                    </h1>

                    <div class="flex items-center mt-6">
                        <div>
                            <h1 class="text-sm text-gray-700 dark:text-gray-200">Amelia. Anderson</h1>
                            <p class="text-sm text-gray-500 dark:text-gray-400">Lead Developer</p>
                        </div>
                    </div>
                </div>
            </div>

            <!--Guide list-->
            <div class="mt-8 lg:w-1/4 lg:mt-0 lg:px-6">
                {#each otherGuides as guide}
                    <div>
                        <h3 class="text-blue-500">{guide.tags.join(", ")}</h3>

                        <a href="/student-life/{guide.slug}" class="block mt-2 font-medium text-gray-700 hover:underline hover:text-gray-500 dark:text-gray-400 ">
                            {guide.name}
                        </a>
                    </div>

                    <hr class="my-6 border-gray-200 dark:border-gray-700">
                {/each}

            </div>
        </div>
    </div>
</section>

<Tips/>
<!--<Places/>-->

<FAQ/>
