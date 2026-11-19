from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive


async def blustery_wind(ctx):
    """120 damage; you may discard the Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="7157626b-581d-54a7-9d7b-aaec4610b729",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dubwool.Name",
    display_name="Dubwool",
    searchable_by=["Dubwool", "Stage 1", "Dubwool"],
    subtypes=["Stage 1"],
    collector_number=125,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    family_id=831,
    abilities=[
        Ability(
            title="Soft Wool",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=blustery_wind,
        ),
    ],
)