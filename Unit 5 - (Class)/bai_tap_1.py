# Tạo class video


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link


def read_video():  # Hàm đọc 1 video
    title = input("Mời bạn nhập title: ")
    link = input("Mời bạn nhập link: ")
    video = Video(title, link)
    return video


def print_video(video):  # Hàm in 1 video
    print("Video tile: " + video.title)
    print("Video link: " + video.link)


def read_videos():  # Hàm đọc nhiều video
    videos = []
    total_video = int(input("Bạn có mấy video: "))
    for i in range(total_video):
        print("video thứ", i + 1)
        vid = read_video()
        videos.append(vid)
    return videos


def print_videos(videos):  # Hàm in nhiều video
    for i in range(len(videos)):
        print_video(videos[i])


def write(videos):  # Ghi file vào text
    total = len(videos)
    with open("data.txt", "w") as file:
        file.write(str(total) + "\n")
        for i in range(total):
            write_video_txt(videos[i], file)


def write_video_txt(video, file):
    file.write(video.title + "\n")
    file.write(video.link + "\n")


def read_video_txt():
    videos = []
    with open("data.txt", "r") as file:
        total = file.readline()
        for i in range(int(total)):
            title = file.readline()
            link = file.readline()
            video = Video(title, link)
            videos.append(video)
    return videos


def main():  # Hàm main
    videos = read_videos()
    write(videos)
    print("+----list----+")
    videos = read_video_txt()
    print_videos(videos)


main()
