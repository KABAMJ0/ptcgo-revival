from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def _look_at_hand_then_shuffle(ctx):
    results = await ctx.flip_coins(1, "Threaten")
    if not (results and results[0]):
        return
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    trainers = [card for card in hand
                if card.get_attribute(AttrID.TRAINER_TYPE) is not None]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=0,
        prompt="Choose a Trainer card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(list(picks), ctx.opponent_id)

card = PokemonCardDef(
    guid="43ae2cfd-512d-535e-b804-c5118c468a9f",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkScizor.Name",
    display_name="Dark Scizor",
    searchable_by=["Dark Scizor", "Stage 1", "DarkScizor"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Threaten",
            game_text="Flip a coin. If heads, look at your opponent's hand. If he or she has any Trainer cards there, choose 1 of them. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_look_at_hand_then_shuffle,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)