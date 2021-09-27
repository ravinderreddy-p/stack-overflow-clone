import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuestionsDataService, Questions } from '../service/data/questions-data.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  public userName: string = ''
  public questions: Questions[];
  public responseStatus: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private service: QuestionsDataService,
  ) { }

  ngOnInit(): void {
    this.userName = sessionStorage.getItem('authenticatedUser');
    // this.getAllQuestions();
  }

  getAllQuestions(){
    this.service.callToGetAllQuestions().subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    );
  }

  handleSuccessfulResponse(response){
    this.responseStatus = response.success;
    this.questions = response.questions;
  }

  handleErrorResponse(error){
    this.responseStatus = error.error.message;
  }

}
