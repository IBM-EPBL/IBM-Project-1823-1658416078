<template>
<v-container fill-height fluid  class="w-100 p-4 d-flex align-items-center justify-content-center"
    style="height: 550px;">
  <v-row class="d-flex justify-center mb-6" >
      <v-col
            cols="12"
            sm="6"
            md="3"
          >
            <v-col>
              <v-text-field
              label="Type or paste your URL here...."
              rounded
              filled
              class = "searchBar"
              background-color="black"
              v-model = "searchBar"
            ></v-text-field>
            <div class="d-flex justify-center mb-6">
              <v-btn
                  rounded
                  color="green"
                  dark
                  @click="searchURL(searchBar)"
                >
                  Search
                </v-btn>
            </div>
          </v-col> 
          </v-col>
  </v-row>
  <v-row v-if="responseCard">
    <v-col  class="d-flex justify-center mb-6">
      <v-card
      class="mx-auto"
      max-width="344"
    >
      <v-card-title>
        Response
      </v-card-title>
          <v-card-text>
            URL : {{this.response}}
           </v-card-text>
           <v-card-text>
            Status : data
           </v-card-text>
    </v-card>
    </v-col>
  </v-row>
  <v-row style = "display: none;">

  </v-row>
</v-container>

</template>

<script>
import axios from "axios"
  export default {
    name: 'SearchBar',

    data: () => ({
      searchBar : "",
      responseCard : false,
      response : {}
    }),

    mounted : async function () {
    this.instance =  axios.create({ baseURL: "http://192.168.1.8:5000" })
    },

    methods:{
      async searchURL(searchBar){
        console.log(searchBar);
        const data = await this.instance.post("/ypredict",{data : {searchBar}})
        this.searchBar = ""
        this.responseCard = true
        return this.response = data
      }
    }
  }
</script>
