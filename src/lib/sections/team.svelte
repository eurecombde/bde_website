<script>
    const AVATAR_FALLBACK_URL = "https://ui-avatars.com/api/?font-size=0.2&name=";
    import {fade, fly} from 'svelte/transition';
    import Icon from 'svelte-awesome';
    import {team} from '$lib/constants/team.ts';

</script>

<section id="team" in:fly={{y: 100 ,duration: 250, delay:250}} out:fly={{y: 100 ,duration: 250}}>
    <div class="container px-6 py-10 mx-auto">
        <div class="xl:flex xl:items-center xL:-mx-4">
        </div>
        <div class="grid gap-8 mt-8 xl:mt-16 xl:grid-cols-5 grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
            <div class="col-span-2 xl:mx-4 my-16">
                <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl dark:text-white">The <span class="underline decoration-blue-500">Team</span></h1>
                <p class="max-w-2xl mt-4 text-gray-500 dark:text-gray-300">
                    We are all here doing our best to help make our student life the best we can. If there is something you are wondering about, feel free to ask here or any of our members 😊
                </p>
            </div>

            {#each team as member, index}
                <div class="flex flex-col items-center" in:fly={{ y: 100, duration: 250, delay: 250+ index * 100}} >
                    <img class="object-cover w-full rounded-xl aspect-square" src={member.photo ?? AVATAR_FALLBACK_URL+member.name.replaceAll(" ","+")} alt={member.name}>
                    <h1 class="mt-4 text-2xl font-semibold text-gray-700 capitalize dark:text-white text-center">{member.name}</h1>
                    <p class="mt-2 text-gray-500 capitalize dark:text-gray-300">{member.role}</p>

                    <div class="flex mt-3 -mx-2">
                        {#each member.socials as social}
                            <a href={social.link} class="mx-2 text-gray-600 transition-colors duration-300 dark:text-gray-300 hover:text-blue-500 dark:hover:text-blue-400" aria-label={social.name}>
                                {#if social.icon}
                                    <Icon data={social.icon}/>
                                {:else}
                                    {social.name}
                                {/if}
                            </a>
                        {/each}
                    </div>
                </div>
            {/each}
        </div>
    </div>
</section>
