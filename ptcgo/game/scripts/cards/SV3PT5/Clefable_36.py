from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _extra_prize(ctx):
    """The opponent takes 1 more Prize card(s) if this attack Knocks Out their Active."""
    ctx.add_extra_prize_watcher(prizes=1)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="3e47f482-29a2-5306-b17a-aec16600f148",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Follow Me",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="More Moon",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            effect=_extra_prize,
        ),
    ],
)