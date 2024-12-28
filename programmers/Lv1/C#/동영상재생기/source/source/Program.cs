using System;

public class Solution
{
    public string solution(string video_len, string pos, string op_start, string op_end, string[] commands)
    {
        string answer = "";
        TimeSpan currentTime = TimeSpan.ParseExact(pos, @"mm\:ss", null);
        TimeSpan videoLenTime = TimeSpan.ParseExact(video_len, @"mm\:ss", null);
        TimeSpan opStartTime = TimeSpan.ParseExact(op_start, @"mm\:ss", null);
        TimeSpan opEndTime = TimeSpan.ParseExact(op_end, @"mm\:ss", null);


        foreach (string command in commands)
        {
            if (opStartTime <= currentTime && currentTime <= opEndTime)
            {
                currentTime = opEndTime;
            }
            if (command == "prev")
            {
                currentTime = currentTime - TimeSpan.FromSeconds(10);
                if (currentTime < TimeSpan.FromSeconds(10))
                {
                    currentTime = TimeSpan.Zero;
                }
            }
            else if (command == "next")
            {
                currentTime = currentTime + TimeSpan.FromSeconds(10);
                if (currentTime > videoLenTime - TimeSpan.FromSeconds(10))
                {
                    currentTime = videoLenTime;
                }
            }
            if (opStartTime <= currentTime && currentTime <= opEndTime)
            {
                currentTime = opEndTime;
            }
        }
        answer = currentTime.ToString(@"mm\:ss");
        return answer;
    }
}