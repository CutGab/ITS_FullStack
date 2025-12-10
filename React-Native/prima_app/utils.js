import { Animated } from 'react-native';

export function fadeInFromBelow(animatedValue, translateValue, duration = 800) {
  Animated.parallel([
    Animated.timing(animatedValue, {
      toValue: 1,
      duration,
      useNativeDriver: true,
    }),
    Animated.timing(translateValue, {
      toValue: 0,
      duration,
      useNativeDriver: true,
    }),
  ]).start();
}