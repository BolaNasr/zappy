import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  tweet;
  constructor(private api: ApiService) {

    this.getAllTweets();
  }
  getAllTweets = () => {
    this.api.getAllTweets().subscribe(
      data => {
        this.tweet = data
      },
      error => {
        console.log(error);
      }
    )
  }
}
