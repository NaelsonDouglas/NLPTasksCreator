import React, { useState } from "react";
import 'antd/dist/antd.css';
import axios from 'axios';
import { PageHeader,Form, Button } from 'antd';
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
          this.state = { query:''};
          this.handleClick = this.handleClick.bind(this);
          this.query = React.createRef()
        }
        handleClick() {
          this.makeRequest()
          this.refreshQuery()
        }

        refreshQuery(){
          this.setState({query:this.query.current.state.value})
        }

        makeRequest(){
          const q = {'params':{'text':this.query.current.state.value}}
          axios.get(`http://127.0.0.1:8080`,q)
            .then(res => {
                  //const res = res.data;
                  this.setState({ timeline:res.data });
            })
            console.log('this.state.timeline')
            console.log(this.state.timeline)
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
                </div>
          );
        }
      }
export default Header