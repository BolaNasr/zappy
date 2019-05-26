import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  base_url = "http://localhost:8000/"
  HttpHeaders = new HttpHeaders({ 'Content-type': 'application/json' })

  constructor(private http: HttpClient) { }
  getAllTweets(): Observable<any> {
    return this.http.get(this.base_url + "tweets/", { headers: this.HttpHeaders })
  }
}
