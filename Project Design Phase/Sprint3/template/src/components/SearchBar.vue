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
  <v-row v-if="responseCard === true">
    <v-col  class="d-flex justify-center mb-6">
      <v-card
      class="mx-auto"
      max-width="344"
    >
      <v-card-title>
        Response
      </v-card-title>
          <v-card-text style = "font-size: medium">
            <b>URL :</b><v-card-text style = "font-size: medium" v-bind:style="{'color': response['status']}">
                      {{this.response.url}}
                  </v-card-text>
           </v-card-text>
           <v-card-text style = "font-size: medium">
            <b>Status :</b><v-card-text style = "font-size: medium" v-bind:style="{'color': response['status']}">
                        {{this.response.prediction}}
                     </v-card-text>
           </v-card-text>
    </v-card>
    </v-col>
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
      response : {
        url : "",
        prediction : "",
        status : "",
      }
    }),

    mounted : async function () {
    this.instance =  axios.create({ baseURL: "http://192.168.1.2:5000" , headers:{'Content-type' : "application/json",}})
    },

    methods:{
      async searchURL(searchBar){
        const data = await this.instance.post("/ypredict",{URL : searchBar}).then((res)=> res.data)
        this.searchBar = ""
        this.responseCard = true
        this.response.url = data['url'],
        this.response.prediction = data['pred']
        this.response.status = data['status']
        
      }
    }
  }
</script>

