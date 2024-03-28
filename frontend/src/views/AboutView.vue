<template>
  <UserLayout>
    <div class="breadcrumbs">
      <ul>
        <li>
          <RouterLink :to="{name: 'home'}">Home</RouterLink>
        </li>
        <li>About</li>
      </ul>
    </div>

    <div>
      <p class="my-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad asperiores at aut
        corporis cum, delectus deleniti deserunt dolore dolores dolorum eveniet impedit ipsam itaque iure maiores maxime
        nam neque nesciunt nihil odit quia sint soluta sunt ullam ut. Aliquid, aspernatur assumenda autem consequuntur
        cum dicta dolore eveniet excepturi facere harum iure laboriosam laborum nihil numquam odio quasi tenetur
        voluptatem voluptatibus?</p>
      <p class="my-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid architecto beatae
        doloremque excepturi facilis impedit iste, officia omnis optio pariatur quae quam, quos reiciendis sint soluta,
        sunt tempora ullam! Dignissimos molestiae nostrum praesentium provident sit. Dolorum incidunt officia quas
        veniam?</p>
      <p class="my-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab ea labore laudantium
        molestiae neque nisi sapiente, ullam unde voluptatum! Aperiam?</p>
    </div>
  </UserLayout>
</template>

<script setup>
import UserLayout from '@/components/layouts/UserLayout.vue'
import { RouterLink } from 'vue-router'
</script>