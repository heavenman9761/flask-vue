<template>
    <div class>
        <b-form inline>
        <label class="sr-only" for="inline-form-startDate">시작일자</label>
        <b-form-input id="inline-form-startDate" class="mb-2 mr-sm-2 mb-sm-0" placeholder="2020-01-10" v-model="startDate"></b-form-input>

        <label class="sr-only" for="inline-form-endDate">종료일자</label>
        <b-form-input id="inline-form-endDate" placeholder="2021-12-20" v-model="endDate"></b-form-input>

        <b-button variant="primary" @click="getDatas()">조회1</b-button>
    </b-form>
        
    </div>
</template>

<script>
export default {
    data() {
        return {
            startDate: '',
            endDate: '',
        };
    },
    methods: {

    }
}
</script>