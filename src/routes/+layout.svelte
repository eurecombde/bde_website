<script>
    const ACTIVE_ROUTE_STYLE = "text-gray-800 dark:text-gray-200 border-b-2 border-blue-500 mx-1.5 sm:mx-6";
    const INACTIVE_ROUTE_STYLE = "border-b-2 border-transparent hover:text-gray-800 dark:hover:text-gray-200 hover:border-blue-500 mx-1.5 sm:mx-6";

    import "../app.css";
    import {page} from '$app/stores';
    import Icon from 'svelte-awesome';
    import {facebookSquare, instagram} from 'svelte-awesome/icons';
    import {routes} from '$lib/constants/routes';
    import {contact} from '$lib/constants/team';
    import {fly, fade} from 'svelte/transition';
    import Toast from '$lib/components/toast/toast.svelte'
    import {dismissToast, toasts} from '$lib/components/toast/store'


    $: activePath = $page.url.pathname;
    $: activeRoute = routes.find((route) => route.path === activePath);
    $: title = activeRoute ? `BDE | ${activeRoute.name} ${activeRoute.emoji ?? ''}` : contact.brand;
</script>

<style lang="postcss">
    section#toasts {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        display: flex;
        margin-top: 1rem;
        justify-content: center;
        flex-direction: column;
        z-index: 1000;
    }
</style>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<nav in:fly={{y: 100 ,duration: 250}}>
    <div class="container p-6 mx-auto">
        <div class="flex flex-col justify-between items-center text-2xl font-bold text-center text-gray-800 dark:text-white lg:text-3xl">
            <div class="flex flex-row">
                <a class="px-2" href="/about">
                    <img class="p-2 h-[5rem] rounded-lg bg-white object-contain" src="images/BDE_official@small.jpg" alt="EURECOM BDE logo">
                </a>
                <a class="px-2 " href="https://eurecom.fr">
                    <img class="p-2 h-[5rem] rounded-lg bg-white object-contain" src="/images/logo_black.png" alt="EURECOM logo"/>
                </a>
            </div>
            <a class="hover:text-gray-700 dark:hover:text-gray-300 mt-2 " href="/"><span class="text-blue-400">{contact.brand}</span> Student Union</a>
        </div>
        <div class="flex items-center justify-center mt-6 text-gray-600 capitalize dark:text-gray-300">
            {#each routes as route}
                <a class="{route.path === activePath ? ACTIVE_ROUTE_STYLE : INACTIVE_ROUTE_STYLE}" href={route.path}>{route.name}</a>
            {/each}

            {#each contact.socials as social}
                <a href={social.url} class="border-b-2 border-transparent hover:text-gray-800 dark:hover:text-gray-200 hover:border-blue-500 mx-1.5 sm:mx-6">
                    <Icon data={social.icon}/>
                </a>
            {/each}
        </div>
    </div>
</nav>

{#if $toasts}
    <section id="toasts">
        {#each $toasts as toast (toast.id)}
            <Toast
                    type={toast.type}
                    dismissible={toast.dismissible}
                    on:dismiss={() => dismissToast(toast.id)}>
                {toast.message}
            </Toast>
        {/each}
    </section>
{/if}

<slot/>

<footer>
    <div class="container p-6 mx-auto">
        <div class="lg:flex">
            <div class="w-full -mx-6 lg:w-2/5">
                <div class="px-6">
                    <div>
                        <a href="/" class="text-xl font-bold text-gray-800 dark:text-white hover:text-gray-700 dark:hover:text-gray-300">{contact.brand}</a>
                    </div>

                    <p class="max-w-sm mt-2 text-gray-500 dark:text-gray-400">{contact.tagline}</p>

                    <div class="flex mt-6 -mx-2">
                        {#each contact.socials as social}
                            <a href={social.url}
                               class="mx-2 text-gray-600 transition-colors duration-300 dark:text-gray-300 hover:text-blue-500 dark:hover:text-blue-400"
                               aria-label={social.name}>
                                <Icon data={social.icon}/>
                            </a>
                        {/each}
                    </div>
                </div>
            </div>

            <div class="mt-6 lg:mt-0 lg:flex-1">
                <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
                    {#each routes as route}
                        <div>
                            <a href={route.path}><h3 class="text-gray-700 uppercase dark:text-white">{route.name}</h3></a>
                            {#if route.sections}
                                {#each route.sections as section}
                                    <a href={route.path + section.tag} class="block mt-2 text-sm text-gray-600 dark:text-gray-400 hover:underline">{section.name}</a>
                                {/each}
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <hr class="h-px my-6 bg-gray-200 border-none dark:bg-gray-700">

        <div>
            <p class="text-center text-gray-500 dark:text-gray-400">© EURECOM BDE 2022 - All rights reserved</p>
        </div>
    </div>
</footer>
