from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ead5ac2-1c05-5404-aeda-1f46588e42b9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitanex.Name",
    display_name="Cetitan ex",
    searchable_by=["Cetitan ex", "Stage 1", "ex", "Cetitanex"],
    subtypes=["Stage 1", "ex"],
    collector_number=65,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Ability(
            title="Snow Camouflage",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Crushing Press",
            game_text="You may discard a Stadium in play. If you do, this attack does 140 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)