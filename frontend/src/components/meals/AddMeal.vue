<script setup>
import { ref } from 'vue'
import { Form } from 'vee-validate'
import InputField from '@/components/forms/InputField.vue'

const activeTab = ref(0)
</script>

<template>
  <div class="card shadow-2xl shadow-purple-200 bg-base-100">
    <div class="card-body">
      <div role="tablist" class="tabs tabs-bordered mb-2">
        <span role="tab" class="tab"
              :class="{'tab-active': activeTab === 0}"
              @click="activeTab = 0"
        >Choose meal</span>

        <span role="tab" class="tab"
              :class="{'tab-active': activeTab === 1}"
              @click="activeTab = 1"
        >Add new meal</span>
      </div>

      <div v-if="activeTab === 0">
        <Form @submit="">
          <div class="form-control">
            <InputField type="text" name="meal" label="Meal"
                        placeholder="Choose a meal" />
          </div>

          <div class="form-control">
            <InputField type="number" name="weight" label="Weight" min="0"
                        placeholder="Weight in grams" />
          </div>

          <div class="form-control mt-4">
            <button class="btn btn-primary max-w-xs">
              <span>Add meal</span>
            </button>
          </div>
        </Form>
      </div>

      <div v-if="activeTab === 1">
        <Form @submit="">
          <div class="form-control">
            <InputField type="text" name="meal" label="Meal"
                        placeholder="Meal name" />
          </div>

          <div class="form-control">

          </div>

          <div class="form-control">

          </div>

          <div class="form-control">
            <InputField type="number" name="weight" label="Weight" min="0"
                        placeholder="Weight in grams" />
          </div>

          <div class="form-control mt-4">
            <button class="btn btn-primary max-w-xs">
              <span>Add meal</span>
            </button>
          </div>
        </Form>
      </div>
    </div>
  </div>
</template>