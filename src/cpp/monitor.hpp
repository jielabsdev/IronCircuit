#pragma once
#include <iostream>

namespace ironcircuit {
    struct Policy {
        double max_tokens;
        bool fail_closed;
        Policy(double mt, bool fc) : max_tokens(mt), fail_closed(fc) {}
    };

    class Monitor {
    private:
        Policy policy_;
        double current_usage_;
    public:
        Monitor(Policy p, double initial_usage = 0.0) : policy_(p), current_usage_(initial_usage) {}
        bool check_usage(double cost) {
            if (current_usage_ + cost > policy_.max_tokens) return false;
            current_usage_ += cost;
            return true;
        }
        double get_usage() const { return current_usage_; }
    };
}
