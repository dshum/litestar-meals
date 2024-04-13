<script setup>
import { ref, computed, reactive } from 'vue'
import {
  Combobox,
  ComboboxInput,
  ComboboxButton,
  ComboboxOptions,
  ComboboxOption,
  TransitionRoot
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'
import { Field } from 'vee-validate'

defineOptions({
  inheritAttrs: false
})

const props = defineProps({
  name: String,
  suggestions: Array
})
const selected = ref(props.suggestions[0])
const query = ref('')
const filteredSuggestions = computed(() =>
  query.value === ''
    ? props.suggestions
    : props.suggestions.filter((suggestion) =>
      suggestion.label
        .toLowerCase()
        .replace(/\s+/g, '')
        .includes(query.value.toLowerCase().replace(/\s+/g, ''))
    )
)
</script>

<template>
  <Combobox v-model="selected">
    <div class="relative">
      <div
        class="flex flex-row items-center input input-bordered"
      >
        <ComboboxInput
          class="w-full"
          :displayValue="(suggestion) => suggestion.label"
        >
          <Field
            :name="name"
            v-bind="$attrs"
            class="w-full pr-4 bg-red-100"
            @change="query = $event.target.value"
          />
        </ComboboxInput>
        <ComboboxButton
          class="absolute inset-y-0 right-0 flex items-center pr-2"
        >
          <ChevronUpDownIcon
            class="h-5 w-5 text-gray-400"
            aria-hidden="true"
          />
        </ComboboxButton>
      </div>
      <TransitionRoot
        leave="transition ease-in duration-100"
        leaveFrom="opacity-100"
        leaveTo="opacity-0"
        @after-leave="query = ''"
      >
        <ComboboxOptions
          v-if="filteredSuggestions.length > 0"
          class="absolute z-[1] mt-1 max-h-60 w-full overflow-auto rounded-xl bg-white py-1 text-base shadow-xl"
        >
          <ul class="menu">
            <li
              v-if="filteredSuggestions.length === 0 && query !== ''"
              class="menu-title"
            >
              Nothing found.
            </li>

            <ComboboxOption
              v-for="suggestion in filteredSuggestions"
              as="template"
              :key="suggestion.value"
              :value="suggestion"
              v-slot="{ selected, active }"
            >
              <li
                class=""
                :class="{
                  'bg-gray-200 rounded-lg': active,
                  '': !active,
                }"
              >
                <span
                  class="block truncate"
                  :class="{ 'font-medium': selected, 'font-normal': !selected }"
                >
                  {{ suggestion.label }}
                </span>
              </li>
            </ComboboxOption>
          </ul>
        </ComboboxOptions>
      </TransitionRoot>
    </div>
  </Combobox>
</template>
