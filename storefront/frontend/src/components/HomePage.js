import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import { Link } from "react-router-dom";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

// import Table from "@material-ui/core/Table";
// import TableBody from "@material-ui/core/TableBody";
// import TableCell from "@material-ui/core/TableCell";
// import TableContainer from "@material-ui/core/TableContainer";
// import TableHead from "@material-ui/core/TableHead";
// import TableRow from "@material-ui/core/TableRow";
// import Paper from "@material-ui/core/Paper";

import Table from "./SimpleTable"

const rows = [

];

export default class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchName: "",
      data: []
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSearchButtonPressed = this.handleSearchButtonPressed.bind(this);
  }
  handleChange(e){
    this.setState({
      searchName: e.target.value
    });
  }

  handleSearchButtonPressed(e){
    const requestOptions = {
      method: 'GET',
      headers: {'Content-Type': 'application/json'}
      
    };
    fetch('/api/get-courses/'+this.state.searchName, requestOptions).then(
      (response) => response.json()
    ).then((data) => {
      this.setState({
        data: data
      });
    });
  }

  render() {
    return (
      <Grid container spacing={1} align="center">
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            Course Recommendation
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="string"
              onChange={this.handleChange}
              defaultValue={this.state.searchName}
              inputProps={{
                style: { textAlign: "center" },
              }}
          />
            <br></br>
            <Button
              color="primary"
              variant="contained"
              onClick={this.handleSearchButtonPressed}
            >
              Search
            </Button>
            <FormHelperText>
              <div align="center">Search Course</div>
            </FormHelperText>
          </FormControl>
        </Grid>
        <Table
          data = {this.state.data}
          header = {[
            {
              name: "Course Title",
              prop: "course_title",
              ref: true,
              asc: false,
            },
            {
              name: "Price ($)",
              prop: "price",
              ref: false,
              asc: false,
            },
            {
              name: "Subscribers",
              prop: "num_subscribers",
              ref: false,
              asc: false,
            },
            {
              name: "Reviews",
              prop: "num_reviews",
              ref: false,
              asc: false,
            },
            {
              name: "Total Lectures",
              prop: "num_lectures",
              ref: false,
              asc: false,
            },
            {
              name: "Level",
              prop: "level",
              ref: false,
              asc: false,
            },
            {
              name: "Course Duration (in hours)",
              prop: "content_duration",
              ref: false,
              asc: false,
            },
            {
              name: "Subject",
              prop: "subject",
              ref: false,
              asc: false,
            }
          ]}
        />
      </Grid>
    );
  }
}
