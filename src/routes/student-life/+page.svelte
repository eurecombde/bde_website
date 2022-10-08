<script>
    import FAQ from '$lib/sections/faq.svelte';
    import Tips from '$lib/sections/tips.svelte';

    import {fade} from 'svelte/transition';
    import Places from '$lib/sections/places.svelte';
    // import {Info} from '$lib/components/alert.svelte';

    export let data;
    const {guides, error} = data;

</script>

<section in:fade out:fade>
    <div class="container px-6 py-10 mx-auto">
<!--        <Info>This page is under development</Info>-->

        <h1 class="text-2xl font-semibold text-gray-800 lg:text-4xl dark:text-white">Student Guides</h1>

        <div class="mt-8 xl:mt-16 lg:flex lg:-mx-6 lg:flex">
            <div class="lg:w-3/4 lg:px-6">
                <img class="object-cover object-center w-full h-80 xl:h-[28rem] rounded-xl" src="https://images.unsplash.com/photo-1624996379697-f01d168b1a52?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="">

                <div>
                    <p class="mt-6 text-sm text-blue-500 uppercase">Want to know</p>

                    <h1 class="max-w-lg mt-4 text-4xl font-semibold leading-tight text-gray-800 dark:text-white">
                        What do you want to know about UI
                        <!--                        <Markdown source={readme}/>-->
                    </h1>

                    <div class="flex items-center mt-6">
                        <img class="object-cover object-center w-10 h-10 rounded-full" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="">

                        <div class="mx-4">
                            <h1 class="text-sm text-gray-700 dark:text-gray-200">Amelia. Anderson</h1>
                            <p class="text-sm text-gray-500 dark:text-gray-400">Lead Developer</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="mt-8 lg:w-1/4 lg:mt-0 lg:px-6">
                <!--Guide list-->

                {#each guides as guideAndMeta}
                    <div>
                        <h3 class="text-blue-500 capitalize">{guideAndMeta.metadata.category}</h3>

                        <a href="/student-life/{guideAndMeta.guide.path}" class="block mt-2 font-medium text-gray-700 hover:underline hover:text-gray-500 dark:text-gray-400 ">
                            {guideAndMeta.metadata.title}
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
