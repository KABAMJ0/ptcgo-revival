from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _extra_prize(ctx):
    """The opponent takes 1 more Prize card(s) if this attack Knocks Out their Active."""
    ctx.add_extra_prize_watcher(prizes=1)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="946cfca0-8f41-53cb-87db-2aefcb621428",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=201,
    abilities=[
        Attack(
            title="Mysterious Signal",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=_extra_prize,
        ),
    ],
)