import React, { useState } from "react";
import 'antd/dist/antd.css';
import axios from 'axios';
import TimeList from './list'
import { List,Form, Button } from 'antd';
import { Input, Checkbox } from 'antd';
const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 8,
  },
};

const onFinish = (values) => {
  console.log('Success:', values);
};

const onFinishFailed = (errorInfo) => {
  console.log('Failed:', errorInfo);
};

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 8,
  },
};



class Header extends React.Component {

        constructor(props) {
          super(props);
          this.state = { query:'',timeline: []};
          this.handleClick = this.handleClick.bind(this);
          this.query = React.createRef()
        }
        handleClick() {
          this.makeRequest()
          this.render()
          // this.refreshQuery()
          //this.refreshList()
        }

        componentDidUpdate() {
          // this.listRef.current.setState({timeline:this.listRef.current.state.timeline})
          this.render()
        }


        // componentDidMount() {
        //   axios.get(`http://127.0.0.1:8080?text=do%20something%20next%20monday`)
        //     .then(
        //       res => {
        //           this.setState({ timeline:res.data });
        //     })
        // }

        componentDidMount() {
          axios.get(`http://127.0.0.1:8080/get`)
            .then(
              res => {
                  this.setState({ timeline:res.data });
            })
        }

        // refreshQuery(){
        //   console.log(this.listRef)
        //   this.setState({query:this.query.current.state.value})
        // }

        makeRequest(){
          const q = {'params':{'text':this.query.current.state.value}}
          axios.get(`http://127.0.0.1:8080`,q)
            .then(res => {
                  console.log(this.state.timeline)
                  this.setState({ timeline:res.data });
            })

        }

        render() {
          return (
                <div>
                        <Form
                              {...layout}
                              name="basic"
                              initialValues={{
                                remember: true,
                              }}
                              onFinish={onFinish}
                              onFinishFailed={onFinishFailed}
                            >
                              <Form.Item
                                label="Query"
                                name="query"
                                rules={[
                                  {
                                    required: true,
                                    message: 'You must specify a search item',
                                  },
                                ]}
                              >
                                <Input placeholder="do something saturday" ref={this.query}/>
                              </Form.Item>

                              <Form.Item {...tailLayout}>
                                <Button type="primary" htmlType="submit" onClick={this.handleClick}>
                                  Search
                                </Button>
                              </Form.Item>
                            </Form>
                            <List
                              itemLayout="vertical"
                              size="small"
                              dataSource={this.state.timeline}
                              renderItem={item => (
                                <List.Item key={item.date}>
                                  <div>
                                    {item.date}
                                  </div>
                                  <div>
                                    {item.day}
                                  </div>
                                  <div>
                                    {item.notes}
                                  </div>
                                </List.Item>

                              )}
                            />
                </div>
          );
        }
      }
export default Header