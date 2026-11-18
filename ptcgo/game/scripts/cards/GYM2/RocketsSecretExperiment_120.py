from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_trainer_card

async def _rockets_secret_experiment(ctx):
    faces = await ctx.flip_coins(1, title="Rocket's Secret Experiment")
    if faces and faces[0]:
        found = await ctx.search_deck(
            None, count=1, minimum=0,
            prompt="Choose a card to put into your hand")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
        return
    ctx.lock_plays(ctx.player_id, is_trainer_card)


card = ItemCardDef(
    guid="1ae6d970-ac31-55fd-b0e0-24e7cfbd7f74",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSecretExperiment.Name",
    display_name="Rocket's Secret Experiment",
    searchable_by=["Rocket's Secret Experiment"],
    subtypes=[],
    collector_number=120,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=_rockets_secret_experiment
)
