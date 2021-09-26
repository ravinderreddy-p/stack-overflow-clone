import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { WelcomeDataService } from '../service/data/welcome-data.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  name = ''
  messageFromService: string;

  constructor(
    private route: ActivatedRoute,
    private service: WelcomeDataService,
  ) { }

  ngOnInit(): void {
    this.name = this.route.snapshot.params['name'];
  }

  getWelcomeMessage(){
    // console.log(this.service.executeHelloWorldService());
    this.service.executeHelloWorldService().subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    );
  }

  handleSuccessfulResponse(response){
    this.messageFromService = response.message;
    console.log(response);
    console.log(response.message);
  }

  handleErrorResponse(error){
    this.messageFromService = error.error.message;
  }

}
