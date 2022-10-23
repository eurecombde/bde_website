<script>
  import Tooltip from "@fouita/tooltip";
  import { GOOGLE_MAPS_QUERY } from "$lib/constants/links";

  export let event;
  export let index;

  const align = index % 2 === 0 ? "left" : "right";
  const textAlign = index % 2 === 0 ? "text-right" : "text-left";

  const startDate = new Date(event.start.date ?? event.start.dateTime);
  const endDate = new Date(event.end.date ?? event.end.dateTime);
  const duration = endDate.getDate() - startDate.getDate();

  const dateRange = duration > 0 ? `${startDate.getDate()} - ${endDate.getDate()}` : startDate.getDate();
  const localeDate = `${dateRange} ${startDate.toLocaleDateString("en", { month: "short", year: "numeric" })}`;

  const preview = event.attachments && event?.attachments[0].mimeType == "image/jpeg" ? event?.attachments[0] : undefined; // todo: change to get the first image/png/jpeg/jpg
  const attachments = preview ? event.attachments.slice(1) : event.attachments; // todo: change to all except the preview
</script>

<style lang="scss">
    :global(.description a) {
        $blue: #2563eb;
        color: $blue;
        text-decoration: $blue underline ;
    }
</style>

<div class="mb-8 flex justify-between items-center w-full {align}-timeline" class:flex-row-reverse="{align==='left'}">
  <div class="order-1 w-5/12"></div>
  <div class="order-1 w-5/12 px-1 py-4 {textAlign} max-w-1/3">
    {#if preview}
    <div class="flex mb-2"
         class:justify-start="{align==='left'}"
         class:justify-end="{align==='left'}">
      <img class="w-full object-contain rounded-lg"
           src="https://drive.google.com/uc?export=view&id={preview.fileId}" />
    </div>
    {/if}


    <p class="mb-3 text-base text-300">{localeDate}</p>
    <h4 class=" font-bold text-lg md:text-2xl">{event.summary}</h4>
    {#if event.location}
    <a href="{GOOGLE_MAPS_QUERY}{event.location}">
      <p class="text-sm md:text-base leading-snug text-gray-500 hover:text-blue-500 mb-3 flex w-full {align}-timeline"
         class:flex-row-reverse={align === 'left'}>
      <span>@</span>
      <span class="mx-1">{event.location.split(',')[0]}</span>
      </p>

    </a>
    {/if}
    {#if event.description}
    <p class="text-sm md:text-base leading-snug overflw-wrap description"> <!--todo: style this-->
      {@html event.description}
    </p>
    {/if}

    {#if attachments}

    <div class="flex mt-2 flex-col"
         class:items-start={align === 'left'}
    class:items-end={align === 'left'}>
    {#each attachments as attachment}
    <a
      class="bg-red-900 mb-2 flex flex-row items-center px-4 py-2 font-medium tracking-wide text-white transition-colors duration-300 transform bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80"
      href="{attachment.fileUrl}">
      <img class="w-4 h-4 mr-2 rounded" src="{attachment.iconLink}/">
      <span class="mx-1 text-xs truncate">{attachment.title}</span>
    </a>
    {/each}
  </div>

  {/if}

</div>
</div>
