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
            <a class="lg:w-3/4 lg:px-6" href="/student-life/{activeGuide.slug}">
                {#if activeGuide.image}
                    <img class="object-cover object-center w-full h-80 xl:h-[28rem] rounded-xl" src={activeGuide.image} alt={activeGuide.tags.join(', ')}>
                {:else}
                    <img class="object-cover object-center w-full h-80 xl:h-[28rem] rounded-xl" src="https://source.unsplash.com/1080x720/?{activeGuide.tags.join(',')}" alt={activeGuide.tags.join(', ')}>
                {/if}
                <div>
                    <p class="mt-6 text-sm text-blue-500 uppercase">{activeGuide.tags.join(", ")}</p>

                    <h1 class="max-w-lg mt-4 text-4xl font-semibold leading-tight text-gray-800 dark:text-white">
                        {activeGuide.name}
                    </h1>

                    <h1 class="text-sm text-gray-700 dark:text-gray-200">By {activeGuide.author}</h1>
                </div>
            </a>

            <!--Guide list-->
            <div class="mt-8 lg:w-1/4 lg:mt-0 lg:px-6">
                {#each otherGuides as guide}
                    <div>
                        <span class="text-blue-500 uppercase text-sm">{guide.tags.join(", ")}</span>
                        <a href="/student-life/{guide.slug}" class="block mt-2 font-medium text-gray-700 hover:underline hover:text-gray-500 dark:text-gray-400 ">
                            {guide.name}
                        </a>
                        <h1 class="mt-2 text-sm text-gray-700 dark:text-gray-200">By {activeGuide.author}</h1>
                    </div>



                    <hr class="my-6 border-gray-200 dark:border-gray-700">
                {/each}

            </div>
        </div>
    </div>
</section>

<!--Add remaining posts as a grid-->

<section class="bg-white dark:bg-gray-900">
    <div class="container px-6 py-10 mx-auto">
        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-3">
            <div>
                <img class="object-cover object-center w-full h-64 rounded-lg lg:h-80" src="https://images.unsplash.com/photo-1624996379697-f01d168b1a52?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="">

                <div class="mt-8">
                    <span class="text-blue-500 uppercase">category</span>

                    <h1 class="mt-4 text-xl font-semibold text-gray-800 dark:text-white">
                        What do you want to know about UI
                    </h1>

                    <p class="mt-2 text-gray-500 dark:text-gray-400">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam est asperiores vel, ab animi
                        recusandae nulla veritatis id tempore sapiente
                    </p>

                    <div class="flex items-center justify-between mt-4">
                        <div>
                            <a href="#" class="text-lg font-medium text-gray-700 dark:text-gray-300 hover:underline hover:text-gray-500">
                                John snow
                            </a>

                            <p class="text-sm text-gray-500 dark:text-gray-400">February 1, 2022</p>
                        </div>

                        <a href="#" class="inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
                    </div>

                </div>
            </div>

            <div>
                <img class="object-cover object-center w-full h-64 rounded-lg lg:h-80" src="https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="">

                <div class="mt-8">
                    <span class="text-blue-500 uppercase">category</span>

                    <h1 class="mt-4 text-xl font-semibold text-gray-800 dark:text-white">
                        All the features you want to know</h1>

                    <p class="mt-2 text-gray-500 dark:text-gray-400">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam est asperiores vel, ab animi
                        recusandae nulla veritatis id tempore sapiente
                    </p>

                    <div class="flex items-center justify-between mt-4">
                        <div>
                            <a href="#" class="text-lg font-medium text-gray-700 dark:text-gray-300 hover:underline hover:text-gray-500">
                                Arthur Melo
                            </a>

                            <p class="text-sm text-gray-500 dark:text-gray-400">February 6, 2022</p>
                        </div>

                        <a href="#" class="inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
                    </div>

                </div>
            </div>

            <div>
                <img class="object-cover object-center w-full h-64 rounded-lg lg:h-80" src="https://images.unsplash.com/photo-1597534458220-9fb4969f2df5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80" alt="">

                <div class="mt-8">
                    <span class="text-blue-500 uppercase">category</span>

                    <h1 class="mt-4 text-xl font-semibold text-gray-800 dark:text-white">
                        Which services you get from Meraki UI
                    </h1>

                    <p class="mt-2 text-gray-500 dark:text-gray-400">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam est asperiores vel, ab animi
                        recusandae nulla veritatis id tempore sapiente
                    </p>

                    <div class="flex items-center justify-between mt-4">
                        <div>
                            <a href="#" class="text-lg font-medium text-gray-700 dark:text-gray-300 hover:underline hover:text-gray-500">
                                Tom Hank
                            </a>

                            <p class="text-sm text-gray-500 dark:text-gray-400">February 19, 2022</p>
                        </div>

                        <a href="#" class="inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<Tips/>
<!--<Places/>-->

<FAQ/>
