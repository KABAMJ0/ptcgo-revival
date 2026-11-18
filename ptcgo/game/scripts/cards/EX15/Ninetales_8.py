from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7444384e-6632-5950-bf00-b956b033824a",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales δ",
    searchable_by=["Ninetales \u03b4", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=38,
    abilities=[
        Ability(
            title="Volunteer",
            game_text="Once during your turn (before your attack), you may remove 4 damage counters from Ninetales and discard Ninetales from Vulpix. If you do, search your deck for Ninetales or Ninetales ex and put it onto Vulpix (this counts as evolving Vulpix). Shuffle your deck afterward.",
            effect=unimplemented,
        ),
        Attack(
            title="Trick Tail",
            game_text="Search your discard pile for an Energy card and attach it to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)