// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <chrono>
#include <memory>
#include <fstream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

#include "rclcpp/clock.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class Client : public rclcpp::Node
{
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
  size_t count_;
  const size_t NUM_MESSAGES = 1500;
  size_t message_size_ = 0;

  rclcpp::Clock *clk_;
  rcl_time_point_value_t start_ns_;

  public:
    Client()
    : Node("client"), count_(0)
    {
      publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);

      subscription_ = this->create_subscription<std_msgs::msg::String>(
        "echo", 10, std::bind(&Client::topic_callback, this, _1));

      timer_ = this->create_wall_timer(
        10ms, std::bind(&Client::timer_callback, this));

      clk_ = new rclcpp::Clock();
    }

  private:
    void timer_callback()
    {
      auto message = std_msgs::msg::String();
      message_size_ = message_size_ + 1000;
      count_++;
      std::string message_string(message_size_, '*');
      message.data = message_string;

      RCLCPP_INFO(this->get_logger(), "Publishing message number: '%d'", count_);

      rclcpp::Time time = clk_->now();
      start_ns_ = time.nanoseconds();

      publisher_->publish(message);

      if(count_ >= NUM_MESSAGES)
        this->timer_->cancel();
    }

  void topic_callback(const std_msgs::msg::String::SharedPtr) const
  {
    RCLCPP_INFO(this->get_logger(), "Response: received!");

    rcl_time_point_value_t end_ns = clk_->now().nanoseconds();
    RCLCPP_INFO(this->get_logger(), "[__TIME__]: %lld", end_ns - start_ns_);

    std::ofstream file;
    file.open("time.txt", std::ios_base::app);
    file << std::to_string(message_size_) << " " << std::to_string(end_ns - start_ns_) << "\n"; 
    file.close();
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Client>());
  rclcpp::shutdown();
  return 0;
}
