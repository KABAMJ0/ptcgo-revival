from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _searching_light(ctx):
    prizes = ctx.face_down_prize_cards()
    if not prizes:
        return
    picks = await ctx.choose_cards(
        prizes, 1, minimum=1,
        prompt="Choose 1 of your face-down Prize cards to look at")
    if picks:
        await ctx.reveal_cards(picks, to_player=ctx.player_id)


card = PokemonCardDef(
    guid="eadfb806-7ec6-564a-aaef-586e5c14d6ad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic", "Chinchou"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=170,
    abilities=[
        Attack(
            title="Searching Light",
            game_text="Look at 1 of your face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_searching_light,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)