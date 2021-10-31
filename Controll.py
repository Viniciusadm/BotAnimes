class Controll:
    @staticmethod
    def nextEpisode(fillers, current) -> int:
        next_episode = current + 1
        while (next_episode in fillers):
            next_episode += 1

        return next_episode